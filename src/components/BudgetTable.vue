<template>
  <section id="budget" class="section-card">
    <h2 class="section-heading">
      <span class="text-gray-500">10.</span>
      Смета: Готовые модули и электроника
    </h2>

    <p class="text-gray-400 mb-6 text-sm">
      Все модули максимально популярны, продаются везде (Ozon, Wildberries, AliExpress, Чип и Дип).
    </p>

    <div class="space-y-6">
      <div v-for="section in budgetSections" :key="section.title">
        <h3 :class="['text-sm font-bold mb-3 px-2 py-1.5 bg-white/[0.04] rounded-lg inline-block', section.color]">
          {{ section.title }}
        </h3>
        <div class="overflow-x-auto rounded-xl border border-white/10">
          <table class="data-table">
            <thead>
              <tr>
                <th class="min-w-[200px]">Наименование</th>
                <th class="min-w-[100px]">Кол-во</th>
                <th class="min-w-[140px]">Цена</th>
                <th>Где купить / Назначение</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in section.items" :key="item.name">
                <td class="font-medium text-white">{{ item.name }}</td>
                <td class="text-gray-400">{{ item.qty }}</td>
                <td class="font-mono text-accent-amber">{{ item.price }}</td>
                <td class="text-gray-400 text-xs">
                  <a v-if="item.url" :href="item.url" target="_blank" rel="noopener" class="text-accent-blue hover:text-blue-300">
                    {{ item.note }}
                  </a>
                  <span v-else>{{ item.note }}</span>
                </td>
              </tr>
              <tr class="subtotal-row">
                <td colspan="2" class="text-right text-gray-300">Подытог:</td>
                <td colspan="2" class="font-mono text-accent-amber font-bold">{{ section.subtotal }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Total -->
      <div class="bg-accent-amber/10 border border-accent-amber/30 rounded-xl p-4 flex justify-between items-center">
        <span class="text-white font-bold">
          ИТОГО (все части):
        </span>
        <span class="text-accent-amber font-bold text-xl font-mono">{{ budgetTotal }}</span>
      </div>
    </div>
  </section>
</template>

<script setup>
import { BUDGET_SECTIONS, BUDGET_TOTAL } from '../constants/budget.js'
const budgetSections = BUDGET_SECTIONS
const budgetTotal = BUDGET_TOTAL
</script>
