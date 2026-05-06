<script setup>
import { ref, onMounted } from 'vue'
import NavBar            from './components/NavBar.vue'
import HeroSection       from './components/HeroSection.vue'
import OverviewSection   from './components/OverviewSection.vue'
import PhilosophySection from './components/PhilosophySection.vue'
import MnO2Section       from './components/MnO2Section.vue'
import UndergroundSection from './components/UndergroundSection.vue'
import BarrelDiagram     from './components/BarrelDiagram.vue'
import ChemistrySection  from './components/ChemistrySection.vue'
import PowerCharts       from './components/PowerCharts.vue'
import BlockDiagram      from './components/BlockDiagram.vue'
import AssemblyGuide     from './components/AssemblyGuide.vue'
import AntennaScene      from './components/AntennaScene.vue'
import HousingSection    from './components/HousingSection.vue'
import BudgetTable       from './components/BudgetTable.vue'
import CalibrationTable  from './components/CalibrationTable.vue'
import ReceiversSection  from './components/ReceiversSection.vue'
import AudioSection      from './components/AudioSection.vue'

const showLink = ref(false)
const recaptchaContainerTop = ref(null)
const recaptchaContainerBottom = ref(null)
const tgLink = ref('')

onMounted(() => {
  const script = document.createElement('script')
  script.src = 'https://www.google.com/recaptcha/api.js?render=explicit'
  script.async = true
  script.defer = true
  script.onload = () => {
    if (window.grecaptcha) {
      const renderWidget = (el) => {
        if (!el) return
        window.grecaptcha.render(el, {
          sitekey: '6LcE-dssAAAAADXr3BTVYE3EYvfrR5-uGp6wIyaq',
          theme: 'dark',
          callback: (response) => {
            if (response) {
              showLink.value = true
              tgLink.value = 'https://' + ['t', 'm', 'e'].join('.') + '/' + ['s', 'e', 'v', 'n', 'e', 't'].join('')
            }
          }
        })
      }
      renderWidget(recaptchaContainerTop.value)
      renderWidget(recaptchaContainerBottom.value)
    }
  }
  document.head.appendChild(script)
})
</script>

<template>
  <div class="min-h-screen bg-night">
    <NavBar />

    <HeroSection />

    <div class="max-w-6xl mx-auto px-4 pt-4 flex justify-end">
      <div v-show="!showLink" ref="recaptchaContainerTop" class="scale-75 origin-right opacity-30 hover:opacity-100 transition-opacity"></div>
      <a
        v-if="showLink"
        :href="tgLink"
        target="_blank"
        rel="noopener"
        class="text-gray-500 hover:text-[#229ED9] text-sm transition-colors"
      >
        Связь с автором: @sevnet
      </a>
    </div>

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

    <footer class="max-w-6xl mx-auto px-4 py-10 mt-4 border-t border-white/10 text-center">
      <div class="flex flex-col items-center gap-4">
        <div v-show="!showLink" ref="recaptchaContainerBottom" class="my-2 min-h-[78px]"></div>
        <a
          v-if="showLink"
          :href="tgLink"
          target="_blank"
          rel="noopener"
          class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full bg-[#229ED9]/15 border border-[#229ED9]/30 text-[#229ED9] hover:bg-[#229ED9]/25 hover:border-[#229ED9]/60 transition-all no-underline font-medium text-sm"
        >
          <svg class="w-5 h-5 shrink-0" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.248-1.97 9.289c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.12L7.19 13.367l-2.97-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.537-.194 1.006.131.636.219z"/>
          </svg>
          Связь: @sevnet
        </a>
        <p class="text-gray-600 text-xs">
          Радиостанция «Дыхание ВТВ» · 1219 кГц · Кольский полуостров · Заполярье
        </p>
      </div>
    </footer>
  </div>
</template>
