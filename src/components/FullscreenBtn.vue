<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  targetRef: { type: Object, default: null },
})

const isFs = ref(false)

function getEl() {
  return props.targetRef?.value ?? null
}

async function toggle() {
  const el = getEl()
  if (!el) return

  if (isFs.value) {
    if (document.fullscreenElement) {
      await document.exitFullscreen().catch(() => {})
    } else {
      el.classList.remove('vtv-fs')
      document.body.style.overflow = ''
      isFs.value = false
      window.dispatchEvent(new Event('resize'))
    }
  } else {
    try {
      await el.requestFullscreen()
    } catch {
      // CSS fallback for iOS Safari (requestFullscreen not supported on divs)
      el.classList.add('vtv-fs')
      document.body.style.overflow = 'hidden'
      isFs.value = true
      window.dispatchEvent(new Event('resize'))
    }
  }
}

function onFsChange() {
  isFs.value = !!document.fullscreenElement
  window.dispatchEvent(new Event('resize'))
}

function onKeydown(e) {
  if (e.key === 'Escape' && isFs.value && !document.fullscreenElement) {
    const el = getEl()
    if (el) {
      el.classList.remove('vtv-fs')
      document.body.style.overflow = ''
      isFs.value = false
      window.dispatchEvent(new Event('resize'))
    }
  }
}

onMounted(() => {
  document.addEventListener('fullscreenchange', onFsChange)
  document.addEventListener('keydown', onKeydown)
})

onBeforeUnmount(() => {
  document.removeEventListener('fullscreenchange', onFsChange)
  document.removeEventListener('keydown', onKeydown)
})
</script>

<template>
  <button
    type="button"
    @click.stop="toggle"
    :title="isFs ? 'Выйти из полного экрана (Esc)' : 'На весь экран'"
    class="absolute top-2 right-2 z-20 flex items-center justify-center w-9 h-9 rounded-lg bg-black/40 hover:bg-black/65 active:scale-95 transition-all border border-white/25 backdrop-blur-sm"
    aria-label="Переключить полный экран"
  >
    <!-- Expand: 4 угловые скобки наружу -->
    <svg v-if="!isFs" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3 9V3h6M3 15v6h6M21 9V3h-6M21 15v6h-6"/>
    </svg>
    <!-- Collapse: 4 угловые скобки внутрь -->
    <svg v-else xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9 3v6H3M9 21v-6H3M15 3v6h6M15 21v-6h6"/>
    </svg>
  </button>
</template>
