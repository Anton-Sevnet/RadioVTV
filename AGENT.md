# AGENT.md — Радиостанция «Дыхание ВТВ» · 1219 кГц · Кольский полуостров

Рабочий файл для AI-агентов. Содержит архитектуру проекта, правила работы с кодом, деплой-пайплайн и техническую базу знаний.

---

## Проект одной строкой

Самодельная автономная AM-радиостанция на **1219 кГц** для Заполярья: магниевые гальванические ячейки в бочках ПНД → MOSFET-ключ класса E → антенна на соснах → водяное заземление «Звезда» в озере. Сайт-руководство с живыми схемами, графиками и сметой.

---

## Ключевые параметры (не менять без пересчёта)

| Параметр | Значение |
|---|---|
| Несущая частота | **1219 кГц** (СВ) |
| Мощность батареи | **8–20 Вт** (зависит от T° грунта, −10…+15°C) |
| Приоритет «мозгам» | ≤ **1 Вт** (MT3608 → 5В → Arduino + DFPlayer) |
| КПД усилителя | **90%** (MOSFET класс E) |
| КПД антенны | **22%** (короткая L-антенна + водяное заземление) |
| Интервал обслуживания | **≤ 14 месяцев** (чистка кукол от шлама, замена анодов) |
| Публичный URL | **https://alttechno.ru/RadioVTV** (алиас `/dvtv`) |

---

## Фронтенд: стек и архитектура

**Стек:** Vite 5 · Vue 3 (Composition API, `<script setup>`) · Tailwind CSS 3 · Chart.js 4 · Three.js 0.170

### Структура `src/`

```
src/
  main.js                      # точка входа Vue
  App.vue                      # корневой layout: NavBar + все секции + footer
  style.css                    # Tailwind directives + @layer components (section-card, highlight-box и т.д.)

  components/
    NavBar.vue                 # sticky top-nav, якорные ссылки на все секции
    HeroSection.vue            # заголовок + aurora-градиент + сетка 2×3 фото
    OverviewSection.vue        # «Что это» — карточки-фичи (id=overview)
    PhilosophySection.vue      # раздел 1 — философия и метрики (id=philosophy)
    MnO2Section.vue            # раздел 2 — деполяризатор пиролюзит (id=mno2)
    UndergroundSection.vue     # раздел 3 — подземное размещение, приоритет питания (id=underground)
    BarrelDiagram.vue          # раздел 4 — SVG-схема бочки с «куклой» (id=barrel)
    ChemistrySection.vue       # раздел 5 — химические реакции, зашламление (id=chemistry)
    PowerCharts.vue            # раздел 6 — Chart.js: мощность/дальность + тепловыделение (id=charts)
    BlockDiagram.vue           # раздел 7 — SVG-блок-схема передатчика (id=diagram)
    AssemblyGuide.vue          # раздел 8 — пошаговая сборка (id=assembly)
    AntennaScene.vue           # раздел 8.1 — Three.js 3D-сцена антенны (id=antenna)
    HousingSection.vue         # раздел 9 — заливка силиконовым компаундом (id=housing)
    BudgetTable.vue            # раздел 10 — таблица сметы (id=budget)
    CalibrationTable.vue       # раздел 10.1 — приборы пуско-наладки (id=calibration)
    ReceiversSection.vue       # раздел 11 — приёмники СВ-диапазона (id=receivers)
    AudioSection.vue           # раздел 12 — подготовка аудио NRSC (id=audio)

  constants/
    images.js                  # ASSET_BASE, список .jpg, функция img()
    budget.js                  # BUDGET_SECTIONS, BUDGET_TOTAL, CALIBRATION_ITEMS
    receivers.js               # RECEIVERS — массив 10 приёмников
    assembly.js                # ASSEMBLY_STEPS — шаги сборки передатчика
```

### Правила для агентов при редактировании

- **Один компонент = один раздел страницы.** Искать раздел по имени файла компонента.
- **Все стили — Tailwind-классы.** Inline-стили (`style=""`) не добавлять. Новые повторяющиеся паттерны выносить в `@layer components` в `style.css`.
- **Данные — в `constants/`.** Текстовые списки (смета, приёмники, шаги) хранятся в константах, а не внутри шаблонов компонентов.
- **SVG-схемы (BarrelDiagram, BlockDiagram) — не трогать** без явного запроса: там точные размеры и координаты схем.
- **Three.js и Chart.js** инициализируются в `onMounted` — код привязан к lifecycle. При изменении логики учитывать `onBeforeUnmount` для очистки.
- Для Chart.js используется `import { Chart, registerables }` — регистрация `Chart.register(...registerables)` обязательна.
- Картинки `.jpg` — **не в Vite-bundle**, хранятся отдельно на сервере. Путь: `img('filename.jpg')` из `constants/images.js`. `ASSET_BASE` инжектируется через PHP как `window.ASSET_BASE`.

---

## Деплой и инфраструктура

### Пайплайн (GitHub Actions → Bitrix)

```
git push → deploy.yml → npm ci → npm run build → python build_presentation.py → SCP
```

1. **`npm run build`** — Vite собирает `dist/`:
   - `dist/index.html` — точка входа
   - `dist/assets/vendor-vue-*.js` — Vue (~62 кБ gzip)
   - `dist/assets/vendor-chartjs-*.js` — Chart.js (~71 кБ gzip)
   - `dist/assets/vendor-three-*.js` — Three.js (~122 кБ gzip)
   - `dist/assets/index-*.js` / `*.css` — код приложения

2. **`.github/scripts/build_presentation.py`** — оборачивает `dist/index.html` в PHP-пролог Bitrix:
   - Добавляет `<?php define('NO_AGENT_CHECK',...); require prolog_before.php; ?>`
   - Заменяет `<title>` на `$APPLICATION->ShowTitle()`
   - Инжектирует `<script>window.ASSET_BASE='<?= htmlspecialcharsbx($presentationsAssetBase) ?>';</script>`
   - Копирует весь `dist/` + `.jpg`-изображения в `deploy/`

3. **SCP** — всё содержимое `deploy/` + `www/urlrewrite.php` загружается по SSH:
   - Хост: `at5.su`, порт `4422`, пользователь `bitrix`
   - Путь: `/home/bitrix/www/local/presentations/power_system_zapolyarye/`
   - Secret: `ALTTECHNO` (приватный SSH-ключ в GitHub Secrets)

### Роутинг Bitrix

`urlrewrite.php` содержит два правила ЧПУ:
- `/RadioVTV` → `/local/presentations/power_system_zapolyarye/index.php`
- `/dvtv` → то же (алиас)

### MCP SSH (прямое управление сервером)

Для диагностики и инспекции использовать:
- **`user-ssh-alttechno-root`** — root-доступ к серверу (`execute-command`)
- **`user-ssh-alttechno-bitrix`** — доступ под пользователем `bitrix` (файлы сайта, порт 4422)

Примеры задач через MCP:
```
# Проверить задеплоенные файлы
ls -la /home/bitrix/www/local/presentations/power_system_zapolyarye/

# Проверить статус сервисов
systemctl status nginx httpd mysqld

# Посмотреть логи Apache
tail -n 50 /var/log/httpd/error_log
```

---

## Техническая база знаний

### Химия ячеек

- **Анод:** Магниевый протектор ПМ-5У (Mg → Mg²⁺ + 2e⁻)
- **Катод:** Графит Ø150мм в «кукле» с пиролюзитом MnO₂
- **Электролит:** Хлорид кальция CaCl₂ (морозостойкость до −10°C)
- **Деполяризатор:** MnO₂ окисляет H₂ → воду, не давая газовой плёнке блокировать графит
- **Итоговая реакция:** `Mg + 2H₂O + 2MnO₂ → Mg(OH)₂↓ + 2MnO(OH)↓ + Q`
- **Проблема шлама:** Mg(OH)₂ и MnO(OH) нерастворимы, забивают поры куклы через 14 мес.
- **КПД с MnO₂:** токоотдача ×3–5 vs голый графит; кулоновский КПД 80–90%

### Электроника передатчика

| Модуль | Роль | Подключение |
|---|---|---|
| MT3608 | DC-DC boost 2.5–4.5В → 5В | IN± от бочек, OUT± к логике |
| Arduino Nano | ШИМ 1219 кГц, управление | 5В от MT3608, D9 → MOSFET |
| DFPlayer Mini | MP3/WAV с MicroSD | 5В от MT3608, DAC_R → A0 Arduino |
| MOSFET D4184/LR7843 | Силовой ключ класс E | VIN± прямо от бочек, SIG ← D9 |
| LC П-контур | ФНЧ, 100 мкГн + 2×1000 пФ | VOUT+ MOSFET → L → антенна |

**Важно:** светодиоды Arduino и DFPlayer скалывать — экономия энергии под землёй.

### Антенна и заземление

- **Полотно:** ПуГВ 4–6 мм² медь, 80–100 м, горизонтально по соснам на ~10 м
- **Изоляторы:** ИТО-20/40 (орешки), зазор к коре обязателен
- **Натяжение:** полиспасты + противовесы (мешок с камнем), тянуть постепенно, выдержать сутки
- **Заземление «Звезда»:** консервная банка (хаб) + 8 лучей медной плетёнки по 1.5–2 м, опускается на дно незамерзающего водоёма, паять свинцом

### Ресурсы для поиска практических данных

- **Guns.ru** — «Батарейка выживальщика», земляные батареи, магниевые аноды от бойлеров
- **nepropadu.ru** — пошаговые инструкции по солевым магниевым батареям
- **Radioscanner.ru** — питание раций от самодельных батарей, Joule Thief
- **usamodelkina.ru** — катодные «куклы» из угля и марганца
- **forum.xumuk.ru** — электрохимия, деполяризаторы, поведение Mg в CaCl₂
- **YouTube:** `earth battery`, `homemade magnesium battery`, `земляная батарея`
- **ITU-R P.368** — расчёт интенсивности поля наземной волны СВ
- **ITU-R P.833** — потери в лесу и растительности

---

## Контакт и связь

Telegram: [@sevnet](https://t.me/sevnet)
