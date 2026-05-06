<script setup>
import { img, PHOTOS } from '../constants/images.js'
</script>

<template>
  <header class="relative overflow-hidden">
    <!-- Aurora gradient overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-blue-950/60 via-night/20 to-night pointer-events-none z-10" />
    <div class="absolute top-0 left-1/4 w-96 h-96 bg-accent-green/10 rounded-full blur-3xl pointer-events-none" />
    <div class="absolute top-0 right-1/4 w-96 h-96 bg-accent-blue/10 rounded-full blur-3xl pointer-events-none" />

    <!-- Photo grid -->
    <div class="grid grid-cols-3 gap-0.5 max-h-72 overflow-hidden opacity-60">
      <div
        v-for="photo in PHOTOS"
        :key="photo.src"
        class="overflow-hidden"
      >
        <img
          :src="img(photo.src)"
          :alt="photo.alt"
          class="w-full h-24 md:h-36 object-cover"
          loading="lazy"
        />
      </div>
    </div>

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
