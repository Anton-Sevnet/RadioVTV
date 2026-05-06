<script setup>
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue'

defineProps({
  frameClass: { type: String, default: '' },
})

const USE_CSS_ZOOM = typeof CSS !== 'undefined' && CSS.supports?.('zoom', '1')

const rootRef = ref(null)
const zoom = ref(1)
const isFs = ref(false)

const surfaceStyle = computed(() => {
  if (!isFs.value) return {}
  if (USE_CSS_ZOOM) return { zoom: zoom.value }
  return {
    transform: `scale(${zoom.value})`,
    transformOrigin: 'center center',
  }
})

const MIN_Z = 0.5
const MAX_Z = 4

function getRoot() {
  return rootRef.value
}

function syncFsState() {
  const el = getRoot()
  if (!el) return
  isFs.value = document.fullscreenElement === el || el.classList.contains('vtv-fs')
}

function activeFs() {
  const el = getRoot()
  if (!el) return false
  return document.fullscreenElement === el || el.classList.contains('vtv-fs')
}

async function toggleFullscreen() {
  const el = getRoot()
  if (!el) return

  if (isFs.value) {
    if (document.fullscreenElement) {
      await document.exitFullscreen().catch(() => {})
    }
    el.classList.remove('vtv-fs')
    document.body.style.overflow = ''
    zoom.value = 1
    syncFsState()
    window.dispatchEvent(new Event('resize'))
  } else {
    try {
      await el.requestFullscreen()
    } catch {
      el.classList.add('vtv-fs')
      document.body.style.overflow = 'hidden'
    }
    if (document.fullscreenElement !== el) {
      el.classList.add('vtv-fs')
      document.body.style.overflow = 'hidden'
    }
    syncFsState()
    window.dispatchEvent(new Event('resize'))
  }
}

function zoomIn() {
  zoom.value = Math.min(MAX_Z, Math.round(zoom.value * 1.15 * 100) / 100)
}

function zoomOut() {
  zoom.value = Math.max(MIN_Z, Math.round(zoom.value / 1.15 * 100) / 100)
}

function zoomReset() {
  zoom.value = 1
}

function onWheel(e) {
  if (!activeFs()) return
  e.preventDefault()
  const factor = e.deltaY > 0 ? 0.92 : 1.08
  zoom.value = Math.min(MAX_Z, Math.max(MIN_Z, Math.round(zoom.value * factor * 100) / 100))
}

let pinchStartDist = 0
let pinchStartZoom = 1

function touchDistance(t0, t1) {
  const dx = t0.clientX - t1.clientX
  const dy = t0.clientY - t1.clientY
  return Math.hypot(dx, dy)
}

function onTouchStart(e) {
  if (!activeFs() || e.touches.length !== 2) return
  pinchStartDist = touchDistance(e.touches[0], e.touches[1])
  pinchStartZoom = zoom.value
}

function onTouchMove(e) {
  if (!activeFs() || e.touches.length !== 2) return
  e.preventDefault()
  const d = touchDistance(e.touches[0], e.touches[1])
  if (pinchStartDist > 0) {
    const z = pinchStartZoom * (d / pinchStartDist)
    zoom.value = Math.min(MAX_Z, Math.max(MIN_Z, Math.round(z * 100) / 100))
  }
}

function onTouchEnd(e) {
  if (e.touches.length < 2) pinchStartDist = 0
}

function onFsChange() {
  const wasFs = isFs.value
  syncFsState()
  if (wasFs && !isFs.value) {
    zoom.value = 1
    document.body.style.overflow = ''
  }
  window.dispatchEvent(new Event('resize'))
}

function onKeydown(e) {
  if (e.key === 'Escape' && isFs.value && !document.fullscreenElement) {
    const el = getRoot()
    if (el?.classList.contains('vtv-fs')) {
      el.classList.remove('vtv-fs')
      document.body.style.overflow = ''
      zoom.value = 1
      isFs.value = false
      window.dispatchEvent(new Event('resize'))
    }
  }
}

let wheelEl = null

onMounted(async () => {
  document.addEventListener('fullscreenchange', onFsChange)
  document.addEventListener('keydown', onKeydown)
  await nextTick()
  wheelEl = getRoot()
  wheelEl?.addEventListener('wheel', onWheel, { passive: false })
  wheelEl?.addEventListener('touchstart', onTouchStart, { passive: true })
  wheelEl?.addEventListener('touchmove', onTouchMove, { passive: false })
  wheelEl?.addEventListener('touchend', onTouchEnd, { passive: true })
})

onBeforeUnmount(() => {
  document.removeEventListener('fullscreenchange', onFsChange)
  document.removeEventListener('keydown', onKeydown)
  wheelEl?.removeEventListener('wheel', onWheel)
  wheelEl?.removeEventListener('touchstart', onTouchStart)
  wheelEl?.removeEventListener('touchmove', onTouchMove)
  wheelEl?.removeEventListener('touchend', onTouchEnd)
})
</script>

<template>
  <div ref="rootRef" class="relative" :class="frameClass">
    <button
      type="button"
      @click="toggleFullscreen"
      :title="isFs ? 'Выйти из полного экрана (Esc)' : 'На весь экран'"
      class="absolute top-2 right-2 z-50 flex items-center justify-center w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 active:scale-95 transition-all border border-white/25 backdrop-blur-sm pointer-events-auto"
      aria-label="Переключить полный экран"
    >
      <svg v-if="!isFs" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 9V3h6M3 15v6h6M21 9V3h-6M21 15v6h-6" />
      </svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 3v6H3M9 21v-6H3M15 3v6h6M15 21v-6h6" />
      </svg>
    </button>

    <div
      v-show="isFs"
      class="absolute top-12 right-2 z-50 flex flex-col gap-1 pointer-events-auto"
      role="toolbar"
      aria-label="Масштаб в полноэкранном режиме"
    >
      <button
        type="button"
        class="w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 border border-white/25 text-white text-lg font-semibold leading-none backdrop-blur-sm"
        title="Приблизить"
        aria-label="Приблизить"
        @click="zoomIn"
      >
        +
      </button>
      <button
        type="button"
        class="w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 border border-white/25 text-white text-lg font-semibold leading-none backdrop-blur-sm"
        title="Отдалить"
        aria-label="Отдалить"
        @click="zoomOut"
      >
        −
      </button>
      <button
        type="button"
        class="w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 border border-white/25 text-white text-xs font-medium backdrop-blur-sm px-0.5"
        title="Сброс масштаба"
        aria-label="Сброс масштаба"
        @click="zoomReset"
      >
        1:1
      </button>
    </div>

    <div
      class="vtv-zoom-surface inline-block will-change-transform transition-[transform] duration-75"
      :style="surfaceStyle"
    >
      <slot />
    </div>
  </div>
</template>
