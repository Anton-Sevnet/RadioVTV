<template>
  <section id="underground" class="section-card">
    <h2 class="section-heading">
      <span class="text-gray-500">3.</span>
      Подземное размещение и Приоритет Питания
    </h2>

    <p class="text-gray-300 mb-4">
      Бочки будут <strong class="text-white">закопаны под землю</strong>, а зимой дополнительно укрыты снегом.
      Это гарантирует, что температура внутри даже в лютые морозы не опустится ниже −10°C.
      Вся вырабатываемая мощность строго распределяется по приоритетам.
    </p>

    <div class="bg-blue-950/30 border border-accent-blue/30 rounded-xl p-5">
      <h3 class="text-white font-bold mb-4 flex items-center gap-2">
        <span class="text-accent-blue">⚡</span>
        Железобетонный приоритет: Мозги → Антенна
      </h3>

      <div class="space-y-3">
        <div
          v-for="p in priorities"
          :key="p.num"
          :class="['flex gap-4 p-3 rounded-lg', p.bg]"
        >
          <div :class="['shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold', p.numBg]">
            {{ p.num }}
          </div>
          <div>
            <div :class="['font-semibold text-sm mb-1', p.color]">{{ p.title }}</div>
            <p class="text-gray-400 text-sm leading-relaxed" v-html="p.text" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const priorities = [
  {
    num: 1,
    title: 'Приоритет №1 — Генерация',
    text: 'Вся мощность первоочередно направляется на DC-DC преобразователь (MT3608). Он обеспечивает 5В для питания Arduino и DFPlayer.',
    bg: 'bg-amber-950/30',
    numBg: 'bg-accent-amber/20 text-accent-amber',
    color: 'text-accent-amber',
  },
  {
    num: '💤',
    title: 'Режим ожидания (Сон)',
    text: 'Если мощности недостаточно (мороз), DC-DC преобразователь отключается. Arduino и плеер «засыпают» и ждут достаточной мощности.',
    bg: 'bg-gray-800/30',
    numBg: 'bg-gray-600/30 text-gray-400',
    color: 'text-gray-300',
  },
  {
    num: 2,
    title: 'Приоритет №2 — Излучатель',
    text: 'Как только «мозгам» хватает энергии, <strong class="text-white">всё, что есть сверху</strong>, уходит в силовой ключ (MOSFET) и отправляется в антенну. Никакого сброса мощности в тепло — вся лишняя энергия летит в эфир!',
    bg: 'bg-green-950/30',
    numBg: 'bg-accent-green/20 text-accent-green',
    color: 'text-accent-green',
  },
]
</script>
