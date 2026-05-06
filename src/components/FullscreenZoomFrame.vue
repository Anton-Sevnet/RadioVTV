<script setup>
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue'

const props = defineProps({
  frameClass: { type: String, default: '' },
})

const rootRef    = ref(null)
const surfaceRef = ref(null)

const zoom      = ref(1)
const panX      = ref(0)
const panY      = ref(0)
const isFs      = ref(false)
const isDragging = ref(false)

const MIN_Z = 0.25
const MAX_Z = 5

// ── Pan clamping ──────────────────────────────────────────────────────────────
// Keeps surface inside the viewport; called after every zoom/pan change.
function clampPan(z, px, py) {
  const root    = rootRef.value
  const surface = surfaceRef.value
  if (!root) return { x: px, y: py }
  const rW = root.clientWidth
  const rH = root.clientHeight
  // Surface rendered size after zoom (actual CSS px, not virtual)
  const sW = surface ? surface.scrollWidth  : z * rW
  const sH = surface ? surface.scrollHeight : rH
  const minX = rW >= sW ? 0 : rW - sW
  const minY = rH >= sH ? 0 : rH - sH
  return {
    x: Math.min(0, Math.max(minX, px)),
    y: Math.min(0, Math.max(minY, py)),
  }
}

// ── Zoom engine ───────────────────────────────────────────────────────────────
// vpCx/vpCy — cursor/pinch-center in viewport pixels (relative to root).
// If omitted, zooms toward viewport center.
function setZoom(newZ, vpCx, vpCy) {
  const oldZ = zoom.value
  newZ = Math.min(MAX_Z, Math.max(MIN_Z, Math.round(newZ * 100) / 100))
  if (newZ === oldZ) return

  const root = rootRef.value
  const cx = vpCx !== undefined ? vpCx : (root ? root.clientWidth  / 2 : 0)
  const cy = vpCy !== undefined ? vpCy : (root ? root.clientHeight / 2 : 0)

  // Keep the content point under cursor fixed:
  // new_pan = cursor - (cursor - old_pan) * (new_zoom / old_zoom)
  const ratio  = newZ / oldZ
  const newPX  = cx - (cx - panX.value) * ratio
  const newPY  = cy - (cy - panY.value) * ratio

  zoom.value = newZ
  // Clamp after DOM update (surface has new width by then)
  nextTick(() => {
    const c = clampPan(newZ, newPX, newPY)
    panX.value = c.x
    panY.value = c.y
    // Let Chart.js ResizeObserver pick up the width change
    window.dispatchEvent(new Event('resize'))
  })
}

// ── Computed styles ───────────────────────────────────────────────────────────
// Normal mode  → no extra style (Tailwind block w-full handles it)
// Fullscreen   → position:absolute fills root; width changes give Chart.js
//               native-resolution redraws; translate handles panning (no scale!)
const surfaceStyle = computed(() => {
  if (!isFs.value) return {}
  return {
    position:        'absolute',
    top:             '0',
    left:            '0',
    width:           `${zoom.value * 100}%`,
    transform:       `translate(${panX.value}px, ${panY.value}px)`,
    transformOrigin: '0 0',
    willChange:      'transform',
    cursor:          zoom.value > 1.01
                       ? (isDragging.value ? 'grabbing' : 'grab')
                       : 'default',
    transition:      isDragging.value ? 'none' : 'transform 60ms linear',
  }
})

// ── Fullscreen toggle ─────────────────────────────────────────────────────────
function syncFsState() {
  const el = rootRef.value
  if (!el) return
  isFs.value = document.fullscreenElement === el || el.classList.contains('vtv-fs')
}

function resetView() {
  zoom.value = 1
  panX.value = 0
  panY.value = 0
}

// Auto-fit: zoom out if content is taller than viewport (common for SVG diagrams)
async function autoFit() {
  await new Promise(r => setTimeout(r, 120))
  const root    = rootRef.value
  const surface = surfaceRef.value
  if (!root || !surface) return
  const rW = root.clientWidth
  const rH = root.clientHeight
  const sW = surface.scrollWidth
  const sH = surface.scrollHeight
  if (sH > rH || sW > rW) {
    const fitZoom = Math.min(rW / sW, rH / sH)
    if (fitZoom < 1) {
      zoom.value = Math.round(fitZoom * 100) / 100
    }
  }
}

async function toggleFullscreen() {
  const el = rootRef.value
  if (!el) return

  if (isFs.value) {
    if (document.fullscreenElement) await document.exitFullscreen().catch(() => {})
    el.classList.remove('vtv-fs')
    document.body.style.overflow = ''
    resetView()
    syncFsState()
    await nextTick()
    window.dispatchEvent(new Event('resize'))
  } else {
    try {
      await el.requestFullscreen()
    } catch {
      el.classList.add('vtv-fs')
      document.body.style.overflow = 'hidden'
    }
    syncFsState()
    resetView()
    await nextTick()
    window.dispatchEvent(new Event('resize'))
    autoFit()
  }
}

function onFsChange() {
  const wasFs = isFs.value
  syncFsState()
  if (wasFs && !isFs.value) {
    resetView()
    document.body.style.overflow = ''
  }
  window.dispatchEvent(new Event('resize'))
}

function onKeydown(e) {
  if (e.key === 'Escape' && isFs.value && !document.fullscreenElement) {
    const el = rootRef.value
    if (el?.classList.contains('vtv-fs')) {
      el.classList.remove('vtv-fs')
      document.body.style.overflow = ''
      resetView()
      isFs.value = false
      window.dispatchEvent(new Event('resize'))
    }
  }
}

// ── Zoom buttons ──────────────────────────────────────────────────────────────
function zoomIn()    { setZoom(zoom.value * 1.25) }
function zoomOut()   { setZoom(zoom.value / 1.25) }
function zoomReset() {
  resetView()
  nextTick(() => window.dispatchEvent(new Event('resize')))
}

// ── Wheel zoom (toward cursor) ────────────────────────────────────────────────
function onWheel(e) {
  if (!isFs.value) return
  e.preventDefault()
  const rect   = rootRef.value?.getBoundingClientRect()
  const factor = e.deltaY > 0 ? 0.9 : 1.11
  const cx     = rect ? e.clientX - rect.left : undefined
  const cy     = rect ? e.clientY - rect.top  : undefined
  setZoom(zoom.value * factor, cx, cy)
}

// ── Mouse drag (pan) ──────────────────────────────────────────────────────────
const drag = { active: false, startX: 0, startY: 0, startPanX: 0, startPanY: 0 }

function onMouseDown(e) {
  if (!isFs.value || e.button !== 0) return
  if (e.target.closest('button, [role="button"]')) return
  drag.active    = true
  drag.startX    = e.clientX
  drag.startY    = e.clientY
  drag.startPanX = panX.value
  drag.startPanY = panY.value
  isDragging.value = true
  e.preventDefault()
}

function onMouseMove(e) {
  if (!drag.active) return
  const c = clampPan(
    zoom.value,
    drag.startPanX + e.clientX - drag.startX,
    drag.startPanY + e.clientY - drag.startY,
  )
  panX.value = c.x
  panY.value = c.y
}

function onMouseUp() {
  drag.active = false
  isDragging.value = false
}

// ── Touch: 1-finger drag + 2-finger pinch ────────────────────────────────────
let pinchDist0  = 0
let pinchZoom0  = 1
let pinchCx     = 0
let pinchCy     = 0

function touchDist(t0, t1) {
  return Math.hypot(t0.clientX - t1.clientX, t0.clientY - t1.clientY)
}

function onTouchStart(e) {
  if (!isFs.value) return
  if (e.touches.length === 2) {
    e.preventDefault()
    pinchDist0 = touchDist(e.touches[0], e.touches[1])
    pinchZoom0 = zoom.value
    const rect = rootRef.value?.getBoundingClientRect()
    if (rect) {
      pinchCx = ((e.touches[0].clientX + e.touches[1].clientX) / 2) - rect.left
      pinchCy = ((e.touches[0].clientY + e.touches[1].clientY) / 2) - rect.top
    }
  } else if (e.touches.length === 1) {
    drag.active    = true
    drag.startX    = e.touches[0].clientX
    drag.startY    = e.touches[0].clientY
    drag.startPanX = panX.value
    drag.startPanY = panY.value
    isDragging.value = true
  }
}

function onTouchMove(e) {
  if (!isFs.value) return
  e.preventDefault()
  if (e.touches.length === 2 && pinchDist0 > 0) {
    const newDist = touchDist(e.touches[0], e.touches[1])
    setZoom(pinchZoom0 * (newDist / pinchDist0), pinchCx, pinchCy)
  } else if (e.touches.length === 1 && drag.active) {
    const c = clampPan(
      zoom.value,
      drag.startPanX + e.touches[0].clientX - drag.startX,
      drag.startPanY + e.touches[0].clientY - drag.startY,
    )
    panX.value = c.x
    panY.value = c.y
  }
}

function onTouchEnd(e) {
  if (e.touches.length < 2)  pinchDist0 = 0
  if (e.touches.length === 0) { drag.active = false; isDragging.value = false }
}

// ── Lifecycle ─────────────────────────────────────────────────────────────────
let wheelEl = null

onMounted(async () => {
  document.addEventListener('fullscreenchange', onFsChange)
  document.addEventListener('keydown', onKeydown)
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup',   onMouseUp)
  await nextTick()
  wheelEl = rootRef.value
  wheelEl?.addEventListener('wheel',      onWheel,      { passive: false })
  wheelEl?.addEventListener('touchstart', onTouchStart, { passive: false })
  wheelEl?.addEventListener('touchmove',  onTouchMove,  { passive: false })
  wheelEl?.addEventListener('touchend',   onTouchEnd,   { passive: true })
})

onBeforeUnmount(() => {
  document.removeEventListener('fullscreenchange', onFsChange)
  document.removeEventListener('keydown', onKeydown)
  window.removeEventListener('mousemove', onMouseMove)
  window.removeEventListener('mouseup',   onMouseUp)
  wheelEl?.removeEventListener('wheel',      onWheel)
  wheelEl?.removeEventListener('touchstart', onTouchStart)
  wheelEl?.removeEventListener('touchmove',  onTouchMove)
  wheelEl?.removeEventListener('touchend',   onTouchEnd)
})
</script>

<template>
  <div
    ref="rootRef"
    class="relative"
    :class="frameClass"
    @mousedown="onMouseDown"
  >
    <!-- Fullscreen toggle button -->
    <button
      type="button"
      @click.stop="toggleFullscreen"
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

    <!-- Zoom controls — visible only in fullscreen -->
    <div
      v-show="isFs"
      class="absolute top-12 right-2 z-50 flex flex-col gap-1 pointer-events-auto select-none"
      role="toolbar"
      aria-label="Масштаб"
    >
      <button
        type="button"
        class="w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 border border-white/25 text-white text-lg font-semibold leading-none backdrop-blur-sm"
        title="Приблизить (+)"
        @click.stop="zoomIn"
      >+</button>
      <button
        type="button"
        class="w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 border border-white/25 text-white text-lg font-semibold leading-none backdrop-blur-sm"
        title="Отдалить (−)"
        @click.stop="zoomOut"
      >−</button>
      <button
        type="button"
        class="w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 border border-white/25 text-white text-xs font-medium backdrop-blur-sm"
        title="Сбросить масштаб"
        @click.stop="zoomReset"
      >1:1</button>
      <span class="text-center text-white text-xs font-mono bg-black/40 border border-white/25 rounded px-0.5 py-0.5 tabular-nums leading-none">
        {{ Math.round(zoom * 100) }}%
      </span>
    </div>

    <!-- Pan / zoom surface:
         Normal mode  → block w-full  (fills container, Chart.js responsive works)
         Fullscreen   → position:absolute + width:zoom*100% (real resize, not CSS scale!)
                        + translate for pan                                        -->
    <div
      ref="surfaceRef"
      class="vtv-zoom-surface"
      :class="isFs ? '' : 'block w-full'"
      :style="surfaceStyle"
    >
      <slot />
    </div>
  </div>
</template>
