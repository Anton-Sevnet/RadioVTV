<template>
  <section id="assembly" class="section-card border-l-4 border-accent-green">
    <h2 class="section-heading">
      <span class="text-accent-green">8.</span>
      Практическое руководство: Сборка шаг за шагом
    </h2>

    <div class="space-y-4">
      <div
        v-for="step in steps"
        :key="step.num"
        :class="['step-card', step.color || 'border-accent-green']"
      >
        <h4 :class="['font-bold mb-3 flex items-center gap-2', step.titleColor || 'text-accent-green']">
          <span class="bg-accent-green/20 text-accent-green rounded-full w-6 h-6 flex items-center justify-center text-xs font-mono shrink-0">
            {{ step.num }}
          </span>
          {{ step.title }}
        </h4>
        <div v-if="step.warning" class="warning-box text-sm mb-3">
          ⚠️ {{ step.warning }}
        </div>
        <div class="text-gray-300 text-sm leading-relaxed" v-html="step.content" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ASSEMBLY_STEPS } from '../constants/assembly.js'
const steps = ASSEMBLY_STEPS
</script>
