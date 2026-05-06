<script setup>
import { ref, watch, onMounted, onBeforeUnmount, computed } from 'vue'

const props = defineProps({
  modelValue: { type: Number, default: null }, // null = закрыто, иначе индекс текущего фото
  images: { type: Array, required: true },
})
const emit = defineEmits(['update:modelValue'])

const scale        = ref(1)
const displayIndex = ref(null)
const isLoading    = ref(false)
const numberKey    = ref(0)

const isOpen  = computed(() => props.modelValue !== null)
const current = computed(() => props.modelValue ?? 0)
const total   = computed(() => props.images.length)
const displayPhoto = computed(() => props.images[displayIndex.value ?? current.value])
const targetPhoto  = computed(() => props.images[current.value])
const watermark    = computed(() => targetPhoto.value?.author ? `Фото: ${targetPhoto.value.author}` : '')

let loadToken = 0
let lastWheelNavAt = 0

function loadCurrentImage() {
  if (!isOpen.value || !targetPhoto.value) return

  const token = ++loadToken
  const targetIndex = current.value
  const image = new Image()

  scale.value = 1
  isLoading.value = true
  numberKey.value += 1

  image.onload = () => {
    if (token !== loadToken) return
    displayIndex.value = targetIndex
    isLoading.value = false
  }

  image.onerror = () => {
    if (token !== loadToken) return
    displayIndex.value = targetIndex
    isLoading.value = false
  }

  image.src = targetPhoto.value.src
}

function close() {
  loadToken += 1
  isLoading.value = false
  displayIndex.value = null
  emit('update:modelValue', null)
}

function go(dir) {
  scale.value = 1
  const next = ((current.value + dir) % total.value + total.value) % total.value
  emit('update:modelValue', next)
}

function resetZoom() { scale.value = 1 }

function onWheel(e) {
  if (!isOpen.value) return
  e.preventDefault()
  if (e.ctrlKey) {
    const delta = e.deltaY < 0 ? 1.12 : 0.89
    scale.value = Math.min(8, Math.max(0.3, scale.value * delta))
  } else {
    const now = Date.now()
    if (now - lastWheelNavAt < 260) return
    lastWheelNavAt = now
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
watch(() => props.modelValue, () => {
  if (props.modelValue === null) return
  loadCurrentImage()
})

// Блокировка прокрутки страницы когда галерея открыта
watch(isOpen, (v) => { document.body.style.overflow = v ? 'hidden' : '' })

onMounted(() => {
  window.addEventListener('keydown', onKey)
  window.addEventListener('wheel', onWheel, { passive: false })
})
onBeforeUnmount(() => {
  window.removeEventListener('keydown', onKey)
  window.removeEventListener('wheel', onWheel)
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
        <div class="relative flex items-center justify-center w-full h-full overflow-hidden pointer-events-none">
          <img
            v-if="displayPhoto"
            :src="displayPhoto.src"
            :alt="displayPhoto.alt"
            class="max-w-[90vw] max-h-[85vh] rounded-xl shadow-2xl object-contain transition-all duration-300"
            :class="{ 'blur-md opacity-55 saturate-50': isLoading }"
            :style="{ transform: `scale(${scale})` }"
            draggable="false"
          />

          <div
            v-if="isLoading"
            class="absolute inset-0 flex items-center justify-center"
            aria-live="polite"
          >
            <div class="w-14 h-14 rounded-full border-4 border-white/20 border-t-white/80 animate-spin" />
          </div>

          <div
            :key="numberKey"
            class="gm-photo-number absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 text-white/90 text-7xl md:text-8xl font-black tracking-tight drop-shadow-[0_6px_22px_rgba(0,0,0,0.85)]"
          >
            {{ current + 1 }}
          </div>

          <div
            v-if="watermark"
            class="absolute right-6 bottom-16 max-w-[70vw] rounded-full bg-black/35 px-4 py-1.5 text-xs md:text-sm text-white/45 backdrop-blur-sm"
          >
            {{ watermark }}
          </div>
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

.gm-photo-number {
  animation: gm-photo-number-fade 0.85s ease-out forwards;
}

@keyframes gm-photo-number-fade {
  0% {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.84);
  }
  18% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
  100% {
    opacity: 0;
    transform: translate(-50%, -50%) scale(1.14);
  }
}
</style>
