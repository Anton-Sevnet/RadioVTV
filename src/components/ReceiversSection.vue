<template>
  <section id="receivers" class="section-card border-l-4 border-accent-amber">
    <h2 class="section-heading">
      <span class="text-accent-amber">📻</span>
      Рекомендуемые приёмники для СВ-диапазона (AM / Средние Волны)
    </h2>

    <p class="text-gray-300 mb-2 text-sm">
      Для уверенного приёма сигнала на СВ (526–1606 кГц) нужны приёмники с встроенной ферритовой антенной
      и режимом «AM» или «СВ». Настройтесь на <strong class="text-white">1219 кГц</strong> — частота «Дыхания ВТВ».
    </p>

    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
      <div
        v-for="r in receivers"
        :key="r.num"
        class="receiver-card"
      >
        <div class="flex items-start justify-between gap-2">
          <h4 class="text-accent-teal font-semibold text-sm">{{ r.num }}. {{ r.name }}</h4>
        </div>
        <p class="text-gray-400 text-xs leading-relaxed flex-1">{{ r.desc }}</p>
        <div class="flex items-center justify-between pt-2 border-t border-white/10">
          <span class="text-accent-amber font-mono text-sm font-bold">{{ r.price }}</span>
          <div class="flex gap-1">
            <a
              v-for="link in r.links"
              :key="link.label"
              :href="link.url"
              target="_blank"
              rel="noopener"
              :class="['text-xs px-2 py-1 rounded text-white no-underline hover:opacity-80 transition-opacity', link.color]"
            >{{ link.label }}</a>
          </div>
        </div>
      </div>
    </div>

    <div class="highlight-box mt-6 text-sm">
      <strong class="text-white">Важно:</strong> На СВ (AM) волну ловит не телескопическая антенна (она для FM/КВ),
      а встроенная <strong class="text-white">магнитная (ферритовая) антенна</strong>. Для лучшего приёма
      сам корпус приёмника нужно вращать в пространстве — он имеет ярко выраженную направленность «восьмёркой».
    </div>
  </section>
</template>

<script setup>
import { RECEIVERS } from '../constants/receivers.js'
const receivers = RECEIVERS
</script>
