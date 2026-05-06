from pathlib import Path
import html
import re
import shutil


ROOT = Path(__file__).resolve().parents[2]
DEPLOY_DIR = ROOT / "deploy"
SOURCE_HTML = ROOT / "power-system-zapolyarye-transmitter-guide.html"
REMOTE_ASSET_BASE = "/local/presentations/power_system_zapolyarye/"

IMAGES = [
    "aleksei-oborotov-oborotov-aleksei-murmanskaia-oblast-zapolia.jpg",
    "khibiny-kolskii-poluostrov-rossiia-doroga-zakat-gory-ozero-d.jpg",
    "konstantin-voronov-kolskii-poluostrov-gory-khibiny-pereval-k.jpg",
    "konstantin-voronov-kolskii-poluostrov-khibiny-gory-ozero-ras.jpg",
    "konstantin-voronov-kolskii-poluostrov-khibiny-gory-priroda-p.jpg",
    "konstantin-voronov-priroda-peizazh-kolskii-poluostrov-gory-k.jpg",
]


def main() -> None:
    DEPLOY_DIR.mkdir(exist_ok=True)
    source = SOURCE_HTML.read_text(encoding="utf-8")

    title_match = re.search(r"<title>(.*?)</title>", source, re.S)
    title = html.unescape(title_match.group(1).strip()) if title_match else "Дыхание ВТВ"
    title_php = title.replace("\\", "\\\\").replace("'", "\\'")

    source = re.sub(
        r"<title>.*?</title>",
        "<title><?php $APPLICATION->ShowTitle(); ?></title>",
        source,
        count=1,
        flags=re.S,
    )

    for image in IMAGES:
        source = source.replace(
            f'src="{image}"',
            f'src="<?= htmlspecialcharsbx($presentationsAssetBase) ?>{image}"',
        )
        shutil.copy2(ROOT / image, DEPLOY_DIR / image)

    php_header = f"""<?php
define('STOP_STATISTICS', true);
define('NO_AGENT_CHECK', true);
require_once $_SERVER['DOCUMENT_ROOT'] . '/bitrix/modules/main/include/prolog_before.php';
$APPLICATION->SetTitle('{title_php}');
$presentationsAssetBase = '{REMOTE_ASSET_BASE}';
?>
"""

    (DEPLOY_DIR / "index.php").write_text(php_header + source, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
