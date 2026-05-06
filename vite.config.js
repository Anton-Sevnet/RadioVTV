import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/local/presentations/power_system_zapolyarye/',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor-vue':    ['vue'],
          'vendor-three':  ['three'],
          'vendor-chartjs': ['chart.js'],
        },
      },
    },
  },
})
