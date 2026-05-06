<script setup>
import { onMounted, ref } from 'vue'
import { Chart, registerables } from 'chart.js'

const auditItems = [
  {
    title: '1. Мощность батареи по месяцам',
    text: 'Температура ячейки T (°C) ограничена [−10…+15]. Полная электрическая мощность трёх ячеек линейно от холодного минимума к тёплому максимуму:',
    formula: 'P_бат = 8 + (T + 10) · (12/25)  →  T=−10°C: 8 Вт; T=+15°C: 20 Вт',
  },
  {
    title: '2. Распределение: логика и передатчик',
    text: 'P_лог = 1 Вт. Мощность на входе П-контура с КПД η_PA = 0.9:',
    formula: 'P_нос = max(0, P_бат − P_лог) · η_PA',
  },
  {
    title: '3. Эквивалентная излучаемая мощность (короткая антенна СВ)',
    text: 'Совокупный коэффициент передачи в эфир η_ант = 0.22 (22%). Упрощённая степенная модель дальности (калибровка по ITU-R P.368):',
    formula: 'P_экв = P_нос · 0.22\nD_откр = 25 · √(P_экв) км\nD_лес = 0.38 · D_откр',
  },
]
Chart.register(...registerables)

const powerCanvasRef = ref(null)
const heatCanvasRef  = ref(null)

onMounted(() => {
  const months    = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
  const rawTemps  = [-12, -10, -6, -1, 5, 10, 14, 12, 8, 1, -4, -8]
  const temps     = rawTemps.map(t => Math.min(15, Math.max(-10, t)))

  const P_LOGIC  = 1.0
  const P_SLEEP  = 2.0
  const ETA_PA   = 0.9
  const ETA_ANT  = 0.22
  const K_RANGE  = 25
  const ALPHA    = 0.38

  const totalPower = temps.map(t => parseFloat((8 + (t + 10) * (12 / 25)).toFixed(2)))

  const radioPower = totalPower.map(p => {
    if (p < P_SLEEP) return 0
    return parseFloat(((p - P_LOGIC) * ETA_PA).toFixed(2))
  })

  const pEquiv     = radioPower.map(p => parseFloat((p * ETA_ANT).toFixed(3)))
  const rangeOpen  = pEquiv.map(pe => pe <= 0 ? 0 : parseFloat((K_RANGE * Math.sqrt(pe)).toFixed(1)))
  const rangeHilly = rangeOpen.map(d => parseFloat((d * ALPHA).toFixed(1)))
  const rangeMean  = rangeOpen.map((d, i) => parseFloat(((d + rangeHilly[i]) / 2).toFixed(1)))

  const chemHeat = [], elecHeat = [], totalHeat = []
  temps.forEach((t, i) => {
    const p     = totalPower[i]
    const I     = p / 3.6
    const qChem = parseFloat((p * 1.4).toFixed(2))
    const Rint  = 0.15 + ((15 - t) * 0.02)
    const qElec = parseFloat((I * I * Rint).toFixed(2))
    chemHeat.push(qChem)
    elecHeat.push(qElec)
    totalHeat.push(parseFloat((qChem + qElec).toFixed(2)))
  })

  // Power chart
  new Chart(powerCanvasRef.value.getContext('2d'), {
    type: 'bar',
    data: {
      labels: months,
      datasets: [
        { type: 'line', label: 'Мощность на антенну P_нос (Вт)',        data: radioPower, borderColor: '#2ecc71', backgroundColor: 'rgba(46,204,113,0.35)', fill: true,  tension: 0.4, borderWidth: 3, yAxisID: 'y' },
        { type: 'line', label: 'Дальность, открытая местность (км)',    data: rangeOpen,  borderColor: '#f1c40f', backgroundColor: 'transparent',             fill: false, tension: 0.4, borderWidth: 2.5, yAxisID: 'yRange' },
        { type: 'line', label: 'Дальность, лесисто-холмистая (км)',     data: rangeHilly, borderColor: '#e67e22', backgroundColor: 'transparent',             fill: false, tension: 0.4, borderWidth: 2, borderDash: [6,4], yAxisID: 'yRange' },
        { type: 'line', label: 'Дальность, средняя оценка (км)',        data: rangeMean,  borderColor: '#9b59b6', backgroundColor: 'transparent',             fill: false, tension: 0.4, borderWidth: 2, borderDash: [2,3], yAxisID: 'yRange' },
        { type: 'line', label: 'Температура ячейки (°C)',               data: temps,      borderColor: '#3498db', backgroundColor: 'transparent',             fill: false, tension: 0.4, borderWidth: 2, borderDash: [5,5], yAxisID: 'yTemp' },
      ],
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        title:  { display: true, text: 'Радиомощность (класс E) и дальность СВ (1219 кГц), заземление «звезда»', color: '#333', font: { size: 14 } },
        legend: { labels: { color: '#333', boxWidth: 12, font: { size: 10 } } },
      },
      scales: {
        x:      { ticks: { color: '#666' }, grid: { color: '#eee' } },
        y:      { type: 'linear', display: true, position: 'left',  title: { display: true, text: 'Мощность на антенну (Вт)', color: '#2ecc71' }, ticks: { color: '#666' }, grid: { color: '#eee' }, min: 0, max: 20 },
        yRange: { type: 'linear', display: true, position: 'right', title: { display: true, text: 'Дальность (км)',           color: '#f39c12' }, ticks: { color: '#666' }, grid: { drawOnChartArea: false }, min: 0, max: 55 },
        yTemp:  { type: 'linear', display: true, position: 'right', title: { display: true, text: 'Температура (°C)',         color: '#3498db' }, ticks: { color: '#3498db' }, grid: { drawOnChartArea: false }, min: -15, max: 20 },
      },
    },
  })

  // Heat chart
  new Chart(heatCanvasRef.value.getContext('2d'), {
    type: 'line',
    data: {
      labels: months,
      datasets: [
        { label: 'Суммарное тепло (Вт)',      data: totalHeat, borderColor: '#e74c3c', backgroundColor: 'rgba(231,76,60,0.2)',  fill: true,  tension: 0.4, borderWidth: 3, yAxisID: 'y' },
        { label: 'Химическое тепло (Вт)',     data: chemHeat,  borderColor: '#e67e22', backgroundColor: 'transparent',          fill: false, tension: 0.4, borderWidth: 2, borderDash: [5,5], yAxisID: 'y' },
        { label: 'Электрическое тепло (Вт)', data: elecHeat,  borderColor: '#9b59b6', backgroundColor: 'transparent',          fill: false, tension: 0.4, borderWidth: 2, borderDash: [2,2], yAxisID: 'y' },
        { label: 'Температура ячейки (°C)',  data: temps,     borderColor: '#3498db', backgroundColor: 'transparent',          fill: false, tension: 0.4, borderWidth: 2, borderDash: [5,5], yAxisID: 'yTemp' },
      ],
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        title:  { display: true, text: 'Тепловыделение (Q при P_бат 8…20 Вт по месяцам)', color: '#333', font: { size: 14 } },
        legend: { labels: { color: '#333' } },
      },
      scales: {
        x:     { ticks: { color: '#666' }, grid: { color: '#eee' } },
        y:     { type: 'linear', display: true, position: 'left',  title: { display: true, text: 'Тепло (Вт)',       color: '#e74c3c' }, ticks: { color: '#666' }, grid: { color: '#eee' }, min: 0 },
        yTemp: { type: 'linear', display: true, position: 'right', title: { display: true, text: 'Температура (°C)', color: '#3498db' }, ticks: { color: '#3498db' }, grid: { drawOnChartArea: false }, min: -15, max: 20 },
      },
    },
  })
})
</script>

<template>
  <section id="charts" class="section-card">
    <h2 class="section-heading">
      <span class="text-gray-500">6.</span>
      Графики мощности и тепловыделения
    </h2>

    <p class="text-gray-400 text-sm mb-6">
      Модель работы передатчика по месяцам на основе климатических данных аэропорта Мурманск (Мурмаши).
      Бочки закопаны под слой мха (20 см) и зимнего снега (до 2 м), температура внутри ограничена:
      не ниже −10°C зимой и не выше +15°C летом. Несущая <strong class="text-white">1219 кГц</strong>.
    </p>

    <h3 class="text-accent-blue font-semibold mb-3 text-base">
      Выдаваемая в эфир мощность и дальность
    </h3>
    <p class="text-gray-400 text-sm mb-4">
      Три ячейки с деполяризатором MnO₂, диапазон выработки <strong class="text-white">8–20 Вт</strong>,
      приоритет «мозгам» <strong class="text-white">до 1 Вт</strong>,
      усилитель класса E (П-контур), короткая L-антенна с водяным заземлением «звезда».
    </p>
    <div class="bg-white rounded-xl p-4 mb-8">
      <canvas ref="powerCanvasRef" height="100" />
    </div>

    <h3 class="text-accent-red font-semibold mb-3 text-base">
      Тепловыделение (Терморегуляция ячейки)
    </h3>
    <p class="text-gray-400 text-sm mb-4">
      Химическое тепло Q_хим ≈ 1.4·P_бат; электрическое Q_эл = I²R_внутр.
      Снижением эффективности из-за зашламления в пределах 15% пренебрегаем.
    </p>
    <div class="bg-white rounded-xl p-4 mb-6">
      <canvas ref="heatCanvasRef" height="100" />
    </div>

    <!-- Audit block -->
    <div class="highlight-box">
      <h3 class="text-accent-green font-bold mb-3 flex items-center gap-2">
        ✅ Аудит схемы и полный пересчёт (мощность, дальность)
      </h3>

      <p class="text-gray-300 text-sm mb-4">
        <strong class="text-white">Исходные допущения:</strong> три гальванические ячейки в бочках ПНД;
        MT3608 (5В для логики), Arduino Nano, DFPlayer Mini, MOSFET (LR7843/D4184), П-контур 100 мкГн + 2×1000 пФ;
        несущая вещания <strong class="text-white">1219 кГц</strong>; антенна — горизонтальное полотно с коротким спуском
        и <strong class="text-white">водяным заземлением «звезда»</strong>.
      </p>

      <div class="space-y-4 text-sm">
        <div v-for="item in auditItems" :key="item.title">
          <h4 class="text-accent-blue font-semibold mb-1">{{ item.title }}</h4>
          <p class="text-gray-300 leading-relaxed" v-html="item.text" />
          <div v-if="item.formula" class="formula-block mt-2">{{ item.formula }}</div>
        </div>
      </div>

      <div class="mt-4 pt-4 border-t border-white/10">
        <h4 class="text-gray-400 font-semibold mb-2 text-sm">Справочные материалы</h4>
        <ul class="text-xs text-gray-500 space-y-1">
          <li>ITU-R P.368 — расчёт интенсивности поля наземной волны.</li>
          <li>ITU-R P.833 — влияние растительности.</li>
          <li>Kraus, Marhefka, <em>Antennas for All Applications</em> — излучение коротких антенн, согласование.</li>
        </ul>
      </div>
    </div>

    <!-- Thermal balance block -->
    <div class="warning-box mt-6">
      <h4 class="text-accent-red font-bold mb-2 flex items-center gap-2">
        🌡️ Теплообмен: Не закипит ли бочка летом?
      </h4>
      <p class="text-sm text-gray-300 mb-3">
        Суммарное тепловыделение одной 65-литровой бочки на пике — <strong class="text-white">30–35 Вт</strong>.
        Может ли она перегреться в летнем грунте (+10...+15°C)?
        <strong class="text-accent-green">Нет, установится идеальный температурный баланс.</strong>
      </p>
      <ul class="text-sm text-gray-400 space-y-2">
        <li><strong class="text-white">Плотность теплового потока:</strong> ~35 Вт/м² (тело человека излучает 55 Вт/м²). Безопасно.</li>
        <li><strong class="text-white">Теплопроводность стенки:</strong> ПНД 3 мм даёт перепад всего ~0.3°C. Не препятствует отводу тепла.</li>
        <li><strong class="text-white">Рассеивание во влажный грунт:</strong> λ = 1.0–1.5 Вт/(м·°C). ΔT внутри = 7.5–11°C.</li>
      </ul>
      <p class="text-sm text-gray-300 mt-3">
        <strong class="text-white">Итог:</strong> При грунте +10°C равновесная температура внутри бочки — 
        <strong class="text-accent-green">+17.5...+21°C</strong>. Идеальная «комнатная» температура для максимальной ионной подвижности.
      </p>
    </div>
  </section>
</template>

