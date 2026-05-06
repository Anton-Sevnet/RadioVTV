<template>
  <section id="philosophy" class="section-card border-l-4 border-accent-blue">
    <h2 class="section-heading">
      <span class="text-accent-blue">1.</span>
      Философия: «Практичность вместо микроамперов»
    </h2>

    <p class="text-gray-300 mb-4">
      Химическая батарея (3 бочки ПНД) стабильно генерирует
      <strong class="text-white">8–20 Вт мощности</strong>.
      Мы выделяем на питание «мозгов»
      <strong class="text-white">до 1 Ватта</strong>
      (что с запасом перекрывает любые нужды), а всю остальную энергию направляем в антенну
      через высокоэффективный MOSFET-ключ (Class-E).
      Это позволяет собрать передатчик из готовых, дешёвых модулей с маркетплейсов,
      с минимальным использованием паяльника.
    </p>

    <div class="grid md:grid-cols-3 gap-4 mt-6">
      <div
        v-for="card in cards"
        :key="card.label"
        :class="['bg-white/[0.03] rounded-xl p-4 border', card.border]"
      >
        <div :class="['text-2xl font-bold font-mono mb-1', card.color]">{{ card.value }}</div>
        <div class="text-sm font-semibold text-white mb-1">{{ card.label }}</div>
        <div class="text-xs text-gray-400">{{ card.sub }}</div>
      </div>
    </div>
  </section>
</template>

<script setup>
const cards = [
  { value: '8–20 Вт', label: 'Полная мощность', sub: 'Три ячейки в зависимости от температуры грунта', color: 'text-accent-amber', border: 'border-accent-amber/20' },
  { value: '≤ 1 Вт',  label: 'На логику',       sub: 'Arduino Nano + DFPlayer Mini через MT3608 (5В)', color: 'text-accent-blue',  border: 'border-accent-blue/20' },
  { value: '> 90%',   label: 'КПД ключа',        sub: 'MOSFET класса E — почти вся энергия в антенну', color: 'text-accent-green', border: 'border-accent-green/20' },
]
</script>
