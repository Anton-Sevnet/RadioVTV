<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'hero',
    validator: v => ['hero', 'footer'].includes(v),
  },
})

const telegramHref = ref('')

onMounted(() => {
  // Ссылку собираем на клиенте: в сыром HTML до гидратации её нет.
  telegramHref.value =
    '\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0074\u002e\u006d\u0065\u002f\u0073\u0065\u0076\u006e\u0065\u0074'

  // #region agent log
  fetch('http://127.0.0.1:7277/ingest/cc94e87f-d223-4e50-b5ea-9ad945c95ad9', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Debug-Session-Id': '5cc65f' },
    body: JSON.stringify({
      sessionId: '5cc65f',
      runId: 'tg-cta',
      hypothesisId: 'H5',
      location: 'TelegramAuthorCta.vue:onMounted',
      message: 'telegram_cta_hydrated',
      data: {
        variant: props.variant,
        host: typeof window !== 'undefined' ? window.location.host : '',
        hasHref: Boolean(telegramHref.value),
      },
      timestamp: Date.now(),
    }),
  }).catch(() => {})
  // #endregion
})
</script>

<template>
  <div
    v-if="variant === 'hero'"
    class="mt-8 pt-6 border-t border-white/10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"
  >
    <p class="text-gray-500 text-sm m-0 max-w-xl">
      Вопросы по проекту и эфиру — напишите автору в Telegram.
    </p>
    <a
      :href="telegramHref || undefined"
      target="_blank"
      rel="noopener noreferrer nofollow"
      class="inline-flex items-center justify-center gap-2.5 shrink-0 px-5 py-3 rounded-xl
             bg-[#229ED9] text-white font-semibold text-sm shadow-lg shadow-[#229ED9]/20
             hover:bg-[#1f8fc7] hover:shadow-[#229ED9]/30 active:translate-y-px transition-all no-underline"
    >
      <svg class="w-5 h-5 shrink-0" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.248-1.97 9.289c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.12L7.19 13.367l-2.97-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.537-.194 1.006.131.636.219z"/>
      </svg>
      Написать в Telegram
      <span class="text-white/90 font-normal">(@sevnet)</span>
    </a>
  </div>

  <div v-else class="flex flex-col items-center gap-2 w-full">
    <a
      :href="telegramHref || undefined"
      target="_blank"
      rel="noopener noreferrer nofollow"
      class="inline-flex items-center justify-center gap-2.5 px-6 py-3 rounded-xl
             bg-[#229ED9] text-white font-semibold text-sm shadow-lg shadow-[#229ED9]/20
             hover:bg-[#1f8fc7] hover:shadow-[#229ED9]/30 active:translate-y-px transition-all no-underline"
    >
      <svg class="w-5 h-5 shrink-0" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.248-1.97 9.289c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.12L7.19 13.367l-2.97-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.537-.194 1.006.131.636.219z"/>
      </svg>
      Написать в Telegram
      <span class="text-white/90 font-normal">(@sevnet)</span>
    </a>
  </div>
</template>
