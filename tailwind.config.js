/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts}',
  ],
  theme: {
    extend: {
      colors: {
        night:    '#0a0f1a',
        panel:    '#111827',
        border:   '#1f2937',
        accent: {
          green:  '#2ecc71',
          blue:   '#3498db',
          amber:  '#f1c40f',
          red:    '#e74c3c',
          orange: '#e67e22',
          purple: '#9b59b6',
          teal:   '#1abc9c',
        },
      },
      fontFamily: {
        sans: ['ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Consolas', 'monospace'],
      },
    },
  },
  plugins: [],
}
