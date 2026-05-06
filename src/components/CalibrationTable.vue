<template>
  <section id="calibration" class="section-card border-l-4 border-accent-amber">
    <h2 class="section-heading">
      <span class="text-accent-amber">10.1</span>
      Смета: Приборы для пуско-наладки (подстройка 1219 кГц)
    </h2>

    <p class="text-gray-400 mb-6 text-sm">
      Отдельно от основной сметы — то, что удобно на время пусконаладки. Часть можно одолжить у знакомых или взять в аренду.
    </p>

    <div class="overflow-x-auto rounded-xl border border-white/10">
      <table class="data-table">
        <thead>
          <tr>
            <th class="min-w-[220px]">Позиция</th>
            <th class="min-w-[80px]">Кол-во</th>
            <th class="min-w-[140px]">Цена</th>
            <th>Зачем на 1219 кГц</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.name">
            <td class="font-medium text-white">{{ item.name }}</td>
            <td class="text-gray-400">{{ item.qty }}</td>
            <td class="font-mono text-accent-amber">{{ item.price }}</td>
            <td class="text-gray-400 text-xs">{{ item.note }}</td>
          </tr>
          <tr class="subtotal-row">
            <td colspan="2" class="text-right text-gray-300">Подытог (если брать всё новым):</td>
            <td colspan="2" class="font-mono text-accent-amber font-bold">{{ subtotal }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="text-gray-500 text-xs mt-3">
      Аренда/одолжить: SDR, осциллограф и частотомер часто проще временно взять у радиолюбителей;
      приёмник СВ полезен оставить как эталонный контроль эфира.
    </p>
  </section>
</template>

<script setup>
import { CALIBRATION_ITEMS, CALIBRATION_SUBTOTAL } from '../constants/budget.js'
const items = CALIBRATION_ITEMS
const subtotal = CALIBRATION_SUBTOTAL
</script>
