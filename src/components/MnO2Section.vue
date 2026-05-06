<template>
  <section id="mno2" class="section-card">
    <h2 class="section-heading">
      <span class="text-gray-500">2.</span>
      Рост эффективности за счёт Диоксида Марганца (Пиролюзита)
    </h2>

    <p class="text-gray-300 mb-4">
      Обычный графитовый катод быстро подвергается
      <strong class="text-white">газовой поляризации</strong>
      (покрывается пузырьками водорода), что увеличивает внутреннее сопротивление и роняет ток.
      Добавление «куклы» с диоксидом марганца (MnO₂) решает эту проблему кардинально.
    </p>

    <div class="grid md:grid-cols-3 gap-4 mt-4">
      <div
        v-for="benefit in benefits"
        :key="benefit.title"
        class="bg-white/[0.03] rounded-xl p-4 border border-white/10"
      >
        <div class="text-accent-green text-sm font-bold mb-2">{{ benefit.icon }} {{ benefit.title }}</div>
        <p class="text-gray-400 text-sm leading-relaxed">{{ benefit.text }}</p>
        <div v-if="benefit.stat" class="mt-2 text-xl font-bold font-mono text-accent-green">{{ benefit.stat }}</div>
      </div>
    </div>
  </section>
</template>

<script setup>
const benefits = [
  {
    icon: '🔥',
    title: 'Химическое сжигание водорода',
    text: 'MnO₂ выступает деполяризатором, окисляя выделяющийся водород до воды. Газовая плёнка не образуется.',
    stat: null,
  },
  {
    icon: '⚡',
    title: 'Увеличение токоотдачи',
    text: 'Эффективность ячейки вырастает по сравнению с голым графитом. Ток больше не проседает под нагрузкой.',
    stat: '×3–5',
  },
  {
    icon: '📊',
    title: 'Кулоновская эффективность',
    text: 'Химическая энергия магния расходуется на полезный ток, а не на паразитные побочные реакции.',
    stat: '80–90%',
  },
]
</script>
