const COURSES = [
  {
    folder: "engineering-mathematics-1",
    code: "100102",
    title: "Engineering Mathematics - I",
    type: "theory",
    ltp: "3-0-0",
    credits: 3,
    units: [
      "Unit 1: Basic Linear Algebra (Rank, Eigenvalues, Cayley-Hamilton, Quadratic Forms)",
      "Unit 2: Differential Calculus: Single Variable (Leibnitz, Mean Value, Curvature)",
      "Unit 3: Differential Calculus: Several Variables (Euler's, Taylor's, Lagrange Multipliers)",
      "Unit 4: Integral Calculus (Double/Triple Integrals, Beta & Gamma Functions)",
      "Unit 5: Vector Calculus (Grad, Div, Curl, Green's, Stokes' & Gauss Theorems)"
    ]
  },
  {
    folder: "engineering-physics",
    code: "100104",
    title: "Engineering Physics",
    type: "theory",
    ltp: "3-0-0",
    credits: 3,
    units: [
      "Unit 1: Wave Optics (Newton's Rings, Michelson, Diffraction, Polarization)",
      "Unit 2: Lasers & Optical Fiber (Einstein A & B, He-Ne/Ruby, Numerical Aperture)",
      "Unit 3: Electromagnetism & Wave Propagation (Dielectrics, Maxwell's Eq, Poynting)",
      "Unit 4: Quantum Mechanics (De-Broglie, Schrödinger Eq, Particle in a Box, Tunneling)",
      "Unit 5: Semiconductors & Nano-materials (Hall Effect, Solar Cell, 0D/1D Nanomaterials)"
    ]
  },
  {
    folder: "ai",
    code: "100105",
    title: "Introduction to AI",
    type: "theory",
    ltp: "3-0-0",
    credits: 3,
    units: [
      "Unit 1: Intro to AI, PEAS Framework, Agent Architectures & Task Environments",
      "Unit 2: Problem Solving by Search (BFS, DFS, A*, Hill Climbing, Minimax, Alpha-Beta)",
      "Unit 3: Knowledge Representation & Reasoning (Propositional, FOPL, Resolution, Frames)",
      "Unit 4: Reasoning Under Uncertainty (Bayes' Theorem, Bayesian Networks, Fuzzy Logic)",
      "Unit 5: Intro to Machine Learning, ANN/Perceptron, NLP, Vision, Ethics & SDGs"
    ]
  },
  {
    folder: "computer-fundamentals",
    code: "100108",
    title: "Computer Fundamentals & Emerging Technologies",
    type: "theory",
    ltp: "3-0-0",
    credits: 3,
    units: [
      "Unit 1: Fundamentals of Computer Systems (CPU, Memory Hierarchy, Von-Neumann)",
      "Unit 2: Data Representation (Binary/Octal/Hex, 1's & 2's Complement, ASCII/Unicode)",
      "Unit 3: Computer Software & Operating Systems (Process/Memory Mgmt, CLI vs GUI)",
      "Unit 4: Computer Networks & Internet Basics (LAN/WAN, Topologies, TCP/UDP/HTTP/DNS)",
      "Unit 5: Emerging Technologies (IoT, Cyber Security & CIA Triad, AI/ML, Blockchain, Data Science)"
    ]
  },
  {
    folder: "universal-human-values",
    code: "100109",
    title: "Universal Human Values",
    type: "theory",
    ltp: "2-0-0",
    credits: 2,
    units: [
      "Unit 1: Self-Exploration, Continuous Happiness and Prosperity, Right Understanding",
      "Unit 2: Relationship, Physical Facility & Co-existence of Sentient 'Self' and Material 'Body'",
      "Unit 3: Values in Human-Human Relationships and Harmony in Society",
      "Unit 4: Harmony in Nature, Four Orders of Nature & Co-existence in Space",
      "Unit 5: Holistic Understanding on Professional Ethics & Universal Human Order"
    ]
  },
  {
    folder: "indian-constitution",
    code: "100110",
    title: "Essence of Indian Constitution",
    type: "theory",
    ltp: "3-0-0",
    credits: 0,
    units: [
      "Unit 1: Constitution Meaning, Historical Perspective, Salient Features & Preamble",
      "Unit 2: Fundamental Rights (Part-III) and Fundamental Duties & Significance",
      "Unit 3: Directive Principles of State Policy (Part-IV) & Relation to Fundamental Rights",
      "Unit 4: Governance under Part-VI, State Legislature: Assembly vs Council",
      "Unit 5: Constitutional Amendments: Powers, Procedure & 42nd, 44th, 74th, 76th, 86th, 91st"
    ]
  },
  {
    folder: "basics-of-electrical-electronics",
    code: "100111",
    title: "Basics of Electrical & Electronics Engineering",
    type: "theory",
    ltp: "3-0-0",
    credits: 3,
    units: [
      "Unit 1: Basic Electrical Circuits (Ohm's/Kirchhoff's Laws, Mesh/Nodal, Star-Delta)",
      "Unit 2: A.C. Circuits (RMS/Average, Peak/Form Factor, Phasors, Power Triangle, 3-Phase)",
      "Unit 3: Basic Electrical Machines (DC Machines, 1-Phase Transformers, Induction Motors)",
      "Unit 4: Semiconductor Devices (p-n Diode, Rectifiers, Zener Regulator, BJT CE Amplifier)",
      "Unit 5: Digital/Analog Electronics, IC 7805/7912, CRO/Multimeter, Sensors, MCB & Earthing"
    ]
  },
  {
    folder: "engineering-physics-lab",
    code: "100104P",
    title: "Engineering Physics Lab",
    type: "lab",
    ltp: "0-0-2",
    credits: 1,
    units: [
      "LE 1–4: Diffraction Grating, Newton's Rings, Telescope Resolving Power, Polarimeter",
      "LE 5–8: Optical Fiber NA, Dielectric Constant, Planck's Constant, Stern-Gerlach",
      "LE 9–12: p-n Junction I-V, Hall Effect, Four-Probe Band Gap, Nanoparticle Absorption"
    ]
  },
  {
    folder: "electrical-electronics-lab",
    code: "100111P",
    title: "Basics of Electrical & Electronics Engineering Lab",
    type: "lab",
    ltp: "0-0-2",
    credits: 1,
    units: [
      "LE 1–5: Ohm's Law, KVL/KCL, Power Factor Improvement, Transformer Ratio, DC/Induction Cut-Section",
      "LE 6–10: Diode V-I, Half/Full-Wave Rectifiers, Zener Regulator, BJT CE, Universal Logic Gates",
      "LE 11–16: CRO Measurements, Cables/Fuses, MCB/MCCB, Earthing, Domestic Wiring & Megger Test"
    ]
  },
  {
    folder: "programming-lab",
    code: "100112P",
    title: "Programming for Problem Solving Lab",
    type: "lab",
    ltp: "0-0-2",
    credits: 1,
    units: [
      "LE 1–5 (C): Flowcharts & I/O, Grading Switch-Case, Prime/Fibonacci Loops, 1D & 2D Matrix Arrays",
      "LE 6–10 (C): Pointers & Strings, Recursion (Factorial/GCD), Call by Ref, Struct/Union Payroll, File I/O",
      "LE 11–17 (C++): Bank Class, Dynamic String Constructors, Static/Friend, Inheritance, Polymorphism, Exceptions & Templates"
    ]
  }
];

// 1. Dynamic Quick Access & Quick Access Notes Updater (Fixes the AI redirect bug)
function updateQuickAccess(folder) {
  const course = COURSES.find((c) => c.folder === folder) || COURSES[0];
  localStorage.setItem("selectedSem1Subject", course.folder);

  document.getElementById("qaOverview").href = `${course.folder}/index.html`;
  document.getElementById("qaSyllabus").href = `${course.folder}/syllabus.html`;
  document.getElementById("qaAllNotes").href = `${course.folder}/notes.html`;
  document.getElementById("qaReferences").href = `${course.folder}/references.html`;

  const unitsBar = document.getElementById("qaUnitsBar");
  if (course.type === "theory") {
    unitsBar.style.display = "flex";
    for (let i = 1; i <= 5; i++) {
      const btn = document.getElementById(`qaUnit${i}`);
      btn.href = `${course.folder}/notes-unit${i}.html`;
      btn.textContent = `Unit ${i}`;
    }
  } else {
    unitsBar.style.display = "flex";
    for (let i = 1; i <= 5; i++) {
      const btn = document.getElementById(`qaUnit${i}`);
      btn.href = `${course.folder}/notes.html#part-${i}`;
      btn.textContent = `Exp Group ${i}`;
    }
  }
}

// 2. Render Course Cards with Direct Unit Note Links per Subject
function renderCourses(filter = "all", query = "") {
  const grid = document.getElementById("subjectsGrid");
  const q = query.trim().toLowerCase();

  const filtered = COURSES.filter((c) => {
    const matchesFilter = filter === "all" || c.type === filter;
    const matchesQuery =
      !q ||
      c.title.toLowerCase().includes(q) ||
      c.code.toLowerCase().includes(q) ||
      c.units.some((u) => u.toLowerCase().includes(q));
    return matchesFilter && matchesQuery;
  });

  grid.innerHTML = filtered
    .map((c) => {
      const unitLinks =
        c.type === "theory"
          ? `<div class="card-unit-pills">
              <a href="${c.folder}/notes-unit1.html">Unit 1</a>
              <a href="${c.folder}/notes-unit2.html">Unit 2</a>
              <a href="${c.folder}/notes-unit3.html">Unit 3</a>
              <a href="${c.folder}/notes-unit4.html">Unit 4</a>
              <a href="${c.folder}/notes-unit5.html">Unit 5</a>
            </div>`
          : `<div class="card-unit-pills">
              <a href="${c.folder}/notes.html">🔬 View All Lab Experiments</a>
            </div>`;

      return `
        <article class="subject-card">
          <div>
            <div class="card-top">
              <span class="code-pill">${c.code}</span>
              <span class="credit-pill">L-T-P: ${c.ltp} • ${c.credits} Credits</span>
            </div>
            <h3>${c.title}</h3>
            <ul class="unit-list">
              ${c.units.map((u) => `<li>• ${u}</li>`).join("")}
            </ul>
            ${unitLinks}
          </div>
          <div class="card-actions">
            <a class="card-btn primary" href="${c.folder}/index.html">Open Hub</a>
            <a class="card-btn" href="${c.folder}/syllabus.html">Syllabus</a>
            <a class="card-btn" href="${c.folder}/notes.html">Notes</a>
          </div>
        </article>
      `;
    })
    .join("");
}

document.addEventListener("DOMContentLoaded", () => {
  const select = document.getElementById("qaSubjectSelect");
  const saved = localStorage.getItem("selectedSem1Subject") || "engineering-mathematics-1";
  select.value = saved;
  updateQuickAccess(saved);

  select.addEventListener("change", (e) => updateQuickAccess(e.target.value));

  renderCourses();

  const searchInput = document.getElementById("subjectSearch");
  let activeFilter = "all";

  searchInput.addEventListener("input", (e) => {
    renderCourses(activeFilter, e.target.value);
  });

  document.querySelectorAll(".filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      activeFilter = btn.dataset.filter;
      renderCourses(activeFilter, searchInput.value);
    });
  });

  const themeBtn = document.getElementById("themeToggle");
  if (localStorage.getItem("sem1Theme") === "dark") {
    document.body.classList.add("dark");
  }
  themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    localStorage.setItem(
      "sem1Theme",
      document.body.classList.contains("dark") ? "dark" : "light"
    );
  });
});