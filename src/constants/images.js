export const ASSET_BASE =
  (typeof window !== 'undefined' && window.ASSET_BASE) ||
  '/local/presentations/power_system_zapolyarye/'

export const img      = (name) => ASSET_BASE + name
export const imgAsset = (name) => ASSET_BASE + 'assets/' + name

/** Превью-сетка в шапке (маленькие файлы из корня) */
export const PHOTOS = [
  { src: 'aleksei-oborotov-oborotov-aleksei-murmanskaia-oblast-zapolia.jpg', alt: 'Озеро в Заполярье' },
  { src: 'khibiny-kolskii-poluostrov-rossiia-doroga-zakat-gory-ozero-d.jpg', alt: 'Дорога на закате у озера' },
  { src: 'konstantin-voronov-kolskii-poluostrov-gory-khibiny-pereval-k.jpg', alt: 'Перевал в Хибинах' },
  { src: 'konstantin-voronov-kolskii-poluostrov-khibiny-gory-ozero-ras.jpg', alt: 'Рассвет над озером' },
  { src: 'konstantin-voronov-kolskii-poluostrov-khibiny-gory-priroda-p.jpg', alt: 'Природа Заполярья' },
  { src: 'konstantin-voronov-priroda-peizazh-kolskii-poluostrov-gory-k.jpg', alt: 'Пейзаж гор и водоёма' },
]

/** Полноразмерные фото из assets/ — открываются в галерее */
export const GALLERY_PHOTOS = [
  { src: 'aleksei-oborotov-oborotov-aleksei-murmanskaia-oblast-zapolia.jpg', alt: 'Озеро в Заполярье', author: 'Алексей Оборотов' },
  { src: 'khibiny-kolskii-poluostrov-rossiia-doroga-zakat-gory-ozero-d.jpg', alt: 'Дорога на закате у озера' },
  { src: 'konstantin-voronov-kolskii-poluostrov-gory-khibiny-pereval-k.jpg', alt: 'Перевал в Хибинах', author: 'Константин Воронов' },
  { src: 'konstantin-voronov-kolskii-poluostrov-khibiny-gory-ozero-ras.jpg', alt: 'Рассвет над озером', author: 'Константин Воронов' },
  { src: 'konstantin-voronov-kolskii-poluostrov-khibiny-gory-priroda-p.jpg', alt: 'Природа Заполярья', author: 'Константин Воронов' },
  { src: 'konstantin-voronov-priroda-peizazh-kolskii-poluostrov-gory-k.jpg', alt: 'Пейзаж гор и водоёма', author: 'Константин Воронов' },
  { src: 'pavel-vashchenkov-kolskii-poluostrov-priroda-peizazh-gory-kh.jpg', alt: 'Горы Кольского полуострова', author: 'Павел Ващенков' },
  { src: 'vladimir-riabkov-khibiny-kolskii-poluostrov-murmanskaia-obla.jpg', alt: 'Хибины, Мурманская область', author: 'Владимир Рябков' },
  { src: 'vladimir-riabkov-priroda-peizazh-kolskii-poluostrov-khibiny.jpg',  alt: 'Природа Хибин', author: 'Владимир Рябков' },
]
