"""
Build script: wraps Vite's dist/index.html in a Bitrix PHP prolog
and copies the entire dist/ to deploy/.

Changes from original:
- Source is now dist/index.html (Vite build output) instead of the raw HTML file.
- Injects window.ASSET_BASE PHP snippet so Vue components can resolve image URLs.
- Copies the full dist/ directory tree (JS, CSS bundles) instead of just one file.
- Still copies .jpg images that live alongside the dist (they are not in the Vite bundle).
"""
from pathlib import Path
import re
import shutil


ROOT       = Path(__file__).resolve().parents[2]
DIST_DIR   = ROOT / "dist"
DEPLOY_DIR = ROOT / "deploy"
REMOTE_ASSET_BASE = "/local/presentations/power_system_zapolyarye/"

IMAGES = [
    "aleksei-oborotov-oborotov-aleksei-murmanskaia-oblast-zapolia.jpg",
    "khibiny-kolskii-poluostrov-rossiia-doroga-zakat-gory-ozero-d.jpg",
    "konstantin-voronov-kolskii-poluostrov-gory-khibiny-pereval-k.jpg",
    "konstantin-voronov-kolskii-poluostrov-khibiny-gory-ozero-ras.jpg",
    "konstantin-voronov-kolskii-poluostrov-khibiny-gory-priroda-p.jpg",
    "konstantin-voronov-priroda-peizazh-kolskii-poluostrov-gory-k.jpg",
]

TITLE = "Дыхание ВТВ — 1219 кГц (СВ) | Динамическая магниевая радиостанция (3 ячейки) — Передатчик и заземление"


def main() -> None:
    if not DIST_DIR.exists():
        raise FileNotFoundError(
            f"Vite dist directory not found at {DIST_DIR}. Run `npm run build` first."
        )

    # Clean and recreate deploy dir
    if DEPLOY_DIR.exists():
        shutil.rmtree(DEPLOY_DIR)
    DEPLOY_DIR.mkdir(parents=True)

    # Copy entire dist tree (JS bundles, CSS, sourcemaps, etc.)
    for item in DIST_DIR.rglob("*"):
        if item.name == "index.html":
            continue  # handled separately below
        dest = DEPLOY_DIR / item.relative_to(DIST_DIR)
        if item.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest)

    # Copy images (not in Vite bundle – served from the same directory on server)
    for image in IMAGES:
        src = ROOT / image
        if src.exists():
            shutil.copy2(src, DEPLOY_DIR / image)

    # Copy full-resolution gallery images from assets/
    assets_src = ROOT / "assets"
    assets_dst = DEPLOY_DIR / "assets"
    if assets_src.exists():
        assets_dst.mkdir(parents=True, exist_ok=True)
        for f in assets_src.iterdir():
            if f.is_file():
                shutil.copy2(f, assets_dst / f.name)

    # Process index.html: inject PHP prolog + ASSET_BASE
    source = (DIST_DIR / "index.html").read_text(encoding="utf-8")

    title_php = TITLE.replace("\\", "\\\\").replace("'", "\\'")

    # Replace <title> with Bitrix dynamic title
    source = re.sub(
        r"<title>.*?</title>",
        "<title><?php $APPLICATION->ShowTitle(); ?></title>",
        source,
        count=1,
        flags=re.S,
    )

    # Inject window.ASSET_BASE right after <head> opening tag
    asset_base_script = (
        "<script>window.ASSET_BASE='<?= htmlspecialcharsbx($presentationsAssetBase) ?>';</script>"
    )
    source = source.replace("<head>", f"<head>\n  {asset_base_script}", 1)

    php_header = f"""<?php
define('STOP_STATISTICS', true);
define('NO_AGENT_CHECK', true);
require_once $_SERVER['DOCUMENT_ROOT'] . '/bitrix/modules/main/include/prolog_before.php';
$APPLICATION->SetTitle('{title_php}');
$presentationsAssetBase = '{REMOTE_ASSET_BASE}';
?>
"""

    (DEPLOY_DIR / "index.php").write_text(
        php_header + source, encoding="utf-8", newline="\n"
    )

    print(f"Build complete. Deploy directory: {DEPLOY_DIR}")
    print(f"  Files: {sum(1 for _ in DEPLOY_DIR.rglob('*') if _.is_file())}")


if __name__ == "__main__":
    main()
