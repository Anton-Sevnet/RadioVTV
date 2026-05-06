<template>
  <section id="housing" class="section-card border-l-4 border-accent-amber">
    <h2 class="section-heading">
      <span class="text-accent-amber">9.</span>
      Корпус: Прозрачная заливка компаундом
    </h2>

    <p class="text-gray-300 mb-4">
      Под землёй (особенно рядом с водяным заземлением) — 100% влажность.
      Любой лак или коробка IP68 рано или поздно пустит конденсат, и плата сгниёт.
    </p>

    <div class="success-box mb-6">
      <strong class="text-white">Решение:</strong> Монолитная заливка, как в блоках управления стиральными машинами.
      Прозрачный силиконовый компаунд — всегда видно состояние паек, плюс силикон мягкий и не оторвёт детали при морозе
      (в отличие от эпоксидки).
    </div>

    <div class="bg-white/[0.03] border border-white/10 rounded-xl p-5">
      <h3 class="text-white font-semibold mb-4">Процесс заливки:</h3>
      <ol class="space-y-3">
        <li
          v-for="(step, i) in housingSteps"
          :key="i"
          class="flex gap-3 text-sm text-gray-300"
        >
          <span class="shrink-0 w-6 h-6 rounded-full bg-accent-amber/20 text-accent-amber flex items-center justify-center text-xs font-bold">
            {{ i + 1 }}
          </span>
          <span v-html="step" />
        </li>
      </ol>
    </div>
  </section>
</template>

<script setup>
const housingSteps = [
  'Покупаем <strong class="text-white">Силиконовый компаунд прозрачный ПК-68 или Гермоизол ПЗСК</strong> (двухкомпонентный, Ozon, ВсеИнструменты или Чип и Дип).',
  'Берём обычный пластиковый пищевой контейнер по размеру вашей гирлянды из модулей.',
  'Сверлим в боковой стенке дырки, продеваем провода (питание, антенна, заземление). Щели залепляем пластилином или термоклеем снаружи.',
  'Укладываем платы на дно (можно капнуть термоклеем, чтобы не всплыли).',
  'Смешиваем компаунд по инструкции и заливаем контейнер до краёв. Оставляем на 24 часа.',
  '<strong class="text-white">Важно:</strong> Слот для MicroSD карты на DFPlayer должен быть либо выведен за пределы силикона (чтобы менять флешку), либо заливается намертво с флешкой на 128 ГБ внутри. Если заливаете намертво — заклейте щель слота малярным скотчем перед заливкой!',
]
</script>
