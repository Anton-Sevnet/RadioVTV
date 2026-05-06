export const ASSEMBLY_STEPS = [
  {
    num: 1,
    title: 'Подготовка модулей (Откусываем лишнее)',
    color: 'border-accent-green',
    titleColor: 'text-accent-green',
    content: `Берём <strong>Arduino Nano</strong>. На плате есть два мелких SMD светодиода: <code>PWR</code> (красный, питание) и <code>L</code> (зелёный, встроен в пин 13). Под землёй не нужны, а электричество жрут. Берём тонкие кусачки или паяльник и просто <strong>скалываем их с платы</strong>. Так же поступаем со светодиодом на модуле <strong>DFPlayer Mini</strong>.`,
  },
  {
    num: 2,
    title: 'Подключение питания и Логики',
    color: 'border-accent-green',
    titleColor: 'text-accent-green',
    content: `Подключите <strong>MT3608</strong> к бочкам (IN+ и IN–). Покрутите латунный винтик на синем квадратике (потенциометре), пока мультиметр на выходе не покажет ровно <strong>5.0 Вольт</strong>. От OUT+ и OUT– киньте провода на пины <code>5V</code> и <code>GND</code> Arduino Nano, и на <code>VCC</code> и <code>GND</code> DFPlayer Mini.`,
  },
  {
    num: 3,
    title: 'Аудио-линия',
    color: 'border-accent-green',
    titleColor: 'text-accent-green',
    warning: 'НЕ ПОДКЛЮЧАЙТЕ ДИНАМИК к DFPlayer (пины SPK+/SPK–)! Встроенный усилитель сожжёт наш лимит энергии.',
    content: `Соединяем пин <strong>DAC_R</strong> (или DAC_L) на плеере с пином <strong>A0</strong> на Arduino. Это чистый, слаботочный линейный аудиосигнал.`,
  },
  {
    num: 4,
    title: 'Силовой ключ (MOSFET)',
    color: 'border-accent-green',
    titleColor: 'text-accent-green',
    content: `Берём готовый модуль MOSFET (D4184 или LR7843). Пин <code>PWM</code> (или SIG) соединяем с пином <strong>D9</strong> на Arduino — оттуда пойдёт несущая <strong>1219 кГц</strong>. Толстым проводом соединяем клеммы <code>VIN</code> и <code>GND</code> модуля <strong>НАПРЯМУЮ</strong> с клеммами бочек (минуя DC-DC преобразователь!). К клеммам <code>VOUT+</code> и <code>VOUT–</code> подключим сглаживающий фильтр.`,
  },
  {
    num: 5,
    title: 'Фильтр Нижних Частот (П-Контур) — Единственная пайка',
    color: 'border-accent-amber',
    titleColor: 'text-accent-amber',
    content: `Покупаем готовую выводную индуктивность (катушку) на <strong>100 мкГн с током не менее 1–2 А</strong> (напр. <em>DR74-101-R</em>) и два плёночных или керамических конденсатора на <strong>1000 пФ / 50V+</strong>.<br/><br/>
    <strong>Схема спайки:</strong><br/>
    1. Один конец катушки → <code>VOUT+</code> MOSFET, туда же — одна ножка первого конденсатора.<br/>
    2. Второй конец катушки → <strong>выход в Антенну</strong>, туда же — одна ножка второго конденсатора.<br/>
    3. Свободные ножки ОБОИХ конденсаторов → <code>VOUT–</code> (Силовая Земля).<br/><br/>
    <em>Всё! Вы собрали АМ-передатчик Класса E с КПД &gt;90%.</em>`,
  },
  {
    num: 6,
    title: 'Водяное заземление (Топология «Звезда»)',
    color: 'border-accent-blue',
    titleColor: 'text-accent-blue',
    content: `Берём обычную луженую <strong>консервную банку</strong> — центральный хаб. Покупаем <strong>медную плетёнку для снятия припоя</strong> (ширина 2.5–3.5 мм). Нарезаем <strong>8 лучей по 1.5–2 метра</strong>. Припаиваем все 8 лучей к банке — «звезда». <strong>Важно:</strong> паять чистым свинцом или припоем с высоким содержанием свинца. К банке также припаиваем толстый спускающийся кабель (GND) от передатчика. Бросаем «звезду» на дно водоёма и расправляем лучи (придавить камнями на концах).`,
  },
]
