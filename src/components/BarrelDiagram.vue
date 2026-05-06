<script setup>
import { ref } from 'vue'
import FullscreenBtn from './FullscreenBtn.vue'

const containerRef = ref(null)
</script>

<template>
  <section id="barrel" class="section-card">
    <h2 class="section-heading">
      <span class="text-gray-500">4.</span>
      Конструкторская схема: Бочка с «Куклой»
    </h2>

    <p class="text-gray-400 text-sm mb-4">
      Для стабильной работы зимой ячейка помещается ниже уровня промерзания почвы или укрывается снегом.
    </p>

    <div ref="containerRef" class="relative overflow-auto rounded-xl border border-white/10 bg-[#1a1a1a] p-2 vtv-svg-fs">
      <FullscreenBtn :target-ref="containerRef" />
      <svg viewBox="0 0 1000 700" class="w-full max-w-full" style="min-width:560px; height:auto;">
        <rect width="1000" height="700" fill="#1a1a1a" />
        <!-- Бочка (Контур) -->
        <path d="M 200 100 L 200 650 C 200 670 220 680 250 680 L 550 680 C 580 680 600 670 600 650 L 600 100" fill="none" stroke="#607d8b" stroke-width="8" />
        <path d="M 180 100 L 620 100 L 620 80 L 180 80 Z" fill="#455a64" />
        <text x="210" y="60" fill="#b0bec5" font-size="16" font-weight="bold">Бочка ПНД 65л (Под землей)</text>
        <!-- Электролит -->
        <rect x="204" y="190" width="392" height="486" fill="rgba(52, 152, 219, 0.2)" />
        <path d="M 204 190 Q 300 200 400 190 T 596 190" fill="none" stroke="#3498db" stroke-width="2" />
        <!-- Масляный затвор -->
        <rect x="204" y="150" width="392" height="40" fill="rgba(241, 196, 15, 0.4)" />
        <path d="M 204 150 Q 300 160 400 150 T 596 150" fill="none" stroke="#f1c40f" stroke-width="2" />
        <!-- КАТОДНАЯ КУКЛА (Мешок + Пиролюзит + Графит) -->
        <rect x="235" y="170" width="160" height="350" fill="rgba(127, 140, 141, 0.8)" stroke="#bdc3c7" stroke-width="2" stroke-dasharray="4" rx="10" />
        <rect x="240" y="175" width="150" height="340" fill="#34495e" />
        <rect x="265" y="170" width="100" height="350" fill="#212121" stroke="#111" stroke-width="2" />
        <text x="320" y="340" fill="#9e9e9e" font-size="16" font-weight="bold" transform="rotate(-90 320 340)">ГРАФИТ</text>
        <!-- Контакт графита -->
        <rect x="310" y="130" width="10" height="40" fill="#90a4ae" />
        <circle cx="315" cy="140" r="8" fill="#ff7043" />
        <!-- Магниевый анод (ПМ-5У) -->
        <rect x="440" y="190" width="90" height="400" fill="#cfd8dc" stroke="#90a4ae" stroke-width="3" />
        <rect x="480" y="150" width="10" height="40" fill="#78909c" />
        <text x="495" y="400" fill="#455a64" font-size="18" font-weight="bold" transform="rotate(-90 495 400)">АНОД Mg</text>
        <circle cx="485" cy="170" r="8" fill="#ff7043" />
        <!-- Провода -->
        <path d="M 315 140 Q 315 100 150 100" fill="none" stroke="#e74c3c" stroke-width="5" />
        <path d="M 485 170 Q 485 80 150 80" fill="none" stroke="#3498db" stroke-width="5" />
        <text x="70" y="105" fill="#e74c3c" font-size="18" font-weight="bold">ПЛЮС (+)</text>
        <text x="60" y="85" fill="#3498db" font-size="18" font-weight="bold">МИНУС (-)</text>
        <!-- Выноски -->
        <line x1="395" y1="280" x2="650" y2="280" stroke="#fff" stroke-dasharray="4" />
        <text x="660" y="275" fill="#2ecc71" font-size="16" font-weight="bold">Слой Пиролюзита (MnO₂)</text>
        <text x="660" y="295" fill="#95a5a6" font-size="12">Устраняет водородную плёнку,</text>
        <text x="660" y="310" fill="#95a5a6" font-size="12">повышает отдачу тока в 3–5 раз</text>
        <line x1="530" y1="360" x2="650" y2="360" stroke="#fff" stroke-dasharray="4" />
        <text x="660" y="355" fill="#ecf0f1" font-size="16" font-weight="bold">Термоизоляция (Земля/Снег)</text>
        <text x="660" y="375" fill="#95a5a6" font-size="12">Не даёт остыть ниже −10°C</text>
        <path d="M 204 680 L 204 650 Q 300 640 400 660 T 596 640 L 596 680 Z" fill="rgba(149, 165, 166, 0.3)" />
      </svg>
    </div>
  </section>
</template>
