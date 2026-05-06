<script setup>
import NavBar               from './components/NavBar.vue'
import HeroSection          from './components/HeroSection.vue'
import TelegramAuthorCta    from './components/TelegramAuthorCta.vue'
import OverviewSection      from './components/OverviewSection.vue'
import PhilosophySection    from './components/PhilosophySection.vue'
import MnO2Section          from './components/MnO2Section.vue'
import UndergroundSection   from './components/UndergroundSection.vue'
import BarrelDiagram        from './components/BarrelDiagram.vue'
import ChemistrySection     from './components/ChemistrySection.vue'
import PowerCharts          from './components/PowerCharts.vue'
import BlockDiagram         from './components/BlockDiagram.vue'
import AssemblyGuide        from './components/AssemblyGuide.vue'
import AntennaScene         from './components/AntennaScene.vue'
import HousingSection       from './components/HousingSection.vue'
import BudgetTable          from './components/BudgetTable.vue'
import CalibrationTable     from './components/CalibrationTable.vue'
import ReceiversSection     from './components/ReceiversSection.vue'
import AudioSection         from './components/AudioSection.vue'
</script>

<template>
  <div class="min-h-screen bg-night">
    <NavBar />

    <HeroSection />

    <main class="max-w-6xl mx-auto px-4 py-6 space-y-0">
      <OverviewSection />
      <PhilosophySection />
      <MnO2Section />
      <UndergroundSection />
      <BarrelDiagram />
      <ChemistrySection />
      <PowerCharts />
      <BlockDiagram />
      <AssemblyGuide />
      <AntennaScene />
      <HousingSection />
      <BudgetTable />
      <CalibrationTable />
      <ReceiversSection />
      <AudioSection />
    </main>

    <footer class="max-w-6xl mx-auto px-4 py-10 mt-4 border-t border-white/10">
      <div class="flex flex-col items-center gap-6 text-center">
        <TelegramAuthorCta variant="footer" />

        <p class="text-gray-600 text-xs m-0">
          Радиостанция «Дыхание ВТВ» · 1219 кГц · Кольский полуостров · Заполярье
        </p>
      </div>
    </footer>
  </div>
</template>
