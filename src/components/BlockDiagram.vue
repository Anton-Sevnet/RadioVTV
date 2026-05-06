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
      <svg viewBox="0 0 1100 750" class="w-full max-w-full" style="min-width:600px; height:auto;">
        <defs>
          <!-- Маркер-точка для инженерных выносок -->
          <marker id="dot" markerWidth="6" markerHeight="6" refX="3" refY="3">
            <circle cx="3" cy="3" r="3" fill="#bdc3c7" />
          </marker>
          <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#bdc3c7" />
          </marker>
          <marker id="noteArrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto" markerUnits="strokeWidth">
            <path d="M 0 0 L 9 4.5 L 0 9 z" fill="#8a96a3" />
          </marker>
        </defs>

        <rect width="1100" height="750" fill="#1a1a1a" />
        <text x="550" y="32" fill="#f1c40f" font-size="17" font-weight="bold" text-anchor="middle">Несущая вещания: 1219 кГц (СВ)</text>

        <!-- ГЛАВНАЯ ШИНА ПИТАНИЯ (только линии, без текста поверх) -->
        <!-- BAT+ шина -->
        <path d="M 150 280 L 780 280" fill="none" stroke="#e74c3c" stroke-width="4" />
        <!-- GND шина -->
        <path d="M 150 320 L 810 320" fill="none" stroke="#3498db" stroke-width="4" />

        <!-- Питание от бочек -->
        <rect x="50" y="250" width="100" height="100" fill="#34495e" stroke="#7f8c8d" stroke-width="3" rx="8" />
        <text x="60" y="295" fill="#ecf0f1" font-size="14" font-weight="bold">3 х Бочки</text>
        <text x="65" y="315" fill="#f1c40f" font-size="14" font-weight="bold">2.5V - 4.5V</text>

        <!-- ВОДЯНОЕ ЗАЗЕМЛЕНИЕ -->
        <rect x="50" y="460" width="300" height="200" fill="rgba(52, 152, 219, 0.15)" stroke="#2980b9" stroke-width="2" rx="10" />
        <rect x="58" y="466" width="178" height="22" fill="#13283a" />
        <text x="66" y="482" fill="#c7e6ff" font-size="13" font-weight="bold">Незамерзающий водоём</text>
        <path d="M 50 510 Q 125 490 200 510 T 350 510" fill="none" stroke="#3498db" stroke-width="2" />
        <rect x="58" y="636" width="205" height="18" fill="rgba(15, 23, 42, 0.65)" />
        <text x="66" y="650" fill="#d5dde6" font-size="11">Глубина ниже уровня промерзания</text>

        <!-- Провод заземления (чистая линия) -->
        <path d="M 180 320 L 180 460 M 180 490 L 180 560" fill="none" stroke="#3498db" stroke-width="4" />

        <!-- Консервная банка (Центр звезды) -->
        <ellipse cx="180" cy="560" rx="15" ry="8" fill="#95a5a6" stroke="#f1c40f" stroke-width="2" />
        <path d="M 165 560 L 165 575 A 15 8 0 0 0 195 575 L 195 560" fill="#7f8c8d" stroke="#f1c40f" stroke-width="2" />

        <!-- 8 лучей из плетёнки (чистые линии) -->
        <path d="M 180 570 L 110 570" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 570 L 250 570" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 570 L 180 620" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 570 L 130 605" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 570 L 230 605" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 570 L 140 535" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />
        <path d="M 180 570 L 220 535" fill="none" stroke="#e67e22" stroke-width="3" stroke-dasharray="4 2" />

        <!-- Блок 1: DC-DC MT3608 -->
        <rect x="250" y="100" width="120" height="80" fill="#2c3e50" stroke="#f39c12" stroke-width="2" rx="4" />
        <text x="260" y="130" fill="#f39c12" font-size="14" font-weight="bold">DC-DC MT3608</text>
        <text x="270" y="150" fill="#bdc3c7" font-size="12">Вход: 2.5-4.5V</text>
        <text x="270" y="165" fill="#bdc3c7" font-size="12">Выход: 5.0V</text>
        <!-- Соединения блока (чистые линии) -->
        <path d="M 280 280 L 280 180" fill="none" stroke="#e74c3c" stroke-width="2" />
        <path d="M 320 320 L 320 180" fill="none" stroke="#3498db" stroke-width="2" />
        <circle cx="280" cy="280" r="4" fill="#e74c3c" />
        <circle cx="320" cy="320" r="4" fill="#3498db" />

        <!-- Шина 5V (чистая линия) -->
        <path d="M 370 120 L 610 120" fill="none" stroke="#e67e22" stroke-width="3" />

        <!-- Блок 2: DFPlayer Mini -->
        <rect x="420" y="150" width="100" height="90" fill="#2c3e50" stroke="#9b59b6" stroke-width="2" rx="4" />
        <text x="430" y="180" fill="#9b59b6" font-size="14" font-weight="bold">DFPlayer Mini</text>
        <text x="445" y="205" fill="#bdc3c7" font-size="12">MicroSD</text>
        <text x="445" y="225" fill="#bdc3c7" font-size="12">MP3 / WAV</text>
        <!-- Соединения блока (чистые линии) -->
        <path d="M 450 120 L 450 150" fill="none" stroke="#e67e22" stroke-width="2" />
        <path d="M 480 320 L 480 240" fill="none" stroke="#3498db" stroke-width="2" />
        <circle cx="450" cy="120" r="4" fill="#e67e22" />
        <circle cx="480" cy="320" r="4" fill="#3498db" />

        <!-- Блок 3: Arduino Nano -->
        <rect x="580" y="150" width="120" height="90" fill="#2c3e50" stroke="#1abc9c" stroke-width="2" rx="4" />
        <text x="595" y="180" fill="#1abc9c" font-size="14" font-weight="bold">Arduino Nano</text>
        <text x="590" y="205" fill="#bdc3c7" font-size="12">(Без светодиодов)</text>
        <text x="610" y="225" fill="#bdc3c7" font-size="12">Генератор ШИМ</text>
        <!-- Соединения блока (чистые линии) -->
        <path d="M 610 120 L 610 150" fill="none" stroke="#e67e22" stroke-width="2" />
        <path d="M 650 320 L 650 240" fill="none" stroke="#3498db" stroke-width="2" />
        <circle cx="610" cy="120" r="4" fill="#e67e22" />
        <circle cx="650" cy="320" r="4" fill="#3498db" />

        <!-- Аудио сигнал (чистая линия) -->
        <path d="M 520 200 L 580 200" fill="none" stroke="#2ecc71" stroke-width="2" stroke-dasharray="4" />

        <!-- Блок 4: MOSFET Модуль -->
        <rect x="750" y="160" width="100" height="80" fill="#2c3e50" stroke="#e74c3c" stroke-width="2" rx="4" />
        <text x="800" y="182" fill="#e74c3c" font-size="13" font-weight="bold" text-anchor="middle">MOSFET</text>
        <text x="800" y="198" fill="#e74c3c" font-size="13" font-weight="bold" text-anchor="middle">Ключ</text>
        <text x="800" y="216" fill="#bdc3c7" font-size="11" text-anchor="middle">LR7843 / D4184</text>
        <text x="800" y="232" fill="#bdc3c7" font-size="11" text-anchor="middle">Logic Level</text>
        <!-- Соединения блока (чистые линии) -->
        <path d="M 780 280 L 780 240" fill="none" stroke="#e74c3c" stroke-width="3" />
        <path d="M 810 320 L 810 240" fill="none" stroke="#3498db" stroke-width="3" />
        <circle cx="780" cy="280" r="5" fill="#e74c3c" />
        <circle cx="810" cy="320" r="5" fill="#3498db" />

        <!-- Управление от Arduino (чистая линия) -->
        <path d="M 700 215 L 750 215" fill="none" stroke="#f1c40f" stroke-width="2" />

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

        <!-- Подключение фильтра к ключу (чистая линия) -->
        <path d="M 850 205 L 938 205 L 938 440 L 870 440" fill="none" stroke="#e74c3c" stroke-width="3" stroke-linejoin="round" />

        <!-- Земля фильтра -->
        <path d="M 840 480 L 840 500 L 900 500 L 900 320 L 810 320" fill="none" stroke="#3498db" stroke-width="3" stroke-linejoin="round" />

        <!-- Антенна (чистые линии) -->
        <path d="M 730 440 L 680 440 L 680 560" fill="none" stroke="#2ecc71" stroke-width="3" />
        <path d="M 680 560 L 640 600 M 680 560 L 720 600 M 680 560 L 680 620" fill="none" stroke="#2ecc71" stroke-width="2" />

        <!-- ═════════════════════════════════════════════════════════════════════════ -->
        <!-- АННОТАЦИИ: отдельные выноски, чтобы текст не лежал на линиях схемы -->
        <!-- ═════════════════════════════════════════════════════════════════════════ -->

        <!-- Выноска: BAT+ шина -->
        <rect x="18" y="180" width="158" height="54" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="39" cy="203" r="8" fill="none" stroke="#e74c3c" stroke-width="1.5" />
        <text x="39" y="207" fill="#e74c3c" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="54" y="203" fill="#d5dde6" font-size="11" font-weight="bold">BAT+ силовая шина</text>
        <text x="54" y="222" fill="#9aa8b6" font-size="9">напрямую к ключу</text>
        <path d="M 176 232 L 214 252 L 238 275" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: GND шина -->
        <rect x="18" y="360" width="150" height="44" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="39" cy="380" r="8" fill="none" stroke="#3498db" stroke-width="1.5" />
        <text x="39" y="384" fill="#3498db" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="54" y="380" fill="#d5dde6" font-size="11" font-weight="bold">GND силовая шина</text>
        <text x="54" y="397" fill="#9aa8b6" font-size="9">общий минус системы</text>
        <path d="M 168 360 L 215 335 L 238 324" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: +5V логика -->
        <rect x="390" y="52" width="152" height="50" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="407" cy="70" r="8" fill="none" stroke="#e67e22" stroke-width="1.5" />
        <text x="407" y="74" fill="#e67e22" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="422" y="70" fill="#d5dde6" font-size="11" font-weight="bold">+5V логика</text>
        <text x="422" y="87" fill="#9aa8b6" font-size="9">DFPlayer и Arduino</text>
        <path d="M 455 102 L 455 117" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: аудиосигнал -->
        <rect x="420" y="370" width="142" height="44" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="437" cy="388" r="8" fill="none" stroke="#2ecc71" stroke-width="1.5" />
        <text x="437" y="392" fill="#2ecc71" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="452" y="388" fill="#d5dde6" font-size="11" font-weight="bold">Audio DAC_R</text>
        <text x="452" y="405" fill="#9aa8b6" font-size="9">модуляция звука</text>
        <path d="M 562 388 L 565 250 L 552 205" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: ШИМ-несущая -->
        <rect x="708" y="70" width="152" height="50" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="725" cy="89" r="8" fill="none" stroke="#f1c40f" stroke-width="1.5" />
        <text x="725" y="93" fill="#f1c40f" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="740" y="90" fill="#d5dde6" font-size="11" font-weight="bold">PWM D9</text>
        <text x="740" y="107" fill="#9aa8b6" font-size="9">несущая 1219 кГц</text>
        <path d="M 750 120 L 735 158 L 730 215" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: Толстый спуск -->
        <rect x="205" y="388" width="142" height="44" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="222" cy="408" r="8" fill="none" stroke="#3498db" stroke-width="1.5" />
        <text x="222" y="412" fill="#3498db" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="237" y="412" fill="#d5dde6" font-size="11" font-weight="bold">Толстый спуск GND</text>
        <path d="M 205 410 L 184 430" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: Консервная банка -->
        <rect x="365" y="505" width="145" height="44" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="382" cy="524" r="8" fill="none" stroke="#f1c40f" stroke-width="1.5" />
        <text x="382" y="528" fill="#f1c40f" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="397" y="524" fill="#d5dde6" font-size="11" font-weight="bold">Консервная банка</text>
        <text x="397" y="541" fill="#9aa8b6" font-size="9">центр звезды, пайка</text>
        <path d="M 365 530 L 198 560" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: 8 лучей -->
        <rect x="365" y="565" width="190" height="44" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="382" cy="584" r="8" fill="none" stroke="#e67e22" stroke-width="1.5" />
        <text x="382" y="588" fill="#e67e22" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="397" y="584" fill="#d5dde6" font-size="11" font-weight="bold">8 лучей медной плетёнки</text>
        <text x="397" y="601" fill="#9aa8b6" font-size="9">топология «Звезда»</text>
        <path d="M 365 590 L 292 590 L 232 575" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Выноска: ВЧ меандр -->
        <rect x="965" y="332" width="125" height="50" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <circle cx="982" cy="351" r="8" fill="none" stroke="#e74c3c" stroke-width="1.5" />
        <text x="982" y="355" fill="#e74c3c" font-size="11" font-weight="bold" text-anchor="middle">i</text>
        <text x="997" y="351" fill="#d5dde6" font-size="11" font-weight="bold">ВЧ меандр</text>
        <text x="997" y="368" fill="#9aa8b6" font-size="9">к LC-ФНЧ 1219 кГц</text>
        <path d="M 965 355 L 940 355" fill="none" stroke="#8a96a3" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#noteArrow)" />

        <!-- Антенна (под символом) -->
        <rect x="580" y="633" width="200" height="49" fill="rgba(15, 23, 42, 0.82)" stroke="#8a96a3" stroke-width="1" stroke-dasharray="5 3" />
        <text x="680" y="653" fill="#d5dde6" font-size="12" font-weight="bold" text-anchor="middle">В антенну: длинный луч</text>
        <text x="680" y="670" fill="#9aa8b6" font-size="11" text-anchor="middle">Чистая синусоида (АМ)</text>

      </svg>
    </FullscreenZoomFrame>
  </section>
</template>
