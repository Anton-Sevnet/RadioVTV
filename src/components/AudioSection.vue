<template>
  <section id="audio" class="section-card border-l-4 border-accent-purple">
    <h2 class="section-heading">
      <span class="text-accent-purple">12.</span>
      Подготовка музыки (NRSC / Психоакустика) — Задача для Python
    </h2>

    <p class="text-gray-300 mb-4">
      Физика АМ-радио обрежет любые частоты выше 4.5–5 кГц. Сырые MP3 на флешке в лесу будут звучать как
      неразборчивое гудение из ведра. Нужно применить стандарт NRSC Pre-emphasis.
    </p>

    <div class="bg-purple-950/30 border border-accent-purple/30 rounded-xl p-5">
      <h4 class="text-purple-300 font-bold mb-4">🛠 Планируемая автоматизация (ToDo):</h4>
      <p class="text-gray-300 text-sm mb-4">
        Python-скрипт с библиотеками <code>ffmpeg</code> / <code>pydub</code>, запускаемый перед копированием на MicroSD.
        Что делает с каждым файлом:
      </p>
      <ol class="space-y-3">
        <li
          v-for="(step, i) in audioSteps"
          :key="i"
          class="flex gap-3 text-sm text-gray-300"
        >
          <span class="shrink-0 w-6 h-6 rounded-full bg-purple-500/20 text-purple-300 flex items-center justify-center text-xs font-bold">
            {{ i + 1 }}
          </span>
          <span v-html="step" />
        </li>
      </ol>
    </div>
  </section>
</template>

<script setup>
const audioSteps = [
  '<strong class="text-white">Pre-emphasis (Эквалайзер):</strong> Задрать частоты от 2.5 кГц до 5 кГц на +8 дБ.',
  '<strong class="text-white">Low-Pass Filter:</strong> Жёстко отрезать (Brickwall) все частоты выше 5.5 кГц.',
  '<strong class="text-white">Жёсткая компрессия (Limiter):</strong> Поднять тихие участки музыки и обрезать пики для предотвращения перемодуляции.',
  '<strong class="text-white">Конвертация:</strong> Сохранить результат в унифицированный MP3 (или WAV) для DFPlayer.',
]
</script>
