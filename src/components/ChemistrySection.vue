<template>
  <section id="chemistry" class="section-card border-l-4 border-accent-red">
    <h2 class="section-heading">
      <span class="text-accent-red">5.</span>
      Химические реакции и «Зашламление»
    </h2>

    <p class="text-gray-300 mb-6">
      Ниже приведены процессы, происходящие внутри 3-х бочек с магний-графитовыми ячейками
      (с деполяризатором MnO₂).
    </p>

    <div class="grid md:grid-cols-2 gap-6">
      <!-- Chemistry card -->
      <div class="bg-blue-950/30 border border-accent-blue/20 rounded-xl p-5">
        <h3 class="text-accent-red font-bold mb-4 flex items-center gap-2">
          🔋 Химия процесса
        </h3>

        <div class="space-y-4 text-sm text-gray-300">
          <div>
            <div class="font-semibold text-white mb-1">1. На аноде (Растворение магния):</div>
            <code class="formula-block block">Mg → Mg²⁺ + 2e⁻</code>
          </div>
          <div>
            <div class="font-semibold text-white mb-1">2. На катоде (Восстановление воды):</div>
            <code class="formula-block block">2H₂O + 2e⁻ → H₂ + 2OH⁻</code>
          </div>
          <div>
            <div class="font-semibold text-white mb-1">3. Деполяризация (внутри куклы):</div>
            <p class="text-gray-400 text-xs mb-1">
              Пиролюзит (MnO₂) окисляет газообразный водород, не давая ему изолировать графит:
            </p>
            <code class="formula-block block">H₂ + 2MnO₂ → 2MnO(OH)</code>
          </div>
          <div class="pt-3 border-t border-white/10">
            <div class="font-semibold text-white mb-1">Итоговая реакция:</div>
            <code class="formula-block block text-accent-green">
              Mg + 2H₂O + 2MnO₂ → Mg(OH)₂↓ + 2MnO(OH)↓ + Q
            </code>
          </div>
        </div>
      </div>

      <!-- Sludge card -->
      <div class="bg-red-950/30 border border-accent-red/20 rounded-xl p-5">
        <h3 class="text-accent-orange font-bold mb-4 flex items-center gap-2">
          ⚠️ Проблема «Зашламления» (14 месяцев)
        </h3>

        <div class="space-y-3 text-sm text-gray-300">
          <p>
            Продукты реакции — гидроксид магния <code>Mg(OH)₂</code> (белый осадок) и манганит
            <code>MnO(OH)</code> — нерастворимы.
          </p>
          <p>
            Поскольку реакция деполяризации происходит прямо в мешочке «куклы», поры пиролюзита
            и ткань <strong class="text-white">постепенно забиваются (зашламляются)</strong>
            этими твёрдыми осадками.
          </p>
          <div class="warning-box mt-3">
            <div class="font-bold text-accent-red mb-1">Интервал обслуживания:</div>
            <div class="text-2xl font-bold font-mono text-accent-red">≤ 14 месяцев</div>
            <p class="text-xs mt-1 text-red-300">
              Извлечь куклы, механически счистить шлам, заменить мешки с засыпкой.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
