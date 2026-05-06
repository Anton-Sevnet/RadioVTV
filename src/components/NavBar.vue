<script setup>
const sections = [
  { id: 'overview',    label: 'Обзор' },
  { id: 'philosophy',  label: '1. Философия' },
  { id: 'mno2',        label: '2. MnO₂' },
  { id: 'underground', label: '3. Размещение' },
  { id: 'barrel',      label: '4. Схема бочки' },
  { id: 'chemistry',   label: '5. Реакции' },
  { id: 'charts',      label: '6. Графики' },
  { id: 'diagram',     label: '7. Блок-схема' },
  { id: 'assembly',    label: '8. Сборка' },
  { id: 'antenna',     label: '8.1 Антенна' },
  { id: 'housing',     label: '9. Корпус' },
  { id: 'budget',      label: '10. Смета' },
  { id: 'receivers',   label: '11. Приёмники' },
  { id: 'audio',       label: '12. Аудио' },
]

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
</script>

<template>
  <nav class="sticky top-0 z-50 bg-night/90 backdrop-blur-md border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 py-2 flex items-center gap-1 overflow-x-auto scrollbar-hide">
      <div class="flex items-center gap-2 mr-4 shrink-0">
        <span class="badge bg-accent-green/20 text-accent-green border border-accent-green/30 font-mono text-xs">
          📻 1219 кГц
        </span>
      </div>
      <button
        v-for="s in sections"
        :key="s.id"
        class="shrink-0 px-2.5 py-1 rounded-lg text-xs text-gray-400 hover:text-white hover:bg-white/10 transition-all whitespace-nowrap"
        @click="scrollTo(s.id)"
      >
        {{ s.label }}
      </button>
    </div>
  </nav>
</template>
