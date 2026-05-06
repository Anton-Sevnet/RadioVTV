# Дыхание ВТВ · 1219 кГц · Заполярье

Автономная AM-радиостанция на Кольском полуострове. Сайт-руководство по сборке: магниевые ячейки в бочках, антенна на соснах, водяное заземление «Звезда» в озере — и плейлист в эфире без рекламы и повторов.

**Сайт:** [alttechno.ru/RadioVTV](https://alttechno.ru/RadioVTV)

---

## Стек

- **Vite 5** + **Vue 3** (Composition API) + **Tailwind CSS 3**
- **Chart.js 4** — графики мощности и тепловыделения по месяцам
- **Three.js** — интерактивная 3D-сцена размещения антенны
- **Vue lightbox-галерея** — полноразмерные фото с preload, blur/loading-индикацией, wheel-навигацией и `Ctrl + wheel` масштабом
- Деплой через **GitHub Actions** → SCP → **Bitrix24** на `alttechno.ru`

## Структура

```
src/
  components/   # секции страницы + PhotoGallery.vue
  constants/    # данные: смета, приёмники, шаги сборки, картинки
  App.vue / main.js / style.css
assets/                             # полноразмерные фото для галереи
index.html                          # SEO-метатеги, OG, JSON-LD
vite.config.js / tailwind.config.js
.github/
  workflows/deploy.yml              # CI/CD: npm build → python → SCP
  scripts/build_presentation.py     # оборачивает dist/ в PHP-пролог Bitrix
www/urlrewrite.php                  # ЧПУ-правила: /RadioVTV и /dvtv
```

## Быстрый старт (локально)

```bash
npm install
npm run dev       # dev-сервер на localhost:5173
npm run build     # production-сборка в dist/
```

## Деплой

Автоматически при пуше в `main`:

```
npm ci → npm run build → python .github/scripts/build_presentation.py → SCP → alttechno.ru
```

Собранный `dist/index.html` оборачивается в PHP-пролог Bitrix, JS/CSS-чанки, корневые превью `.jpg` и папка `assets/` с полноразмерной галереей загружаются в `/local/presentations/power_system_zapolyarye/`.

## О проекте

Там, где заканчивается сеть, начинается эфир. В глубине Кольского полуострова нет FM, нет интернета, телефон молчит. Здесь мы строим «Дыхание ВТВ» — радиомаяк на **1219 кГц** (СВ): несколько бочек в земле с магниевыми анодами вместо розетки, озеро как антенное заземление, провод по соснам вместо мачты. Инженерный северный челлендж: природа, рыбалка, работа руками — и свой голос в эфире.

**Связь:** [@sevnet](https://t.me/sevnet)
