// Hero mascot: a cut-paper style padlock with eyes, built in Three.js.
// Toon shading + inverted-hull outlines give the thick black "sticker" lines.
// Click the lock (or the button) to unlock it. Confetti shards and coins orbit around it.
import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";

const stage = document.getElementById("stage");
const button = document.getElementById("unlock-btn");
if (stage) init();

function init() {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  } catch (e) {
    return; // keep the static SVG fallback
  }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.domElement.setAttribute("aria-hidden", "true");
  stage.prepend(renderer.domElement);
  stage.classList.add("is-3d");

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 100);
  camera.position.set(0, 0.4, 8);

  // ---- toon lighting ----
  scene.add(new THREE.AmbientLight(0xffffff, 0.9));
  const sun = new THREE.DirectionalLight(0xffffff, 2.2);
  sun.position.set(3, 4, 5);
  scene.add(sun);

  const tones = new Uint8Array([90, 170, 255]);
  const gradient = new THREE.DataTexture(tones, tones.length, 1, THREE.RedFormat);
  gradient.minFilter = gradient.magFilter = THREE.NearestFilter;
  gradient.needsUpdate = true;

  const toon = (color) => new THREE.MeshToonMaterial({ color, gradientMap: gradient });

  // Outline: same geometry, pushed out along normals, black, back faces only.
  const outlineMat = (thickness = 0.045) => {
    const m = new THREE.MeshBasicMaterial({ color: 0x1a1a1a, side: THREE.BackSide });
    m.onBeforeCompile = (shader) => {
      shader.vertexShader = shader.vertexShader.replace(
        "#include <begin_vertex>",
        `vec3 transformed = position + normal * ${thickness.toFixed(3)};`
      );
    };
    return m;
  };
  const withOutline = (geo, color, thickness) => {
    const g = new THREE.Group();
    g.add(new THREE.Mesh(geo, toon(color)));
    g.add(new THREE.Mesh(geo, outlineMat(thickness)));
    return g;
  };

  // ---- the padlock ----
  const lock = new THREE.Group();
  scene.add(lock);

  const body = withOutline(new RoundedBoxGeometry(2.2, 1.75, 0.9, 6, 0.32), 0xee4057, 0.05);
  body.position.y = -0.45;
  lock.add(body);

  // shackle: an arch + two legs, pivoting on the left leg
  const shacklePivot = new THREE.Group();
  shacklePivot.position.set(-0.62, 0.35, 0);
  lock.add(shacklePivot);
  const shackle = new THREE.Group();
  shackle.position.x = 0.62;
  shacklePivot.add(shackle);
  const arch = withOutline(new THREE.TorusGeometry(0.62, 0.16, 20, 48, Math.PI), 0xf4f1e6, 0.04);
  arch.position.y = 0.45;
  shackle.add(arch);
  for (const x of [-0.62, 0.62]) {
    const leg = withOutline(new THREE.CylinderGeometry(0.16, 0.16, 0.6, 20), 0xf4f1e6, 0.04);
    leg.position.set(x, 0.15, 0);
    shackle.add(leg);
  }

  // face: eyes with pupils that follow the cursor, blush, keyhole "mouth"
  const face = new THREE.Group();
  face.position.set(0, -0.3, 0.46);
  lock.add(face);
  const pupils = [];
  for (const x of [-0.42, 0.42]) {
    const eye = withOutline(new THREE.SphereGeometry(0.24, 24, 16), 0xffffff, 0.035);
    eye.scale.set(1, 1.15, 0.45);
    eye.position.set(x, 0.05, 0);
    eye.userData.eye = true;
    face.add(eye);
    const pupil = new THREE.Mesh(new THREE.SphereGeometry(0.11, 16, 12), new THREE.MeshBasicMaterial({ color: 0x1a1a1a }));
    pupil.position.set(x, 0.05, 0.1);
    pupil.userData.home = pupil.position.clone();
    pupil.userData.eye = true;
    face.add(pupil);
    pupils.push(pupil);
  }
  for (const x of [-0.78, 0.78]) {
    const blush = new THREE.Mesh(new THREE.CircleGeometry(0.11, 20), new THREE.MeshBasicMaterial({ color: 0xffd21f }));
    blush.position.set(x, -0.28, 0.02);
    face.add(blush);
  }
  const keyhole = new THREE.Group();
  const kTop = new THREE.Mesh(new THREE.CircleGeometry(0.11, 24), new THREE.MeshBasicMaterial({ color: 0x1a1a1a }));
  const kStem = new THREE.Mesh(new THREE.PlaneGeometry(0.1, 0.26), new THREE.MeshBasicMaterial({ color: 0x1a1a1a }));
  kStem.position.y = -0.14;
  keyhole.add(kTop, kStem);
  keyhole.position.set(0, -0.48, 0.02);
  face.add(keyhole);

  // ---- confetti shards + coins ----
  const palette = [0xee4057, 0x20b8b0, 0x1fa2e6, 0xffa62b, 0xffffff];
  const bits = [];
  const triGeo = new THREE.CylinderGeometry(0.2, 0.2, 0.05, 3);
  const coinGeo = new THREE.CylinderGeometry(0.22, 0.22, 0.07, 28);
  for (let i = 0; i < 22; i++) {
    const isCoin = i % 5 === 0;
    const mesh = isCoin
      ? withOutline(coinGeo, 0xffd21f, 0.025)
      : withOutline(triGeo, palette[i % palette.length], 0.02);
    const r = 2.4 + Math.random() * 1.6;
    mesh.userData = {
      r, a: (i / 22) * Math.PI * 2, y: (Math.random() - 0.5) * 2.6,
      speed: 0.12 + Math.random() * 0.18, spin: new THREE.Vector3(Math.random(), Math.random(), Math.random()).multiplyScalar(1.5),
    };
    mesh.rotation.set(Math.random() * 3, Math.random() * 3, Math.random() * 3);
    scene.add(mesh);
    bits.push(mesh);
  }

  // ---- interaction ----
  const pointer = new THREE.Vector2(0, 0);
  window.addEventListener("pointermove", (e) => {
    const r = stage.getBoundingClientRect();
    pointer.x = ((e.clientX - r.left) / r.width) * 2 - 1;
    pointer.y = -(((e.clientY - r.top) / r.height) * 2 - 1);
  });

  let unlocked = false;
  let open = 0; // 0 = locked, 1 = open
  const toggle = () => {
    unlocked = !unlocked;
    if (button) {
      button.textContent = unlocked ? "🔓 lock it back" : "🔒 click to unlock";
      button.setAttribute("aria-pressed", String(unlocked));
    }
    if (reduceMotion) render(0);
  };
  renderer.domElement.addEventListener("click", toggle);
  button?.addEventListener("click", toggle);

  // ---- sizing ----
  const resize = () => {
    const w = stage.clientWidth, h = stage.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.position.z = w < 500 ? 10 : 8;
    camera.updateProjectionMatrix();
    if (reduceMotion) render(0);
  };
  new ResizeObserver(resize).observe(stage);
  resize();

  // ---- animation ----
  const clock = new THREE.Clock();
  let blinkTimer = 2;
  function render(dt) {
    const t = clock.elapsedTime;
    open += ((unlocked ? 1 : 0) - open) * Math.min(1, dt * 6 || 1);
    shacklePivot.position.y = 0.35 + open * 0.45;
    shacklePivot.rotation.y = open * -1.1;

    lock.position.y = Math.sin(t * 1.6) * 0.08;
    lock.rotation.y += (pointer.x * 0.45 - lock.rotation.y) * 0.08;
    lock.rotation.x += (-pointer.y * 0.25 - lock.rotation.x) * 0.08;

    for (const p of pupils) {
      p.position.x = p.userData.home.x + pointer.x * 0.08;
      p.position.y = p.userData.home.y + pointer.y * 0.08;
    }
    blinkTimer -= dt;
    const blink = blinkTimer < 0.12 ? 0.1 : 1;
    if (blinkTimer < 0) blinkTimer = 2 + Math.random() * 3;
    face.children.forEach((c) => { if (c.userData.eye) c.scale.y = (pupils.includes(c) ? 1 : 1.15) * blink; });

    for (const b of bits) {
      const d = b.userData;
      d.a += d.speed * dt * (1 + open);
      b.position.set(Math.cos(d.a) * d.r, d.y + Math.sin(t + d.a) * 0.15, Math.sin(d.a) * d.r * 0.5 - 0.5);
      b.rotation.x += d.spin.x * dt; b.rotation.y += d.spin.y * dt; b.rotation.z += d.spin.z * dt;
    }
    renderer.render(scene, camera);
  }

  if (reduceMotion) {
    render(0);
  } else {
    renderer.setAnimationLoop(() => {
      const dt = Math.min(clock.getDelta(), 0.05);
      render(dt);
    });
  }
}
