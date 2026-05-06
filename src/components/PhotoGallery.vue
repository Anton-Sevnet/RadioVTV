<script setup>
import { ref, watch, onMounted, onBeforeUnmount, computed } from 'vue'

const props = defineProps({
  modelValue: { type: Number, default: null }, // null = закрыто, иначе индекс текущего фото
  images: { type: Array, required: true },
})
const emit = defineEmits(['update:modelValue'])

const scale  = ref(1)
const imgEl  = ref(null)

const isOpen  = computed(() => props.modelValue !== null)
const current = computed(() => props.modelValue ?? 0)
const total   = computed(() => props.images.length)

function close() { emit('update:modelValue', null) }

function go(dir) {
  scale.value = 1
  const next = ((current.value + dir) % total.value + total.value) % total.value
  // #region agent log
  fetch('http://127.0.0.1:7277/ingest/cc94e87f-d223-4e50-b5ea-9ad945c95ad9',{method:'POST',headers:{'Content-Type':'application/json','X-Debug-Session-Id':'c5ae93'},body:JSON.stringify({sessionId:'c5ae93',location:'PhotoGallery.vue:go',message:'go() called',data:{dir,current:current.value,next,total:total.value},hypothesisId:'H-C',timestamp:Date.now()})}).catch(()=>{})
  // #endregion
  emit('update:modelValue', next)
}

function resetZoom() { scale.value = 1 }

function onWheel(e) {
  // #region agent log
  fetch('http://127.0.0.1:7277/ingest/cc94e87f-d223-4e50-b5ea-9ad945c95ad9',{method:'POST',headers:{'Content-Type':'application/json','X-Debug-Session-Id':'c5ae93'},body:JSON.stringify({sessionId:'c5ae93',location:'PhotoGallery.vue:onWheel',message:'wheel event fired',data:{deltaY:e.deltaY,ctrlKey:e.ctrlKey,target:e.target?.tagName,currentIdx:current.value},hypothesisId:'H-A',timestamp:Date.now()})}).catch(()=>{})
  // #endregion
  e.preventDefault()
  if (e.ctrlKey) {
    const delta = e.deltaY < 0 ? 1.12 : 0.89
    scale.value = Math.min(8, Math.max(0.3, scale.value * delta))
  } else {
    go(e.deltaY > 0 ? 1 : -1)
  }
}

function onKey(e) {
  if (!isOpen.value) return
  if (e.key === 'Escape')      close()
  else if (e.key === 'ArrowLeft')  go(-1)
  else if (e.key === 'ArrowRight') go(1)
}

// Touch-свайп
let touchX = null
function onTouchStart(e) { touchX = e.touches[0].clientX }
function onTouchEnd(e) {
  if (touchX === null) return
  const dx = e.changedTouches[0].clientX - touchX
  if (Math.abs(dx) > 40) go(dx < 0 ? 1 : -1)
  touchX = null
}

// Сброс зума при смене фото
watch(() => props.modelValue, (newVal) => {
  scale.value = 1
  // #region agent log
  fetch('http://127.0.0.1:7277/ingest/cc94e87f-d223-4e50-b5ea-9ad945c95ad9',{method:'POST',headers:{'Content-Type':'application/json','X-Debug-Session-Id':'c5ae93'},body:JSON.stringify({sessionId:'c5ae93',location:'PhotoGallery.vue:watch(modelValue)',message:'modelValue changed',data:{newVal,newSrc:props.images[newVal ?? 0]?.src},hypothesisId:'H-D',timestamp:Date.now()})}).catch(()=>{})
  // #endregion
})

// Блокировка прокрутки страницы когда галерея открыта
watch(isOpen, (v) => { document.body.style.overflow = v ? 'hidden' : '' })

onMounted(() => window.addEventListener('keydown', onKey))
onBeforeUnmount(() => {
  window.removeEventListener('keydown', onKey)
  document.body.style.overflow = ''
})
</script>

<template>
  <Teleport to="body">
    <Transition name="gm-fade">
      <div
        v-if="isOpen"
        class="fixed inset-0 z-[9000] flex items-center justify-center bg-black/92 backdrop-blur-md"
        @click.self="close"
        @touchstart.passive="onTouchStart"
        @touchend.passive="onTouchEnd"
        @wheel.prevent="onWheel"
      >
        <!-- Закрыть -->
        <button
          class="absolute top-4 right-5 z-10 w-11 h-11 rounded-full bg-white/10 hover:bg-red-500/70 text-white text-2xl flex items-center justify-center transition-colors"
          @click="close"
          title="Закрыть (Esc)"
        >✕</button>

        <!-- Сброс зума -->
        <button
          v-if="scale !== 1"
          class="absolute top-4 left-5 z-10 px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-white text-sm transition-colors"
          @click="resetZoom"
          title="Сбросить масштаб"
        >1:1</button>

        <!-- Предыдущая -->
        <button
          class="absolute left-3 top-1/2 -translate-y-1/2 z-10 w-12 h-12 rounded-full bg-white/10 hover:bg-white/25 text-white text-3xl flex items-center justify-center transition-colors"
          @click="go(-1)"
          title="Предыдущая (←)"
        >‹</button>

        <!-- Фото -->
        <div class="flex items-center justify-center w-full h-full overflow-hidden pointer-events-none">
          <img
            ref="imgEl"
            :src="images[current].src"
            :alt="images[current].alt"
            class="max-w-[90vw] max-h-[85vh] rounded-xl shadow-2xl object-contain transition-transform duration-100"
            :style="{ transform: `scale(${scale})` }"
            draggable="false"
          />
        </div>

        <!-- Следующая -->
        <button
          class="absolute right-3 top-1/2 -translate-y-1/2 z-10 w-12 h-12 rounded-full bg-white/10 hover:bg-white/25 text-white text-3xl flex items-center justify-center transition-colors"
          @click="go(1)"
          title="Следующая (→)"
        >›</button>

        <!-- Счётчик -->
        <div class="absolute bottom-5 left-1/2 -translate-x-1/2 bg-black/50 text-gray-300 text-sm px-4 py-1 rounded-full">
          {{ current + 1 }} / {{ total }}
        </div>

        <!-- Подсказка -->
        <div class="absolute bottom-12 left-1/2 -translate-x-1/2 text-white/30 text-xs whitespace-nowrap pointer-events-none">
          Скролл — листать &nbsp;|&nbsp; Ctrl + Скролл — масштаб &nbsp;|&nbsp; ← → — листать &nbsp;|&nbsp; Esc — закрыть
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.gm-fade-enter-active,
.gm-fade-leave-active { transition: opacity 0.2s ease; }
.gm-fade-enter-from,
.gm-fade-leave-to    { opacity: 0; }
</style>
