<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import FullscreenBtn from './FullscreenBtn.vue'

const legend = [
  { bg: 'bg-[#2ecc71]', label: 'Зелёный — полотно антенны (медь ПуГВ)' },
  { bg: 'bg-white',     label: 'Светлые — керамические изоляторы (ИТО)' },
  { bg: 'bg-[#f1c40f]', label: 'Жёлтый — трос натяжения к противовесу' },
  { bg: 'bg-[#e67e22]', label: 'Оранжевый — коаксиальный фидер к передатчику' },
  { bg: 'bg-[#2980b9]', label: 'Синий — водоём (заземление «звезда» на дне)' },
  { bg: 'bg-[#34495e]', label: 'Тёмные цилиндры — бочки ПНД 65л (ячейки)' },
]

const canvasRef = ref(null)
const threeRef  = ref(null)
let renderer, controls, animId

onMounted(() => {
  const canvas = canvasRef.value
  if (!canvas) return

  const wrap = canvas.parentElement
  const W = Math.max(wrap ? wrap.clientWidth : 800, 320)
  const H = Math.min(420, window.innerHeight * 0.65)

  const scene = new THREE.Scene()
  scene.background = new THREE.Color(0x0d1117)

  const aspect = W / H
  const frustumSize = 38
  const camera = new THREE.OrthographicCamera(
    frustumSize * aspect / -2, frustumSize * aspect / 2,
    frustumSize / 2, frustumSize / -2, 0.5, 280
  )
  camera.position.set(44, 38, 46)
  camera.lookAt(0, 4, 2)

  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.setSize(W, H, false)
  renderer.shadowMap.enabled = true

  controls = new OrbitControls(camera, canvas)
  controls.target.set(0, 4, 2)
  controls.enableDamping = true
  controls.dampingFactor = 0.06
  controls.maxPolarAngle = Math.PI / 2 - 0.06

  scene.add(new THREE.AmbientLight(0x8899aa, 0.55))
  const sun = new THREE.DirectionalLight(0xffffff, 0.95)
  sun.position.set(22, 44, 18)
  sun.castShadow = true
  scene.add(sun)

  // Ground
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(90, 90),
    new THREE.MeshLambertMaterial({ color: 0x243d32 })
  )
  ground.rotation.x = -Math.PI / 2
  ground.receiveShadow = true
  scene.add(ground)

  // Water
  const waterGroup = new THREE.Group()
  const water = new THREE.Mesh(
    new THREE.CircleGeometry(14, 48),
    new THREE.MeshLambertMaterial({ color: 0x1a5276, emissive: 0x0a2540, transparent: true, opacity: 0.92 })
  )
  water.rotation.x = -Math.PI / 2
  water.position.set(4, 0.04, 22)
  water.scale.set(1.2, 1, 0.85)
  water.receiveShadow = true
  waterGroup.add(water)
  const shore = new THREE.Mesh(
    new THREE.RingGeometry(13.8, 15.2, 48),
    new THREE.MeshLambertMaterial({ color: 0x3d5c4a, transparent: true, opacity: 0.9 })
  )
  shore.rotation.x = -Math.PI / 2
  shore.position.set(4, 0.03, 22)
  shore.scale.set(1.2, 1, 0.85)
  waterGroup.add(shore)
  scene.add(waterGroup)

  // Star grounding
  const starHub = new THREE.Mesh(
    new THREE.CylinderGeometry(0.35, 0.4, 0.12, 12),
    new THREE.MeshLambertMaterial({ color: 0xb7950b })
  )
  starHub.rotation.x = Math.PI / 2
  starHub.position.set(4, 0.08, 22)
  scene.add(starHub)
  for (let i = 0; i < 8; i++) {
    const ang = (i / 8) * Math.PI * 2
    const ray = new THREE.Mesh(
      new THREE.BoxGeometry(3.2, 0.04, 0.12),
      new THREE.MeshLambertMaterial({ color: 0xc9a227 })
    )
    ray.position.set(4 + Math.cos(ang) * 1.6, 0.07, 22 + Math.sin(ang) * 1.6)
    ray.rotation.y = -ang
    scene.add(ray)
  }

  // Barrels
  function barrel(x, z) {
    const g = new THREE.Group()
    const body = new THREE.Mesh(
      new THREE.CylinderGeometry(0.72, 0.78, 2.0, 20),
      new THREE.MeshLambertMaterial({ color: 0x2c3e50 })
    )
    body.position.y = -0.35
    body.castShadow = true
    g.add(body)
    const rim = new THREE.Mesh(
      new THREE.TorusGeometry(0.78, 0.06, 8, 24),
      new THREE.MeshLambertMaterial({ color: 0x1a252f })
    )
    rim.rotation.x = Math.PI / 2
    rim.position.y = 0.55
    g.add(rim)
    g.position.set(x, 0, z)
    scene.add(g)
  }
  barrel(-5, -4)
  barrel(0, -5)
  barrel(5, -4)

  // Arctic pines
  function arcticPine(x, z, scale = 1) {
    const g = new THREE.Group()
    const h = 9.2 * scale
    const trunk = new THREE.Mesh(
      new THREE.CylinderGeometry(0.22 * scale, 0.42 * scale, h, 10),
      new THREE.MeshLambertMaterial({ color: 0x6d5c4d })
    )
    trunk.position.y = h / 2
    trunk.castShadow = true
    g.add(trunk)
    const barkMat = new THREE.MeshLambertMaterial({ color: 0x4a3f35 })
    for (let i = 0; i < 8; i++) {
      const ang = (i / 8) * Math.PI * 2 + (x + z) * 0.1
      const up = 0.35 + (i % 3) * 0.22
      const br = new THREE.Mesh(
        new THREE.CylinderGeometry(0.05 * scale, 0.03 * scale, 1.8 * scale, 5),
        barkMat
      )
      br.position.set(Math.cos(ang) * 0.32 * scale, h * up, Math.sin(ang) * 0.32 * scale)
      br.rotation.z = Math.PI / 2.5
      br.rotation.y = ang
      g.add(br)
    }
    const crownMat = new THREE.MeshLambertMaterial({ color: 0x3d5c45 })
    const crown = new THREE.Mesh(new THREE.SphereGeometry(1.05 * scale, 10, 8), crownMat)
    crown.position.y = h + 0.45 * scale
    crown.scale.set(1.1, 0.5, 1.05)
    crown.castShadow = true
    g.add(crown)
    const top = new THREE.Mesh(
      new THREE.SphereGeometry(0.45 * scale, 8, 6),
      new THREE.MeshLambertMaterial({ color: 0x4a6748 })
    )
    top.position.y = h + 0.95 * scale
    g.add(top)
    g.position.set(x, 0, z)
    scene.add(g)
    return g
  }

  const treePos = [[-18,-8], [-4,12], [20,0], [12,-16]]
  treePos.forEach(([tx, tz], i) => arcticPine(tx, tz, 0.92 + (i % 3) * 0.04))

  // Antenna wire
  const yWire = 10.05
  const pts = [
    new THREE.Vector3(-18, yWire, -8),
    new THREE.Vector3(-4,  yWire, 12),
    new THREE.Vector3(20,  yWire, 0),
    new THREE.Vector3(12,  yWire, -16),
  ]
  const wireCurve = new THREE.CatmullRomCurve3(pts, false, 'catmullrom', 0.35)
  scene.add(new THREE.Mesh(
    new THREE.TubeGeometry(wireCurve, 64, 0.06, 8, false),
    new THREE.MeshLambertMaterial({ color: 0x2ecc71, emissive: 0x0a3d22 })
  ))

  // Insulators
  const insMat = new THREE.MeshLambertMaterial({ color: 0xecf0f1 })
  pts.forEach(p => {
    const ins = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.2, 0.5, 8), insMat)
    ins.position.copy(p)
    scene.add(ins)
  })

  // Feed drop
  const feed    = pts[1].clone()
  const dropEnd = new THREE.Vector3(feed.x, 0.45, feed.z)
  scene.add(new THREE.Mesh(
    new THREE.TubeGeometry(new THREE.LineCurve3(feed, dropEnd), 12, 0.05, 6, false),
    new THREE.MeshLambertMaterial({ color: 0x27ae60 })
  ))

  // Coax
  const coaxEnd   = new THREE.Vector3(feed.x - 2, 0.35, feed.z + 5)
  const coaxCurve = new THREE.CatmullRomCurve3([
    dropEnd.clone(),
    new THREE.Vector3(feed.x - 0.5, 0.4, feed.z + 1.5),
    coaxEnd,
  ], false, 'catmullrom', 0.4)
  scene.add(new THREE.Mesh(
    new THREE.TubeGeometry(coaxCurve, 32, 0.09, 8, false),
    new THREE.MeshLambertMaterial({ color: 0xe67e22 })
  ))

  // Tension ropes & weights
  function rope(from, to, color) {
    scene.add(new THREE.Mesh(
      new THREE.TubeGeometry(new THREE.LineCurve3(from, to), 4, 0.04, 6, false),
      new THREE.MeshLambertMaterial({ color })
    ))
  }
  rope(new THREE.Vector3(-18, 2.8, -8),  new THREE.Vector3(-23, 0.35, -12), 0xf1c40f)
  rope(new THREE.Vector3(20,  2.8, 0),   new THREE.Vector3(25,  0.35, 4),   0xf1c40f)

  const weightGeo = new THREE.BoxGeometry(1.2, 0.6, 1.6)
  const weightMat = new THREE.MeshLambertMaterial({ color: 0x7f8c8d })
  ;[[-23, -12], [25, 4]].forEach(([wx, wz]) => {
    const w = new THREE.Mesh(weightGeo, weightMat)
    w.position.set(wx, 0.35, wz)
    w.castShadow = true
    scene.add(w)
  })

  function animate() {
    animId = requestAnimationFrame(animate)
    controls.update()
    renderer.render(scene, camera)
  }
  animate()

  window.addEventListener('resize', onResize)
  function onResize() {
    const parent = canvas.parentElement
    const isFullscreen = !!document.fullscreenElement || parent?.classList.contains('vtv-fs')
    const nw = Math.max(parent?.clientWidth ?? 800, 320)
    const nh = isFullscreen ? window.innerHeight : Math.min(420, window.innerHeight * 0.65)
    const a  = nw / nh
    camera.left   = frustumSize * a / -2
    camera.right  = frustumSize * a / 2
    camera.top    = frustumSize / 2
    camera.bottom = frustumSize / -2
    camera.updateProjectionMatrix()
    renderer.setSize(nw, nh, false)
  }
  canvas.__onResize = onResize
})

onBeforeUnmount(() => {
  if (animId) cancelAnimationFrame(animId)
  if (renderer) renderer.dispose()
  if (canvasRef.value?.__onResize) {
    window.removeEventListener('resize', canvasRef.value.__onResize)
  }
})
</script>

<template>
  <section id="antenna" class="section-card border-l-4 border-accent-green">
    <h2 class="section-heading">
      <span class="text-accent-green">8.1</span>
      Размещение антенны на соснах (схема в изометрии)
    </h2>

    <p class="text-gray-400 text-sm mb-4">
      <strong class="text-white">Водоём</strong> только с заземлением «звезда» на дне;
      три <strong class="text-white">бочки ПНД</strong> стоят на суше, под землёй у кромки леса;
      <strong class="text-white">заполярные сосны</strong> — высокие стволы с маленькой кроной;
      <strong class="text-white">горизонтальное полотно</strong> на высоте ~10 м, изоляторы, натяжение тросами.
      Несущая — <strong class="text-white">1219 кГц</strong>. Вращайте сцену мышью (ЛКМ).
    </p>

    <!-- Wire selection guide -->
    <div class="highlight-box mb-6">
      <h3 class="text-white font-semibold mb-2">Какой провод купить</h3>
      <p class="text-sm text-gray-300 mb-2">
        <strong class="text-white">Оптимально для полотна антенны:</strong> одножильный или многожильный
        <strong class="text-white">медный</strong> провод <strong class="text-white">ПуГВ сечением 4–6 мм²</strong>
        (на длинных линиях лучше 6 мм² — меньше потерь и механический запас).
        Ищите в отделе кабеля/провода: бухты 50–100 м.
      </p>
      <p class="text-sm text-gray-300 mb-2">
        <strong class="text-white">Альтернатива:</strong> гибкий силовой КГ или КГтп-ХЛ — устойчивее к перегибам на морозе.
      </p>
      <p class="text-sm text-red-300">
        <strong class="text-white">Не подойдёт:</strong> алюминиевая СИП (хрупкость), тонкий сигнальный провод без сечения.
      </p>
    </div>

    <!-- 3D Scene -->
    <div ref="threeRef"
         class="relative rounded-xl overflow-hidden border border-white/10 vtv-3d-fs"
         style="background: linear-gradient(180deg, #1a2332 0%, #0d1117 100%);">
      <FullscreenBtn :target-ref="threeRef" />
      <canvas
        ref="canvasRef"
        aria-label="Схема размещения антенны на соснах в изометрии"
        class="block w-full"
        style="height: min(420px, 70vh);"
      />
    </div>

    <!-- Legend -->
    <div class="grid grid-cols-2 md:grid-cols-3 gap-3 mt-4 text-sm text-gray-400">
      <div v-for="item in legend" :key="item.label" class="flex items-center gap-2">
        <span :class="['inline-block w-3 h-3 rounded-sm shrink-0', item.bg]" />
        {{ item.label }}
      </div>
    </div>

    <!-- Tensioning steps -->
    <div class="step-card border-accent-green mt-6">
      <h4 class="text-accent-green font-bold mb-3">Порядок натяжки (кратко)</h4>
      <ol class="space-y-2 text-sm text-gray-300 list-decimal list-inside">
        <li>На двух крайних соснах закрепить <strong class="text-white">столбовые крепления</strong> (хомуты с шайбой + абразивная лента) и <strong class="text-white">блоки (полиспасты)</strong> — через них трос к противовесу (бетонный блок, мешок с камнем).</li>
        <li>Полотно <strong class="text-white">ПуГВ</strong> класть на <strong class="text-white">изоляторы ИТО</strong>, не прижимая к коре: зазор уменьшает утечки ВЧ.</li>
        <li>К точке питания подводить <strong class="text-white">спуск ПуГВ</strong> вниз и горизонтальную трассу <strong class="text-white">коаксиалом 30 м</strong> (экран — на общую землю с передатчиком).</li>
        <li>Натягивать <strong class="text-white">постепенно</strong>: лёгкое натяжение, выдержать сутки — дерево «садится», затем подтянуть противовес.</li>
      </ol>
    </div>

    <p class="text-gray-600 text-xs mt-3">
      Графика: Three.js. Если сцена не появилась — откройте страницу в браузере с поддержкой WebGL и ES-модулей.
    </p>
  </section>
</template>
