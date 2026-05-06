<script setup>
import { ref, computed } from 'vue'
import { img, imgAsset, PHOTOS, GALLERY_PHOTOS } from '../constants/images.js'
import PhotoGallery from './PhotoGallery.vue'

const galleryIndex = ref(null)
function openGallery(i) { galleryIndex.value = i }

// Полноразмерные фото с resolved URL — открываются в просмотрщике
const galleryPhotos = computed(() =>
  GALLERY_PHOTOS.map(p => ({ ...p, src: imgAsset(p.src) }))
)

// Соответствие: индекс превью-фото → индекс в галерее (по имени файла)
function previewToGallery(i) {
  const previewSrc = PHOTOS[i].src
  const gi = GALLERY_PHOTOS.findIndex(p => p.src === previewSrc)
  return gi >= 0 ? gi : 0
}
</script>

<template>
  <header class="relative overflow-hidden">
    <!-- Aurora gradient overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-blue-950/60 via-night/20 to-night pointer-events-none z-10" />
    <div class="absolute top-0 left-1/4 w-96 h-96 bg-accent-green/10 rounded-full blur-3xl pointer-events-none" />
    <div class="absolute top-0 right-1/4 w-96 h-96 bg-accent-blue/10 rounded-full blur-3xl pointer-events-none" />

    <!-- Photo grid + Gallery button -->
    <div class="relative">
      <div class="grid grid-cols-3 gap-0.5 max-h-72 overflow-hidden opacity-60">
        <div
          v-for="(photo, i) in PHOTOS"
          :key="photo.src"
          class="overflow-hidden cursor-pointer"
          @click="openGallery(previewToGallery(i))"
        >
          <img
            :src="img(photo.src)"
            :alt="photo.alt"
            class="w-full h-24 md:h-36 object-cover transition-opacity hover:opacity-80"
            loading="lazy"
          />
        </div>
      </div>

      <!-- Кнопка Галерея — поверх фото, правый нижний угол -->
      <button
        class="absolute bottom-20 right-4 z-30 flex items-center gap-2 px-6 py-3 rounded-xl font-bold text-base text-white shadow-xl
               bg-gradient-to-r from-blue-700 to-emerald-700 hover:from-blue-600 hover:to-emerald-600
               ring-1 ring-emerald-400/30 hover:ring-emerald-400/60
               transition-all duration-150 hover:-translate-y-0.5 active:translate-y-0"
        @click="openGallery(0)"
        title="Открыть галерею фотографий"
      >
        <svg class="w-5 h-5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="2"/>
          <circle cx="8.5" cy="8.5" r="1.5"/>
          <polyline points="21 15 16 10 5 21"/>
        </svg>
        Галерея
      </button>
    </div>

    <!-- Модальный просмотрщик (полноразмерные фото из assets/) -->
    <PhotoGallery v-model="galleryIndex" :images="galleryPhotos" />

    <!-- Hero content -->
    <div class="relative z-20 max-w-7xl mx-auto px-4 py-10 -mt-16">
      <div class="bg-night/80 backdrop-blur-md border border-white/10 rounded-2xl p-6 md:p-10">
        <div class="flex flex-wrap items-start gap-4 mb-4">
          <h1 class="text-3xl md:text-4xl font-bold leading-tight">
            Радиостанция «Дыхание ВТВ»
          </h1>
          <span class="badge bg-accent-blue/20 text-accent-blue border border-accent-blue/40 text-sm self-start mt-1">
            1219 кГц · СВ · вещание
          </span>
        </div>

        <p class="text-gray-300 text-base md:text-lg leading-relaxed mb-6 max-w-4xl">
          <strong class="text-white">Там, где заканчивается сеть, начинается эфир.</strong>
          В заполярных местах вокруг ВТВ телефон молчит, интернет исчезает, FM-шкала шипит пустотой,
          а вокруг остаются только озёра, сосны, камень, ветер и огромное небо.
          В этом девственном крае мы создаём «Дыхание ВТВ» — автономную радиостанцию на
          <strong class="text-white">1219 кГц</strong>, которая будет звучать как северный маяк.
          Немного мистики УВБ-76, немного походной романтики, немного инженерного безумия:
          бочки в земле, заземляющая «звезда» в воде, провод по соснам и плейлист на годы без рекламы и повторов.
        </p>

        <p class="text-gray-400 text-sm leading-relaxed max-w-3xl">
          Практическое руководство по динамической магниевой установке: модульная электроника «без паяльной паранойи»,
          прозрачная заливка силиконом и высокоэффективное водяное заземление «Звезда».
          Целевая несущая в эфире — <strong class="text-white">1219 кГц</strong> (средние волны).
        </p>
      </div>
    </div>
  </header>
</template>
