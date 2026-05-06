<script setup>
import { ref, onMounted, nextTick } from 'vue'
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

/** Только из сборки: задайте в GitHub Actions секрет VITE_RECAPTCHA_SITE_KEY (reCAPTCHA v2 «флажок»). */
const RECAPTCHA_SITE_KEY =
  typeof import.meta.env.VITE_RECAPTCHA_SITE_KEY === 'string'
    ? import.meta.env.VITE_RECAPTCHA_SITE_KEY.trim()
    : ''

const recaptchaEnabled = RECAPTCHA_SITE_KEY.length >= 30

const recaptchaContainer = ref(null)
const recaptchaShowPanel = ref(true)
const recaptchaRendered = ref(false)

function debugLog(runId, hypothesisId, location, message, data) {
  // #region agent log
  fetch('http://127.0.0.1:7277/ingest/cc94e87f-d223-4e50-b5ea-9ad945c95ad9', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Debug-Session-Id': '5cc65f' },
    body: JSON.stringify({
      sessionId: '5cc65f',
      runId,
      hypothesisId,
      location,
      message,
      data,
      timestamp: Date.now(),
    }),
  }).catch(() => {})
  // #endregion
}

function renderRecaptchaWidget(runId) {
  if (!window.grecaptcha || !recaptchaContainer.value || recaptchaRendered.value) return

  try {
    debugLog(runId, 'H2', 'App.vue:renderRecaptchaWidget', 'recaptcha_before_render', {
      offsetWidth: recaptchaContainer.value?.offsetWidth,
      offsetHeight: recaptchaContainer.value?.offsetHeight,
    })

    const id = window.grecaptcha.render(recaptchaContainer.value, {
      sitekey: RECAPTCHA_SITE_KEY,
      theme: 'dark',
      size: 'normal',
    })

    recaptchaRendered.value = true
    debugLog(runId, 'H2', 'App.vue:renderRecaptchaWidget', 'recaptcha_render_ok', {
      widgetId: id,
      siteKeyPrefix: RECAPTCHA_SITE_KEY.slice(0, 8),
    })
  } catch (err) {
    recaptchaShowPanel.value = false
    debugLog(runId, 'H2', 'App.vue:renderRecaptchaWidget', 'recaptcha_render_throw', {
      name: err?.name,
      message: err?.message,
    })
  }
}

function bootRecaptcha(runId) {
  debugLog(runId, 'H1', 'App.vue:bootRecaptcha', 'recaptcha_boot', {
    host: window.location.host,
    hostname: window.location.hostname,
    protocol: window.location.protocol,
    path: window.location.pathname,
    siteKeyPrefix: RECAPTCHA_SITE_KEY.slice(0, 8),
    hasGrecaptcha: Boolean(window.grecaptcha),
  })

  const startRender = () => {
    if (typeof window.grecaptcha.ready === 'function') {
      window.grecaptcha.ready(() => renderRecaptchaWidget(runId))
    } else {
      renderRecaptchaWidget(runId)
    }
  }

  if (window.grecaptcha) {
    startRender()
    return
  }

  const existing = document.querySelector('script[data-radio-vtv-recaptcha="1"]')
  if (existing) {
    existing.addEventListener('load', startRender, { once: true })
    return
  }

  const script = document.createElement('script')
  script.dataset.radioVtvRecaptcha = '1'
  script.src = 'https://www.google.com/recaptcha/api.js?render=explicit&hl=ru'
  script.async = true
  script.defer = true
  script.onload = startRender
  script.onerror = () => {
    recaptchaShowPanel.value = false
    debugLog(runId, 'H4', 'App.vue:bootRecaptcha', 'recaptcha_script_error', { src: script.src })
  }
  document.head.appendChild(script)
}

onMounted(() => {
  const runId = `page-${Date.now()}`
  if (!recaptchaEnabled) return
  void nextTick(() => {
    bootRecaptcha(runId)
  })
})
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

        <p
          v-if="!recaptchaEnabled"
          class="text-gray-600 text-xs max-w-md leading-relaxed m-0"
        >
          Антиспам: включите виджет, добавив в GitHub секрет Actions
          <span class="text-gray-400"> VITE_RECAPTCHA_SITE_KEY</span>
          — это Site Key вида «флажок» reCAPTCHA v2, с доменами
          <span class="text-gray-400">alttechno.ru</span> и при необходимости
          <span class="text-gray-400">www.alttechno.ru</span>.
        </p>

        <div
          v-if="recaptchaEnabled && recaptchaShowPanel"
          class="w-full max-w-md rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-5"
        >
          <p class="text-gray-500 text-xs mb-4 m-0 leading-relaxed">
            Подключена reCAPTCHA v2 («флажок»): домены вы настраиваете в
            <a
              href="https://www.google.com/recaptcha/admin/create"
              class="text-[#229ED9] underline decoration-[#229ED9]/40 hover:decoration-[#229ED9]"
              target="_blank"
              rel="noopener noreferrer"
            >
              консоли Google</a>.
            Если раньше был «ошибка ключа» — чаще всего ключ не того типа (нужна v2) или в доменах нет
            <span class="text-gray-400">alttechno.ru</span> /
            <span class="text-gray-400">www.alttechno.ru</span>.
            Ключ в сборке задаётся секретом
            <span class="text-gray-400">VITE_RECAPTCHA_SITE_KEY</span>.
          </p>
          <div
            ref="recaptchaContainer"
            class="flex justify-center mx-auto w-full min-h-[78px] min-w-[302px]"
          />
        </div>

        <p class="text-gray-600 text-xs m-0">
          Радиостанция «Дыхание ВТВ» · 1219 кГц · Кольский полуостров · Заполярье
        </p>
      </div>
    </footer>
  </div>
</template>
