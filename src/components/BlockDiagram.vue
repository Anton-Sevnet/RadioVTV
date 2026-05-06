<script setup>
import FullscreenZoomFrame from './FullscreenZoomFrame.vue'
</script>

<template>
  <section id="diagram" class="section-card">
    <h2 class="section-heading">
      <span class="text-gray-500">7.</span>
      Блок-схема и Принцип Соединения (Модульный подход)
    </h2>

    <p class="text-gray-400 text-sm mb-4">
      Вся электроника размещается в пластиковом контейнере и заливается прозрачным силиконовым компаундом.
      Водяное заземление топологии «Звезда» из медной плетёнки.
    </p>

    <FullscreenZoomFrame frame-class="overflow-auto rounded-xl border border-white/10 bg-[#1a1a1a] p-2 vtv-svg-fs">
      <svg viewBox="0 0 1000 650" class="w-full max-w-full" style="min-width:600px; height:auto;">
        <rect width="1000" height="650" fill="#1a1a1a" />
        <text x="500" y="32" fill="#f1c40f" font-size="17" font-weight="bold" text-anchor="middle">Несущая вещания: 1219 кГц (СВ)</text>
        <!-- Питание от бочек -->
        <rect x="50" y="250" width="100" height="100" fill="#34495e" stroke="#7f8c8d" stroke-width="3" rx="8" />
        <text x="60" y="295" fill="#ecf0f1" font-size="14" font-weight="bold">3 х Бочки</text>
        <text x="65" y="315" fill="#f1c40f" font-size="14" font-weight="bold">2.5V - 4.5V</text>
        <!-- Шина питания -->
        <path d="M 150 280 L 800 280" fill="none" stroke="#e74c3c" stroke-width="4" />
        <path d="M 150 320 L 800 320" fill="none" stroke="#3498db" stroke-width="4" />
        <text x="160" y="270" fill="#e74c3c" font-size="12" font-weight="bold">BAT+ (Силовой)</text>
        <text x="160" y="340" fill="#3498db" font-size="12" font-weight="bold">GND- (Силовой)</text>
        <!-- ВОДЯНОЕ ЗАЗЕМЛЕНИЕ -->
        <rect x="50" y="420" width="300" height="200" fill="rgba(52, 152, 219, 0.15)" stroke="#2980b9" stroke-width="2" rx="10" />
        <path d="M 50 450 Q 125 430 200 450 T 350 450" fill="none" stroke="#3498db" stroke-width="2" />
        <text x="60" y="440" fill="#3498db" font-size="14" font-weight="bold">Незамерзающий водоём</text>
        <text x="60" y="605" fill="#bdc3c7" font-size="12">Глубина ниже уровня промерзания</text>
        <!-- Провод заземления -->
        <path d="M 180 320 L 180 520" fill="none" stroke="#3498db" stroke-width="4" />
        <text x="190" y="380" fill="#3498db" font-size="12" font-weight="bold">Толстый спуск (GND)</text>
        <!-- Консервная банка (Центр звезды) -->
        <ellipse cx="180" cy="520" rx="15" ry="8" fill="#95a5a6" stroke="#f1c40f" stroke-width="2" />
        <path d="M 165 520 L 165 535 A 15 8 0 0 0 195 535 L 195 520" fill="#7f8c8d" stroke="#f1c40f" stroke-width="2" />
        <text x="210" y="525" fill="#f1c40f" font-size="12" font-weight="bold">Консервная банка</text>
        <text x="210" y="540" fill="#e67e22" font-size="11">(Пайка свинцом)</text>
        <!-- 8 лучей из плетёнки -->
        <path d="M 180 530 L 110 530" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 530 L 250 530" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 530 L 180 580" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 530 L 130 565" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 530 L 230 565" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 530 L 140 495" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 530 L 220 495" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <text x="70" y="545" fill="#e67e22" font-size="12" font-weight="bold">8 лучей</text>
        <text x="70" y="560" fill="#e67e22" font-size="11">Медная</text>
        <text x="70" y="575" fill="#e67e22" font-size="11">плетёнка</text>
        <!-- Блок 1: DC-DC MT3608 -->
        <rect x="250" y="100" width="120" height="80" fill="#2c3e50" stroke="#f39c12" stroke-width="2" rx="4" />
        <text x="260" y="130" fill="#f39c12" font-size="14" font-weight="bold">DC-DC MT3608</text>
        <text x="270" y="150" fill="#bdc3c7" font-size="12">Вход: 2.5-4.5V</text>
        <text x="270" y="165" fill="#bdc3c7" font-size="12">Выход: 5.0V</text>
        <path d="M 280 280 L 280 180" fill="none" stroke="#e74c3c" stroke-width="2" />
        <path d="M 320 320 L 320 180" fill="none" stroke="#3498db" stroke-width="2" />
        <circle cx="280" cy="280" r="4" fill="#e74c3c" />
        <circle cx="320" cy="320" r="4" fill="#3498db" />
        <!-- Шина 5V -->
        <path d="M 370 120 L 600 120" fill="none" stroke="#e67e22" stroke-width="3" />
        <text x="400" y="110" fill="#e67e22" font-size="12" font-weight="bold">+5V (Питание логики)</text>
        <!-- Блок 2: DFPlayer Mini -->
        <rect x="420" y="150" width="100" height="90" fill="#2c3e50" stroke="#9b59b6" stroke-width="2" rx="4" />
        <text x="430" y="180" fill="#9b59b6" font-size="14" font-weight="bold">DFPlayer Mini</text>
        <text x="445" y="205" fill="#bdc3c7" font-size="12">MicroSD</text>
        <text x="445" y="225" fill="#bdc3c7" font-size="12">MP3 / WAV</text>
        <path d="M 450 120 L 450 150" fill="none" stroke="#e67e22" stroke-width="2" />
        <path d="M 480 320 L 480 240" fill="none" stroke="#3498db" stroke-width="2" />
        <circle cx="450" cy="120" r="4" fill="#e67e22" />
        <circle cx="480" cy="320" r="4" fill="#3498db" />
        <!-- Блок 3: Arduino Nano -->
        <rect x="580" y="150" width="120" height="90" fill="#2c3e50" stroke="#1abc9c" stroke-width="2" rx="4" />
        <text x="595" y="180" fill="#1abc9c" font-size="14" font-weight="bold">Arduino Nano</text>
        <text x="590" y="205" fill="#bdc3c7" font-size="12">(Без светодиодов)</text>
        <text x="610" y="225" fill="#bdc3c7" font-size="12">Генератор ШИМ</text>
        <path d="M 600 120 L 600 150" fill="none" stroke="#e67e22" stroke-width="2" />
        <path d="M 640 320 L 640 240" fill="none" stroke="#3498db" stroke-width="2" />
        <circle cx="600" cy="120" r="4" fill="#e67e22" />
        <circle cx="640" cy="320" r="4" fill="#3498db" />
        <!-- Аудио сигнал (линия ниже подписи — без пересечения) -->
        <path d="M 518 204 L 582 204" fill="none" stroke="#2ecc71" stroke-width="2" stroke-dasharray="4" />
        <text
          x="520"
          y="196"
          fill="#2ecc71"
          font-size="10"
          font-weight="600"
          stroke="#1a1a1a"
          stroke-width="1.75"
          paint-order="stroke fill"
        >
          Audio (DAC_R)
        </text>
        <!-- Блок 4: MOSFET Модуль -->
        <rect x="750" y="160" width="100" height="80" fill="#2c3e50" stroke="#e74c3c" stroke-width="2" rx="4" />
        <text x="760" y="185" fill="#e74c3c" font-size="14" font-weight="bold">MOSFET Ключ</text>
        <text x="760" y="205" fill="#bdc3c7" font-size="12">(LR7843 / D4184)</text>
        <text x="770" y="225" fill="#bdc3c7" font-size="12">Logic Level</text>
        <path d="M 780 280 L 780 240" fill="none" stroke="#e74c3c" stroke-width="3" />
        <path d="M 800 320 L 800 240" fill="none" stroke="#3498db" stroke-width="3" />
        <circle cx="780" cy="280" r="5" fill="#e74c3c" />
        <circle cx="800" cy="320" r="5" fill="#3498db" />
        <!-- Управление от Arduino -->
        <path d="M 700 218 L 750 218" fill="none" stroke="#f1c40f" stroke-width="2" />
        <text
          x="702"
          y="209"
          fill="#f1c40f"
          font-size="10"
          font-weight="600"
          stroke="#1a1a1a"
          stroke-width="1.75"
          paint-order="stroke fill"
        >
          PWM (D9) → 1219 кГц
        </text>
        <!-- Блок 5: П-Контур (Фильтр) -->
        <rect x="730" y="380" width="140" height="90" fill="#34495e" stroke="#2ecc71" stroke-width="2" rx="4" />
        <text x="740" y="405" fill="#2ecc71" font-size="14" font-weight="bold">LC-Фильтр (ФНЧ)</text>
        <path d="M 740 440 L 760 440" fill="none" stroke="#fff" stroke-width="2" />
        <path d="M 760 440 Q 770 420 780 440 T 800 440 T 820 440 T 840 440 L 860 440" fill="none" stroke="#f1c40f" stroke-width="3" />
        <line x1="760" y1="440" x2="760" y2="460" stroke="#fff" stroke-width="2" />
        <line x1="750" y1="460" x2="770" y2="460" stroke="#fff" stroke-width="2" />
        <line x1="750" y1="465" x2="770" y2="465" stroke="#fff" stroke-width="2" />
        <line x1="840" y1="440" x2="840" y2="460" stroke="#fff" stroke-width="2" />
        <line x1="830" y1="460" x2="850" y2="460" stroke="#fff" stroke-width="2" />
        <line x1="830" y1="465" x2="850" y2="465" stroke="#fff" stroke-width="2" />
        <path d="M 760 465 L 760 480 L 840 480 L 840 465" fill="none" stroke="#3498db" stroke-width="2" />
        <!-- Подключение фильтра к ключу: трасса без захода на подпись -->
        <path d="M 850 205 L 938 205 L 938 440 L 870 440" fill="none" stroke="#e74c3c" stroke-width="3" stroke-linejoin="round" />
        <text
          x="732"
          y="352"
          fill="#e74c3c"
          font-size="11"
          font-weight="bold"
          stroke="#1a1a1a"
          stroke-width="1.5"
          paint-order="stroke fill"
        >
          <tspan x="732" dy="0">ВЧ меандр → LC-ФНЧ</tspan>
          <tspan x="732" dy="14">1219 кГц AM → антенна</tspan>
        </text>
        <!-- Земля фильтра -->
        <path d="M 800 480 L 800 320" fill="none" stroke="#3498db" stroke-width="3" />
        <circle cx="800" cy="320" r="5" fill="#3498db" />
        <!-- Антенна -->
        <path d="M 730 440 L 680 440 L 680 520" fill="none" stroke="#2ecc71" stroke-width="3" />
        <path d="M 680 520 L 640 560 M 680 520 L 720 560 M 680 520 L 680 580" fill="none" stroke="#2ecc71" stroke-width="2" />
        <text x="520" y="550" fill="#2ecc71" font-size="14" font-weight="bold">В Антенну («Длинный луч»)</text>
        <text x="520" y="570" fill="#bdc3c7" font-size="12">Чистая синусоида (АМ)</text>
      </svg>
    </FullscreenZoomFrame>
  </section>
</template>
