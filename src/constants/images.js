export const ASSET_BASE =
  (typeof window !== 'undefined' && window.ASSET_BASE) ||
  '/local/presentations/power_system_zapolyarye/'

export const img = (name) => ASSET_BASE + name

export const PHOTOS = [
  { src: 'aleksei-oborotov-oborotov-aleksei-murmanskaia-oblast-zapolia.jpg',         alt: 'Озеро в Заполярье' },
  { src: 'khibiny-kolskii-poluostrov-rossiia-doroga-zakat-gory-ozero-d.jpg',         alt: 'Дорога на закате у озера' },
  { src: 'konstantin-voronov-kolskii-poluostrov-gory-khibiny-pereval-k.jpg',         alt: 'Перевал в Хибинах' },
  { src: 'konstantin-voronov-kolskii-poluostrov-khibiny-gory-ozero-ras.jpg',         alt: 'Рассвет над озером' },
  { src: 'konstantin-voronov-kolskii-poluostrov-khibiny-gory-priroda-p.jpg',         alt: 'Природа Заполярья' },
  { src: 'konstantin-voronov-priroda-peizazh-kolskii-poluostrov-gory-k.jpg',         alt: 'Пейзаж гор и водоёма' },
]
