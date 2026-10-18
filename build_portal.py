import os
import re

# Complete Syllabus + TSO Exam Outcomes + Key Study Notes (Batch 2026-2030 Group-A)
SUBJECTS = {
    "engineering-mathematics-1": {
        "code": "100102",
        "title": "Engineering Mathematics - I",
        "credits": "3-0-0 (3 Credits)",
        "cos": [
            "CO1: Apply the concept of Linear/Matrix algebra to solve given engineering problems.",
            "CO2: Demonstrate the ability to solve engineering problems based on the application of derivatives.",
            "CO3: Solve the given optimization problems by using the concept of partial derivatives.",
            "CO4: Evaluate the given multiple integrals in different coordinate systems to solve complex engineering problems.",
            "CO5: Apply the concept of vector calculus to solve the given engineering problems."
        ],
        "units": [
            ("Unit 1.0: Basic Linear Algebra (8 hrs)", [
                "1.1 Elementary transformations and Rank of Matrix, Rank by using Echelon and Normal form of Matrices. Linear dependence & independence of vectors in R^n space.",
                "1.2 Consistency of System of Linear Equations (Rouche's Theorem: AX = B and AX = 0).",
                "1.3 Eigenvalues & Eigenvectors (|A - λI| = 0), Cayley-Hamilton Theorem & finding integral powers/inverse of a matrix.",
                "1.4 Similarity of Matrices & Diagonalization (D = P⁻¹AP). Quadratic Form to Canonical Form of Matrices.",
                "Exam Focus (TSO 1a–1d): Find matrix rank via Echelon/Normal form, test consistency of linear systems, apply Cayley-Hamilton theorem for matrix powers, and test nature of quadratic forms."
            ]),
            ("Unit 2.0: Differential Calculus: Single Variable (8 hrs)", [
                "2.1 Higher order derivatives; Successive differentiation and Leibnitz's Theorem for nth derivative of product u·v.",
                "2.2 Mean Value Theorems: Rolle's Theorem, Lagrange's Mean Value Theorem, and Cauchy's Mean Value Theorem.",
                "2.3 Indeterminate Forms (0/0, ∞/∞, 0·∞, ∞−∞, 0⁰, 1^∞, ∞⁰) and L'Hospital's Rule.",
                "2.4 Tangents & Normals of Algebraic & Polar Curves, Radius of Curvature (Cartesian, Parametric, and Polar forms).",
                "Exam Focus (TSO 2a–2d): Find nth order derivatives via Leibnitz's rule, verify Mean Value Theorems, evaluate limits via L'Hospital's rule, and compute curvature of engineering curves."
            ]),
            ("Unit 3.0: Differential Calculus: Several Variables (9 hrs)", [
                "3.1 Partial differentiations; Homogeneous functions and Euler's Theorem (x ∂u/∂x + y ∂u/∂y = n·u).",
                "3.2 Limit, Continuity and Differentiability of functions of Several Variables.",
                "3.3 Taylor's Theorem with remainders and Maclaurin's series expansion in two variables.",
                "3.4 Maxima & Minima of functions of two variables (rt - s² test); Lagrange's Method of Undetermined Multipliers.",
                "Exam Focus (TSO 3a–3d): Apply Euler's theorem, test multi-variable differentiability, expand functions via Taylor's theorem, and optimize constrained engineering functions via Lagrange multipliers."
            ]),
            ("Unit 4.0: Integral Calculus (9 hrs)", [
                "4.1 Differentiation under the integral sign; Leibnitz's Rule.",
                "4.2 Double Integrals; Change of order of integration; Double integration in Polar Coordinates (dx dy = r dr dθ) for area.",
                "4.3 Triple Integrals; Volume evaluation in Cylindrical (r dr dθ dz) and Spherical Polar (r² sinθ dr dθ dφ) coordinates.",
                "4.4 Improper Integrals: Beta and Gamma functions, Relation B(m,n) = Γ(m)Γ(n)/Γ(m+n), Elliptic integrals.",
                "Exam Focus (TSO 4a–4d): Evaluate definite integrals using Leibnitz's rule, find plane area by double integrals, 3D volume by triple integrals, and improper integrals via Beta & Gamma functions."
            ]),
            ("Unit 5.0: Vector Calculus (8 hrs)", [
                "5.1 Scalar and vector point functions; Gradient (∇φ), Divergence (∇·F), Curl (∇×F) & physical significance; Directional derivative and Tangent plane.",
                "5.2 Line integrals, Surface integrals, and Volume integrals.",
                "5.3 Green's Theorem in a plane, Stokes' Theorem (line to surface integral), and Gauss Divergence Theorem (surface to volume integral).",
                "Exam Focus (TSO 5a–5c): Compute grad/div/curl (irrotational & solenoidal fields), apply Stokes' theorem, and apply Gauss' divergence theorem."
            ])
        ],
        "books": [
            "B. S. Grewal — Higher Engineering Mathematics (Khanna Publishers, 44th Ed., ISBN: 9788174091154)",
            "B. V. Ramana — Higher Engineering Mathematics (Tata McGraw Hill, 11th Ed., ISBN: 978-0070634190)",
            "Erwin Kreyszig — Advanced Engineering Mathematics (John Wiley & Sons, 10th Ed., ISBN: 978-0470-15836-5)",
            "N. P. Bali & Dr. Manish Goyal — A Textbook of Engineering Mathematics (University Science Press, 13th Ed., ISBN: 978-93-83828-63-0)",
            "John Bird — Understanding Engineering Mathematics (Routledge, 1st Ed., ISBN: 9780415662840)"
        ]
    },
    "engineering-physics": {
        "code": "100104",
        "title": "Engineering Physics",
        "credits": "3-0-0 (3 Credits)",
        "cos": [
            "CO1: Apply the concepts of wave optics phenomena in various engineering fields.",
            "CO2: Apply the concepts of laser operation and fiber optic propagation in engineering applications.",
            "CO3: Apply the concepts of electromagnetics in engineering applications.",
            "CO4: Utilize semiconductor devices, based on their I-V characteristics, for various engineering applications.",
            "CO5: Apply the principles of Quantum mechanics to analyze quantum phenomena in engineering systems."
        ],
        "units": [
            ("Unit 1.0: Wave Optics (8 hrs)", [
                "1.1 Interference by division of amplitude, Newton's Ring experiment (λ = (D_{m+p}² - D_m²)/(4pR)), Michelson Interferometer.",
                "1.2 Fraunhofer Diffraction at Single slit, Double slit, and Circular aperture.",
                "1.3 Plane transmission Diffraction Grating (d sinθ = nλ) & dispersive/resolving power.",
                "1.4 Rayleigh Criterion for limit of resolution & Resolving Power of a Telescope (RP = D / 1.22λ).",
                "1.5 Polarization of light, Double-refracting crystal (O-ray and E-ray), Construction and working of Nicol Prism."
            ]),
            ("Unit 2.0: Lasers and Optical Fiber (8 hrs)", [
                "2.1 Laser characteristics (coherence, directionality, monochromaticity), Spontaneous vs Stimulated emission, Einstein's A & B coefficients derivation, Population inversion, Pumping, Optical resonator.",
                "2.2 Construction, energy level diagram, and working of Ruby Laser (3-level), He-Ne Laser (4-level), and Semiconductor Laser.",
                "2.3 Optical Fiber structure, Total Internal Reflection (TIR), Acceptance Angle, Numerical Aperture (NA = √(n₁² - n₂²)), Step-index vs Graded-index (Single-mode & Multi-mode) fibers.",
                "2.4 Light propagation mechanism & Attenuation losses (absorption, Rayleigh scattering, bending losses) in optical fibers.",
                "2.5 Applications of Lasers and Fiber Optic Sensors in communications, medical, defense, and industries."
            ]),
            ("Unit 3.0: Electromagnetism & Propagation of Waves (8 hrs)", [
                "3.1 Electric fields, Gauss's Law in dielectric media, Dielectric constant, Polarization, and Capacitors with dielectrics.",
                "3.2 Magnetic fields & classification of Dia-, Para-, and Ferromagnetic materials.",
                "3.3 Maxwell's Four Equations in integral and differential forms and their physical significance (Displacement current).",
                "3.4 Electromagnetic wave propagation & Poynting Vector (S = E × H) and Poynting Theorem for energy transport per unit area."
            ]),
            ("Unit 4.0: Quantum Mechanics (8 hrs)", [
                "4.1 Inadequacy of classical mechanics and need for Quantum Mechanics.",
                "4.2 De-Broglie matter wave hypothesis (λ = h/p) and Heisenberg's Uncertainty Principle (Δx·Δp ≥ ℏ/2).",
                "4.3 Wave function ψ(x,t), physical significance (Born probability density |ψ|²), normalization and orthogonality.",
                "4.4 Time-dependent and Time-independent Schrödinger Wave Equations.",
                "4.5 Particle in a 1D infinite potential box: Quantized Energy Eigenvalues (E_n = n²h²/(8mL²)) and Normalized Eigenfunctions.",
                "4.6 Finite Potential Barrier and Quantum Mechanical Tunneling."
            ]),
            ("Unit 5.0: Semiconductors & Nano-materials (10 hrs)", [
                "5.1 Energy band comparison of Metals, Insulators, and Semiconductors.",
                "5.2 Intrinsic and Extrinsic (N-type & P-type) semiconductors, Drift and Diffusion current density, Fermi level variation.",
                "5.3 Working and characteristics of Photodiode, P-N junction transistor, and LED.",
                "5.4 Hall Effect: Determination of Hall coefficient (R_H), carrier type, concentration, and mobility.",
                "5.5 Solar Cell: Photovoltaic principle, I-V characteristics, fill factor, and efficiency.",
                "5.6–5.8 Introduction to Nanoscience & Nanotechnology; Surface-to-volume ratio, quantum confinement effect on band gap, and classification into 0D (Quantum Dots) and 1D (Nanowires)."
            ])
        ],
        "books": [
            "Ajay Ghatak — Optics (McGraw Hill Education, 5th Ed., ISBN-10: 1259004340)",
            "O. Svelto — Principles of Lasers (Springer, 5th Ed., ISBN-10: 1441913017)",
            "David J. Griffiths — Introduction to Electrodynamics (Cambridge University Press, 5th Ed., ISBN-10: 1009397729)",
            "S. O. Kasap — Principles of Electronic Materials and Devices (McGraw Hill, 3rd Ed., ISBN-10: 0073104647)",
            "Donald A. Neamen — Semiconductor Physics and Devices (McGraw-Hill, 4th Ed., ISBN-10: 0073529583)",
            "David J. Griffiths — Introduction to Quantum Mechanics (Cambridge University Press, 2nd Ed., ISBN-10: 1107179866)",
            "Sulabha K. Kulkarni — Nanotechnology: Principles and Practices (Springer, 3rd Ed., ISBN-10: 3319091700)",
            "S. K. Roy — Concepts of Engineering Physics & Physics Practical for Engineers (Novelty Publication)",
            "Kumari Mamta & Raj Kumar Singh — Concepts of Engineering Physics (CRC Press, ISBN: 9781041191834)"
        ]
    },
    "ai": {
        "code": "100105",
        "title": "Introduction to AI",
        "credits": "3-0-0 (3 Credits)",
        "cos": [
            "CO1: Explain the foundational concepts of Artificial Intelligence, intelligent agents, and task environments.",
            "CO2: Trace uninformed, informed, local, and adversarial search strategies for solving AI problems.",
            "CO3: Perform manual logical inference using propositional and predicate logic and structured knowledge representation.",
            "CO4: Apply probabilistic reasoning and basic fuzzy-logic concepts to handle uncertainty in AI systems.",
            "CO5: Analyze foundational machine learning paradigms underlying AI-based systems."
        ],
        "units": [
            ("Unit 1.0: Introduction to Artificial Intelligence (8 hrs)", [
                "1.1 What is AI? History and evolution of AI.",
                "1.2 Foundations of AI: philosophy, mathematics, and cognitive-science influences.",
                "1.3 Intelligent agents: agent-environment interaction, PEAS (Performance measure, Environment, Actuators, Sensors) framework.",
                "1.4 Properties of Task Environments: Observable vs Partially Observable, Deterministic vs Stochastic, Episodic vs Sequential, Static vs Dynamic, Discrete vs Continuous, Single vs Multi-agent.",
                "1.5 Agent Architectures: Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, and Learning Agents.",
                "1.6 Overview of AI application domains across engineering disciplines."
            ]),
            ("Unit 2.0: Problem Solving by Search (9 hrs)", [
                "2.1 State-space problem formulation (Initial state, Actions, Transition model, Goal test, Path cost).",
                "2.2 Uninformed Search: Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search (UCS), Depth-Limited Search (DLS), Iterative Deepening Search (IDS).",
                "2.3 Informed (Heuristic) Search: Greedy Best-First Search, A* Search (f(n) = g(n) + h(n)).",
                "2.4 Heuristic function design: Admissibility (h(n) ≤ h*(n)) and Consistency (triangle inequality).",
                "2.5 Local Search: Hill Climbing (and local maxima/plateau/ridge issues), Simulated Annealing.",
                "2.6 Adversarial Search: Minimax algorithm and Alpha-Beta Pruning for two-player games.",
                "2.7 Constraint Satisfaction Problems (CSPs): Variables, Domains, Constraints, and Backtracking search."
            ]),
            ("Unit 3.0: Knowledge Representation and Reasoning (8 hrs)", [
                "3.1 Knowledge representation issues; Propositional Logic syntax, semantics, and truth tables.",
                "3.2 Inference in Propositional Logic: Conjunctive Normal Form (CNF) and Resolution refutation.",
                "3.3 First-Order Predicate Logic (FOPL): Syntax, predicates, functions, Universal (∀) and Existential (∃) quantifiers.",
                "3.4 Inference in FOPL: Unification, Forward Chaining, Backward Chaining, and Resolution.",
                "3.5 Structured Knowledge Representation: Semantic Networks (IS-A, HAS-A links) and Frames (slots and fillers).",
                "3.6 Rule-based (Production) Systems architecture (Working memory, Rule base, Inference engine)."
            ]),
            ("Unit 4.0: Reasoning Under Uncertainty (7 hrs)", [
                "4.1 Sources of uncertainty in real-world AI; Conditional probability and product rule.",
                "4.2 Bayes' Theorem: P(H|E) = [P(E|H)·P(H)] / P(E) and application to diagnostic reasoning.",
                "4.3 Bayesian Networks: Directed Acyclic Graph (DAG), Conditional Probability Tables (CPTs), and manual inference.",
                "4.4 Fuzzy Logic & Fuzzy Sets: Membership functions μ(x) ∈ [0,1], Fuzzy Union, Intersection, and Complement operations.",
                "4.5 Certainty Factors (CF) and rule-based uncertainty overview."
            ]),
            ("Unit 5.0: Introduction to Machine Learning and AI Applications (10 hrs)", [
                "5.1 Machine Learning Paradigms: Supervised, Unsupervised, and Reinforcement Learning.",
                "5.2 Regression and Classification concepts: Linear Regression, k-Nearest Neighbors (k-NN), and Decision Trees.",
                "5.3 Unsupervised Clustering concept: k-Means clustering algorithm.",
                "5.4 Artificial Neural Networks (ANN): Single-layer Perceptron model, weights, bias, activation functions, and multilayer architecture.",
                "5.5–5.8 AI Domains: Natural Language Processing (NLP), Computer Vision, Expert Systems, and Intelligent Robotics.",
                "5.9 AI Ethics, algorithmic bias, Responsible AI, societal impact, and AI for UN Sustainable Development Goals (SDGs)."
            ])
        ],
        "books": [
            "Stuart Russell & Peter Norvig — Artificial Intelligence: A Modern Approach (Pearson, 4th Ed., ISBN: 978-0134610993)",
            "Saptarsi Goswami, Amit Kumar Das, Amlan Chakrabarti — AI for Everyone (Pearson, ISBN: 978-9361591754)",
            "Dan W. Patterson — Introduction to Artificial Intelligence and Expert Systems (PHI Learning, ISBN: 978-8120307775)",
            "Elaine Rich, Kevin Knight, Shivashankar B. Nair — Artificial Intelligence (McGraw-Hill, 3rd Ed., ISBN: 978-1259029420)",
            "Dilip Narayan Sahu et al. — Artificial Intelligence - A Modern Approach (ISBN: 978-9355151445)",
            "Dhairya Parikh — Machine Learning Essentials (Vibrant Publishers, ISBN: 978-1636513775)"
        ]
    },
    "computer-fundamentals": {
        "code": "100108",
        "title": "Computer Fundamentals & Emerging Technologies",
        "credits": "3-0-0 (3 Credits)",
        "cos": [
            "CO1: Analyze the structure and interaction of computer system components.",
            "CO2: Apply number system conversions and data representation techniques to solve computational problems.",
            "CO3: Differentiate types of operating systems based on their functions and suitability for various applications.",
            "CO4: Analyse computer network components, topologies, and data communication processes.",
            "CO5: Identify appropriate emerging technologies to address given engineering problems."
        ],
        "units": [
            ("Unit 1.0: Fundamentals of Computer Systems (8 hrs)", [
                "1.1 Classification of computers (Micro, Mini, Mainframe, Supercomputers) and Functional units (Input, CPU, Memory, Output).",
                "1.2 Central Processing Unit (CPU) organization: ALU, Control Unit (CU), Registers, and Fetch-Decode-Execute cycle.",
                "1.3 Memory Architecture, Memory Representation (Bits, Bytes, Words), and Memory Hierarchy (Registers → Cache → RAM → Secondary Storage).",
                "1.4 Role of CPU Registers (PC, IR, MAR, MDR, Accumulator) and impact of L1/L2/L3 Cache Memory on system performance.",
                "1.5 Motherboard components: CPU socket, Chipset (Northbridge/Southbridge/PCH), System buses, PCIe slots, CMOS/BIOS/UEFI.",
                "1.6 The Von-Neumann Stored-Program Architecture and Von-Neumann bottleneck.",
                "1.7 Machine Language, Assembly Language (Assembler), and High-Level Languages; Compiler vs Interpreter comparison."
            ]),
            ("Unit 2.0: Data Representation (8 hrs)", [
                "2.1 Data Representation & Positional Number Systems: Binary (Base-2), Octal (Base-8), Decimal (Base-10), Hexadecimal (Base-16).",
                "2.2 Step-by-step conversion between Decimal and Binary systems (integer and fractional parts).",
                "2.3 Fast conversion among Binary, Octal (3-bit grouping), and Hexadecimal (4-bit grouping) systems.",
                "2.4 Binary Arithmetic operations: Binary Addition and Binary Subtraction.",
                "2.5 Signed number representation using Sign-Magnitude and 1's Complement.",
                "2.6 Signed number representation and subtraction using 2's Complement.",
                "2.7 Character encoding schemes: ASCII (7/8-bit) and Unicode (UTF-8/UTF-16), and data representation in computer memory."
            ]),
            ("Unit 3.0: Computer Software and Operating Systems (9 hrs)", [
                "3.1 Definition of Software and classification into System Software and Application Software.",
                "3.2 System Software components: Operating Systems, Device Drivers, System Utilities, Language Translators.",
                "3.3 Application Software classification based on usage (General-purpose vs Specific-purpose).",
                "3.4 Operating System (OS) definition, kernel role, and primary objectives (convenience, efficiency, resource management).",
                "3.5 Types of Operating Systems: Batch OS, Time-Sharing (Multitasking) OS, Distributed OS, and Real-Time OS (Hard & Soft RTOS).",
                "3.6 Core OS Functions: Process Management (PCB, scheduling, deadlock) and Memory Management (paging, segmentation, virtual memory).",
                "3.7 User Interfaces: Command Line Interface (CLI) vs Graphical User Interface (GUI) usability and efficiency.",
                "3.8 File System organization and feature comparison of Windows (NTFS), Linux (ext4), and macOS (APFS)."
            ]),
            ("Unit 4.0: Computer Networks and Internet Basics (9 hrs)", [
                "4.1–4.2 Fundamentals of Computer Networking and benefits (resource sharing, reliability, scalability).",
                "4.3–4.4 Data Transmission components (Sender, Receiver, Message, Medium, Protocol) and Transmission Media: Twisted Pair, Coaxial Cable, Optical Fiber, Radio/Microwave/Infrared.",
                "4.5 Classification by scale: Local Area Network (LAN), Metropolitan Area Network (MAN), Wide Area Network (WAN).",
                "4.6 Network Topologies: Star, Bus, Ring, and Mesh topologies (pros, cons, fault tolerance) and Communication Protocols.",
                "4.7 Network Hardware Devices: Hub, Switch, Router, Modem, Gateway, and Wireless Networking (Wi-Fi/Access Points).",
                "4.8–4.9 Internet Basics: IP Addressing (IPv4 vs IPv6), TCP vs UDP, HTTP/HTTPS, FTP, DNS resolution, URL structure, and Client-Server Architecture."
            ]),
            ("Unit 5.0: Emerging Technologies (8 hrs)", [
                "5.1 Internet of Things (IoT): Sensing-Network-Application layer architecture and Smart Home / Smart City applications.",
                "5.2 Cyber Security: CIA Triad (Confidentiality, Integrity, Availability), Malware/Phishing/DoS/MITM threats, and countermeasures (Firewalls, Encryption, MFA).",
                "5.3 Artificial Intelligence (AI): Fundamentals, Intelligent Agents, and engineering applications.",
                "5.4 Machine Learning (ML): Supervised, Unsupervised, and Reinforcement learning paradigms and real-world use cases.",
                "5.5 Blockchain Technology: Distributed Ledger Technology (DLT), Block structure, Cryptographic Hashing (SHA-256), and Decentralization.",
                "5.6 Data Science: Stages of the Data Science Lifecycle (Capture, Clean, Explore, Model, Communicate) and data-driven decision making."
            ])
        ],
        "books": [
            "P. K. Sinha & Priti Sinha — Computer Fundamentals (BPB Publications, 6th Ed., ISBN: 978-8176567527)",
            "Peter Norton — Introduction to Computers (McGraw Hill, 7th Ed., ISBN: 978-0070636774)",
            "Charles M. Gilmore — Data Representation and Computer Logic (McGraw Hill, ISBN: 978-0070245754)",
            "Abraham Silberschatz, Peter B. Galvin, Greg Gagne — Operating System Concepts (Wiley, 10th Ed., ISBN: 978-1119456339)",
            "Behrouz A. Forouzan — Data Communications and Networking (McGraw Hill, 5th Ed., ISBN: 978-0073376226)",
            "Amita Kapoor & Vinay Chopra — IoT for Beginners: Architecture, Principles and Applications (BPB, ISBN: 978-9355510063)",
            "Mayank Bhushan et al. — Fundamentals of Cyber Security (BPB Publications, ISBN: 9789386551559)",
            "Melanie Mitchell — Artificial Intelligence: A Guide for Thinking Humans (Farrar, Straus and Giroux, ISBN: 9780374257835)"
        ]
    },
    "universal-human-values": {
        "code": "100109",
        "title": "Universal Human Values",
        "credits": "2-0-0 (2 Credits)",
        "cos": [
            "CO1: Explain Self-Exploration and Right Understanding for achieving Happiness and Prosperity.",
            "CO2: Explain Right Understanding, Relationship and Physical Facility and analyze the co-existence of Self and Body.",
            "CO3: Identify values in human relationships and explain Harmony in the Society.",
            "CO4: Explain Harmony in Nature, mutual fulfilment among the four orders and co-existence in Existence.",
            "CO5: Explain human values and ethical conduct with reference to Professional Ethics and Universal Human Order."
        ],
        "units": [
            ("Unit 1.0: Self-Exploration, Happiness and Prosperity (5 hrs)", [
                "1.1 Self-Exploration as the process for Value Education: Dialogue between 'what I am' and 'what I really want to be' (Natural Acceptance) and Experiential Validation.",
                "1.2 Basic Human Aspirations: Continuous Happiness (harmony/synergy within) and Prosperity (feeling of having more than required physical facility).",
                "1.3 Right Understanding as the foundation for fulfilling aspirations."
            ]),
            ("Unit 2.0: Relationship, Physical Facility and Human Being (5 hrs)", [
                "2.1 Correct priority order: (1) Right Understanding in the Self, (2) Fulfilment in Relationship, (3) Physical Facility (Animal vs Human consciousness).",
                "2.2 Prevailing notions of Happiness and Prosperity vs Holistic Happiness and Prosperity.",
                "2.3 Human Being as the co-existence of the sentient 'Self' (I — continuous, qualitative needs of trust/respect; activities of desiring, thinking, selecting) and the material 'Body' (temporary, quantitative needs of food/shelter; physico-chemical activities)."
            ]),
            ("Unit 3.0: Values in Human Relationships and Harmony in Society (5 hrs)", [
                "3.1 Nine Foundational Values in Human-Human Relationship: Trust (Vishwas — foundational value), Respect (Samman — right evaluation), Affection, Care, Guidance, Reverence, Glory, Gratitude, and Love (complete value).",
                "3.2 Intention vs Competence in maintaining Trust; Differentiation vs Respect.",
                "3.3 Harmony in Society: Comprehensive Human Goal (Right Understanding & Freedom in every individual, Prosperity in every family, Fearlessness/Trust in society, Co-existence in nature) across five dimensions (Education-Sanskar, Health-Sanyam, Production-Work, Justice-Preservation, Exchange-Storage)."
            ]),
            ("Unit 4.0: Harmony in Nature and Existence (6 hrs)", [
                "4.1 Harmony and self-regulation in Nature.",
                "4.2 Interconnectedness and mutual fulfilment among the Four Orders of Nature: Material Order (Padartha), Pranic/Bio Order (Prana), Animal Order (Jeev), and Human Order (Gyan).",
                "4.3 Existence as Co-existence (Sah-astitva) of mutually interacting units (Submerged in All-Pervasive Space / Shunya).",
                "4.4 Holistic perception of harmony at all four levels of existence (Individual, Family, Society, Nature/Existence)."
            ]),
            ("Unit 5.0: Implications of Holistic Understanding on Professional Ethics (7 hrs)", [
                "5.1 Natural acceptance of human values (Values of material things, relationship values, and character values).",
                "5.2 Definitiveness of Ethical Human Conduct: Values (Mulya), Policy (Niti), and Character (Charitra).",
                "5.3 Basis for Humanistic Education, Humanistic Constitution, and Universal Human Order (Sarvabhaum Vyavastha).",
                "5.4 Competence in Professional Ethics: People-friendly and eco-friendly production systems, holistic technologies, and management models.",
                "5.5 Strategy for transition from the present state to Universal Human Order: (a) At the level of Individual, (b) At the level of Society."
            ])
        ],
        "books": [
            "R. R. Gaur, R. Sangal, G. P. Bagaria — A Foundation Course in Human Values and Professional Ethics (Excel Books)",
            "AICTE Universal Human Values (UHV) Student & Faculty Reference Handbooks"
        ]
    },
    "indian-constitution": {
        "code": "100110",
        "title": "Essence of Indian Constitution",
        "credits": "3-0-0 (0 Credits / Mandatory Audit)",
        "cos": [
            "CO1: List salient features and characteristics of the Constitution of India.",
            "CO2: Follow fundamental rights and duties as a responsible citizen and engineer of the country.",
            "CO3: Explain the relevance of Directive Principles of State Policy and identify their relationship with Fundamental Rights.",
            "CO4: Explain the system of governance under Part-VI.",
            "CO5: Analyze major constitutional amendments in the Constitution."
        ],
        "units": [
            ("Unit 1.0: Constitution and Preamble (8 hrs)", [
                "1.1 Meaning and significance of the Constitution of India as the supreme law of the land.",
                "1.2 Historical perspective of the Constitution of India: Constituent Assembly formation, Drafting Committee, enactment on 26 Nov 1949, enforcement on 26 Jan 1950.",
                "1.3 Salient features and characteristics: Lengthiest written constitution, blend of rigidity and flexibility, federal system with unitary bias, parliamentary form, independent judiciary, secularism, single citizenship.",
                "1.4 Preamble to the Constitution of India: Keywords — Sovereign, Socialist, Secular, Democratic, Republic, Justice, Liberty, Equality, Fraternity."
            ]),
            ("Unit 2.0: Fundamental Rights and Duties (8 hrs)", [
                "2.1 Fundamental Rights under Part-III (Articles 12–35): Right to Equality (Art. 14–18), Right to Freedom (Art. 19–22), Right Against Exploitation (Art. 23–24), Right to Freedom of Religion (Art. 25–28), Cultural and Educational Rights (Art. 29–30), Right to Constitutional Remedies & Writs (Art. 32).",
                "2.2 Fundamental Duties under Part-IVA (Article 51A — 11 duties) and their practical significance for responsible citizens and engineers (environmental protection, scientific temper, safeguarding public property)."
            ]),
            ("Unit 3.0: Directive Principles (8 hrs)", [
                "3.1 Relevance of Directive Principles of State Policy (DPSP) under Part-IV (Articles 36–51) for establishing a Welfare State and relationship/conflicts with Fundamental Rights.",
                "3.2 Classification of DPSP Articles: Socialistic Principles (Art. 38, 39, 39A, 41, 42, 43), Gandhian Principles (Art. 40, 43, 46, 47, 48), and Liberal-Intellectual Principles (Art. 44, 45, 48A, 49, 50, 51)."
            ]),
            ("Unit 4.0: Governance (9 hrs)", [
                "4.1 System of State Governance under Part-VI (Articles 152–237): State Executive (Governor, Chief Minister, State Council of Ministers, Advocate General) and High Courts.",
                "4.2 State Legislature: Unicameral vs Bicameral legislatures; composition, powers, tenure, and comparison between the Legislative Assembly (Vidhan Sabha) and Legislative Council (Vidhan Parishad)."
            ]),
            ("Unit 5.0: Amendments of Constitution (9 hrs)", [
                "5.1 Constitutional Amendment Powers and Procedure under Article 368 (Simple Majority, Special Majority of Parliament, and Special Majority + Ratification by half of the States).",
                "5.2 Analysis of Major Constitutional Amendments: 42nd Amendment (1976 — 'Mini Constitution', Socialist/Secular/Integrity, Fundamental Duties), 44th Amendment (1978 — Right to Property made legal right, emergency safeguards), 74th Amendment (1992 — Urban Local Bodies / Municipalities), 76th Amendment (1994 — Ninth Schedule reservation protection), 86th Amendment (2002 — Article 21A Right to Education), and 91st Amendment (2003 — 15% cap on Council of Ministers size & anti-defection strengthening)."
            ])
        ],
        "books": [
            "D. D. Basu — Introduction to the Constitution of India (LexisNexis)",
            "M. Laxmikanth — Indian Polity (McGraw Hill Education)",
            "Subhash C. Kashyap — Our Constitution (National Book Trust)"
        ]
    },
    "basics-of-electrical-electronics": {
        "code": "100111",
        "title": "Basics of Electrical & Electronics Engineering",
        "credits": "3-0-0 (3 Credits)",
        "cos": [
            "CO1: Apply fundamental electrical laws to analyse DC circuits.",
            "CO2: Analyse the performance of AC circuits.",
            "CO3: Interpret the applications of basic electrical machines.",
            "CO4: Analyse the characteristics of semiconductor devices such as diodes and transistors for rectifiers, regulators, and amplifiers.",
            "CO5: Explain and apply fundamentals of digital/analog electronics, measurement, sensors, power systems, and electrical safety."
        ],
        "units": [
            ("Unit 1.0: Basic Electrical Circuits (8 hrs)", [
                "1.1 Electrical Circuit Elements: Resistance (R), Inductance (L), Capacitance (C); Active vs Passive elements.",
                "1.2 Classification of Elements: Unilateral vs Bilateral; Linear vs Nonlinear elements.",
                "1.3 Basic Circuit Laws: Ohm's Law (V = IR), Kirchhoff's Current Law (KCL: ΣI = 0), and Kirchhoff's Voltage Law (KVL: ΣV = 0).",
                "1.4 Circuit Configurations: Series and parallel combinations, ideal & practical voltage/current sources, source transformation.",
                "1.5 Circuit Analysis Methods: Mesh Analysis and Nodal Analysis.",
                "1.6 Network Transformations: Voltage Divider Rule, Current Divider Rule, and Star-Delta (Y-Δ) Transformation."
            ]),
            ("Unit 2.0: A.C. Circuits (8 hrs)", [
                "2.1 Signals and Waveforms: Sinusoidal, square, triangular, and ramp signals.",
                "2.2 AC Quantities: Instantaneous value, Peak/Maximum value (Vm), Average value (2Vm/π), and RMS value (Vm/√2).",
                "2.3 Waveform Factors: Peak Factor / Crest Factor (1.414) and Form Factor (1.11) of sinusoidal waves.",
                "2.4 Phase & Phasors: Phase difference, lagging/leading/in-phase quantities, rectangular and polar phasor algebra.",
                "2.5 AC Circuit Parameters: Impedance (Z = R + jX), Admittance (Y), Power Factor (cosφ = R/Z), and Power Triangle (Active Power P = VI cosφ, Reactive Power Q = VI sinφ, Apparent Power S = VI).",
                "2.6 Three-Phase Systems: Necessity, advantages over single-phase, phase sequence, and balanced/unbalanced Star and Delta loads."
            ]),
            ("Unit 3.0: Basic Electrical Machines (8 hrs)", [
                "3.1 Electromagnetic Principles: Faraday's Law of Electromagnetic Induction, Lenz's Law, Self-Inductance (L) and Mutual Inductance (M).",
                "3.2 DC Machines: Construction (yoke, poles, armature, commutator, brushes), working principle of DC Generator & DC Motor, classification (Series, Shunt, Compound), and applications.",
                "3.3 Single-Phase Transformers: Necessity, principle of mutual induction, core/shell construction, and E.M.F. Equation (E = 4.44 f N Φm).",
                "3.4 Transformer Performance: Voltage transformation ratio, current ratio, and Voltage Regulation.",
                "3.5–3.6 Induction Motors & Applications: Working principle of 3-phase (rotating magnetic field, slip) and 1-phase induction motors, and fractional horsepower motor applications."
            ]),
            ("Unit 4.0: Semiconductor Devices (8 hrs)", [
                "4.1 Semiconductor Materials: Intrinsic and Extrinsic (N-type and P-type) semiconductors.",
                "4.2 p-n Junction Diode: Depletion layer, barrier potential, Forward Bias and Reverse Bias V-I characteristics.",
                "4.3 Diode Behavior: Temperature effects and Zener vs Avalanche Breakdown mechanisms.",
                "4.4 Diode Applications: Half-Wave Rectifier, Full-Wave (Center-tapped & Bridge) Rectifier, Capacitor Filters, and Zener Diode as Shunt Voltage Regulator.",
                "4.5–4.6 Bipolar Junction Transistor (BJT): PNP and NPN construction, operating regions (Active, Cutoff, Saturation), Common Emitter (CE) amplifier configuration, and BJT as a Switch."
            ]),
            ("Unit 5.0: Fundamentals of Digital, Analog Electronics, Measurement & Electrical Safety (10 hrs)", [
                "5.1 Number Systems: Binary, Octal, Decimal, and Hexadecimal systems; Binary addition and basic operations.",
                "5.2 Digital Logic: Basic logic gates (AND, OR, NOT, XOR, XNOR), Universal gates (NAND, NOR), and Boolean algebra laws.",
                "5.3 Display & ICs: LED operation, Seven-Segment Display (Common Anode & Common Cathode) truth tables, and overview of Digital/Analog ICs.",
                "5.4 Voltage Regulators & Instruments: IC 7805 (+5V) and IC 7912 (-12V) linear regulators; Digital Multimeter and Cathode Ray Oscilloscope (CRO) applications.",
                "5.5 Sensors & Power System Layout: Sensors vs Transducers (active/passive); Generation, Transmission, and Distribution of electrical power.",
                "5.6–5.7 Electrical Safety & Earthing: Protection against electrical hazards, working of Fuse, MCB (Miniature Circuit Breaker), MCCB (Molded Case Circuit Breaker), and purpose/methods of Earthing (Plate and Pipe earthing)."
            ])
        ],
        "books": [
            "D. P. Kothari & I. J. Nagrath — Basic Electrical Engineering (McGraw-Hill, 2019, ISBN: 978-9353165727)",
            "Robert L. Boylestad & Louis Nashelsky — Electronic Devices and Circuit Theory (Pearson, ISBN: 978-1292025636)",
            "M. Morris Mano — Digital Logic and Computer Design (Pearson India, ISBN: 978-9332586048)",
            "P. S. Bimbhra — Electrical Machinery (Khanna Publishers, 2024, ISBN: 978-9389139105)",
            "A. K. Sawhney — A Course in Electrical and Electronic Measurements and Instrumentation (Dhanpat Rai & Co., 19th Ed., ISBN: 978-8177001006)",
            "Massimo Mitolo — Electrical Safety of Low Voltage Systems (McGraw-Hill, ISBN: 978-0071508186)",
            "Charles K. Alexander & Matthew N. O. Sadiku — Fundamentals of Electric Circuits (McGraw-Hill, 7th Ed., ISBN: 978-9355320162)"
        ]
    },
    "engineering-physics-lab": {
        "code": "100104P",
        "title": "Engineering Physics Lab",
        "credits": "0-0-2 (1 Credit)",
        "cos": [
            "CO1 & CO2: Measure wavelength, radius of curvature, resolving power, specific rotation, and numerical aperture in optical systems.",
            "CO3: Measure dielectric constant of given dielectric materials.",
            "CO4: Determine Planck's constant and electron beam wavelength.",
            "CO5: Characterize p-n junction diodes, Hall effect, energy band gap, and size-dependent absorption of nanoparticles."
        ],
        "units": [
            ("Experiments LE-1 to LE-4: Wave Optics", [
                "LE-1: Diffraction Grating (LSO 1.1) — Measure the wavelength of a given light source using a plane diffraction grating (Formula: (a+b) sinθ = nλ).",
                "LE-2: Newton's Ring Experiment (LSO 1.2, 1.3) — Measure the wavelength of a monochromatic sodium light source and the radius of curvature of a plano-convex lens (Formula: λ = (D_{m+p}² - D_m²)/(4pR)).",
                "LE-3: Resolving Power of Telescope (LSO 1.4) — Determine the practical and theoretical resolving power of a given telescope using a rectangular adjustable slit.",
                "LE-4: Polarimeter (LSO 1.5) — Determine the specific rotation (S = θ / (l·c)) of cane sugar solution using a half-shade polarimeter."
            ]),
            ("Experiments LE-5 to LE-8: Fiber Optics, Dielectrics & Quantum Mechanics", [
                "LE-5: Numerical Aperture of Optical Fiber (Virtual Lab, LSO 2.1) — Determine the Numerical Aperture (NA = sin θ_max = D / √(4L² + D²)) of a given optical fiber.",
                "LE-6: Dielectric Constant (LSO 3.1) — Measure the dielectric constant (K = C_d / C_0) of given solid/liquid dielectric materials.",
                "LE-7: Measurement of Planck's Constant (LSO 4.1) — Determine Planck's constant (h = e · ΔV_0 / Δν) using a photoelectric cell and optical filters.",
                "LE-8: Stern-Gerlach / Electron Beam Experiment (Virtual Lab, LSO 4.2) — Determine the de-Broglie wavelength of an electron beam and study spin quantization."
            ]),
            ("Experiments LE-9 to LE-12: Semiconductors & Nanomaterials", [
                "LE-9: p-n Junction Diode (LSO 5.1) — Plot and analyze the Forward and Reverse Bias I-V characteristics of a p-n junction diode and find knee voltage & dynamic resistance.",
                "LE-10: Hall Effect Experiment (LSO 5.2) — Measure the Hall voltage, calculate the Hall coefficient (R_H), and determine hole/electron carrier density in a semiconductor.",
                "LE-11: Energy Band Gap Measurement (LSO 5.3) — Use the Four-Probe Method to measure temperature-dependent resistivity and calculate the forbidden energy band gap (E_g) of a semiconductor.",
                "LE-12: Nanoparticle Optical Absorption (LSO 5.4) — Demonstrate the shift in optical absorption peak (quantum confinement effect) on changing the size of nanoparticles."
            ])
        ],
        "books": [
            "S. K. Roy — Physics Practical for Engineers (Novelty Publication, 1st Ed., 2018)"
        ]
    },
    "electrical-electronics-lab": {
        "code": "100111P",
        "title": "Basics of Electrical & Electronics Engineering Lab",
        "credits": "0-0-2 (1 Credit)",
        "cos": [
            "CO1: Verify Ohm's Law, KVL, KCL, and voltage/current division rules experimentally.",
            "CO2: Demonstrate power factor improvement of a single-phase load using a capacitor.",
            "CO3: Test single-phase transformer ratios and identify main parts of DC and induction machines.",
            "CO4: Characterize P-N junction diodes, rectifiers, Zener voltage regulators, and CE BJT circuits.",
            "CO5 & CO6: Construct logic gates using universal gates, use CRO & Megger, and demonstrate wiring, earthing, and protection devices."
        ],
        "units": [
            ("Experiments LE-1 to LE-5: DC/AC Circuits & Electrical Machines", [
                "LE-1: Active/Passive Components & Ohm's Law (LSO 1.1, 1.2) — Identify resistors, inductors, capacitors, and sources, and plot V vs I to verify Ohm's Law.",
                "LE-2: Kirchhoff's Laws & Divider Rules (LSO 2.1, 2.2) — Verify KVL and KCL in series/parallel DC networks and verify Voltage and Current Division experimentally.",
                "LE-3: Power Factor Improvement (LSO 3.1, 3.2) — Observe low power factor in an inductive single-phase load and improve cosφ using a shunt capacitor.",
                "LE-4: Single-Phase Transformer Ratios (LSO 4.1, 4.2) — Measure primary/secondary voltages and currents to verify the voltage ratio and turns ratio (V1/V2 = N1/N2).",
                "LE-5: Cut-Section Models of Electrical Machines (LSO 5.1, 5.2) — Identify stator, rotor, commutator, slip rings, field windings, and brushes in DC and Induction machines."
            ]),
            ("Experiments LE-6 to LE-10: Analog & Digital Electronics", [
                "LE-6: P-N Junction Diode V-I Characteristics (LSO 6.1, 6.2) — Record and plot forward and reverse bias V-I readings of a silicon/germanium diode.",
                "LE-7: Half-Wave and Full-Wave Rectifiers (LSO 7.1, 7.2) — Verify rectifier output waveforms and calculate ripple factor with and without a capacitor filter.",
                "LE-8: Zener Diode Voltage Regulator (LSO 8.1, 8.2) — Analyze line regulation and load regulation of a Zener diode shunt regulator.",
                "LE-9: Common Emitter (CE) BJT Characterization (LSO 9.1, 9.2) — Plot input (I_B vs V_BE) and output (I_C vs V_CE) characteristics of an NPN transistor in CE mode.",
                "LE-10: Universal Logic Gates Implementation (LSO 10.1, 10.2) — Construct AND, OR, NOT, and XOR gates using only NAND gates and only NOR gates and verify truth tables."
            ]),
            ("Experiments LE-11 to LE-16: CRO, Protection Devices, Wiring & Earthing", [
                "LE-11: CRO Signal Measurements (LSO 11.1, 11.2) — Measure peak-to-peak amplitude, time period (T), and frequency (f = 1/T) of AC waveforms using a Cathode Ray Oscilloscope.",
                "LE-12: Electrical Cables, Wires & Fuses (LSO 12.1, 12.2) — Identify wire gauges, insulation types, and current ratings of cables and fuses.",
                "LE-13: Fuse, MCB, and MCCB Operation (LSO 13.1, 13.2) — Study construction and evaluate tripping/blowing behavior under overload and fault conditions.",
                "LE-14: Earthing Techniques & Electrical Safety (LSO 14.1, 14.2) — Demonstrate standard earthing installations and electrical shock/hazard safety practices.",
                "LE-15: Domestic Wiring of Lamp & Fan (LSO 15.1, 15.2) — Wire a single lamp and ceiling fan with regulator controlled by switches and protected by a fuse/MCB.",
                "LE-16: Megger & Earth Resistance Testing (LSO 16.1, 16.2) — Safely operate a Megger for insulation testing and measure earth resistance for grounding verification."
            ])
        ],
        "books": [
            "D. P. Kothari & I. J. Nagrath — Basic Electrical Engineering (McGraw-Hill)",
            "A. K. Sawhney — A Course in Electrical and Electronic Measurements and Instrumentation"
        ]
    },
    "programming-lab": {
        "code": "100112P",
        "title": "Programming for Problem Solving Lab",
        "credits": "0-0-2 (1 Credit)",
        "cos": [
            "CO1: Develop basic C programs to solve given problems by developing algorithms.",
            "CO2: Implement structured programming constructs to solve computational problems in C.",
            "CO3: Apply advanced memory and data management techniques to design efficient C programs.",
            "CO4: Design object-oriented C++ programs using foundational OOP principles.",
            "CO5: Apply advanced OOP concepts (inheritance, polymorphism, exception handling, templates) to build robust software solutions."
        ],
        "units": [
            ("Experiments LE-1 to LE-5: Structured Programming in C", [
                "LE-1: Algorithmic Logic & Basic I/O (LSO 1.1–1.3) — Write a C program to calculate the area of a circle, triangle, and rectangle using appropriate data types and explicit type casting, accompanied by a flowchart.",
                "LE-2: Decision Making Systems (LSO 2.1, 2.2) — Develop a Student Grading and Classification System in C using an if-else ladder (for marks grading) and a switch-case statement (to classify eligible fee waivers by category).",
                "LE-3: Iterative Problem Solving (LSO 3.1, 3.2) — Write a C program using while and for loops to: (i) Find all prime numbers between 1 and N, (ii) Generate the Fibonacci sequence up to N terms.",
                "LE-4: 1-D Array Operations (LSO 4.1) — Write a C program to: (i) Find the maximum and minimum element in an array using Linear Search, (ii) Calculate the average of elements in a 1-D array.",
                "LE-5: Matrix Manipulation with 2-D Arrays (LSO 5.1) — Write a C program to perform: (i) Matrix Multiplication of two 2-D arrays, (ii) Transpose of a matrix."
            ]),
            ("Experiments LE-6 to LE-10: Pointers, Recursion, Structures & Files in C", [
                "LE-6: Pointer Arithmetic & Strings (LSO 6.1, 6.2) — Write a C program to: (i) Reverse a string using pointer-based swapping, (ii) Count vowels and consonants in a string using pointers.",
                "LE-7: Recursion vs. Iteration (LSO 7.1, 7.2) — Write a C program using both iterative and recursive functions to compare logic flow and time/space complexity for: (i) Factorial of N, (ii) Greatest Common Divisor (GCD) of two numbers.",
                "LE-8: Parameter Passing Mechanisms (LSO 8.1, 8.2) — Develop a C program that swaps two numbers and updates array elements using both Call by Value and Call by Reference (pointers).",
                "LE-9: User-Defined Data Types (LSO 9.1–9.3) — Create an 'Employee Payroll System' using Structures and Unions in C to store employee details and compare their memory allocation using the sizeof operator.",
                "LE-10: File Handling Operations (LSO 10.1–10.3) — Write a C program to create a text file and: (i) Write structured student records, (ii) Read and display all student records on the console, (iii) Search and extract specific records by keyword/roll number."
            ]),
            ("Experiments LE-11 to LE-17: Object-Oriented Programming in C++", [
                "LE-11: Classes, Objects & Encapsulation (LSO 11.1–11.3) — Design a C++ BankAccount class with private balance data member and public deposit(), withdraw(), and display() member functions across multiple objects.",
                "LE-12: Constructors & Memory Management (LSO 12.1–12.3) — Implement a C++ String class utilizing Default, Parameterized, and Copy Constructors along with dynamic memory allocation (new) and a Destructor (delete[]).",
                "LE-13: Static Members & Friend Functions (LSO 13.1–13.3) — Write a C++ program that uses a static data member & static function to track the count of objects created and a friend function to compare private data of two different classes.",
                "LE-14: Implementation of Inheritances (LSO 14.1) — Write a C++ program demonstrating arithmetic operations across (i) Single, (ii) Multiple, (iii) Multilevel, (iv) Hierarchical, and (v) Hybrid/Virtual Inheritance.",
                "LE-15: Polymorphism & Abstract Classes (LSO 15.1–15.3) — Write C++ programs to: (i) Create an Abstract Class Shape with pure virtual function draw() = 0, (ii) Find area of shapes using Function Overloading, (iii) Add two Complex numbers using Operator Overloading (+).",
                "LE-16: Robust Error Management (LSO 16.1–16.3) — Write a C++ program demonstrating Exception Handling using try, catch, and throw blocks for 'Division by Zero' and 'Negative Stock Input'.",
                "LE-17: Template Implementation (LSO 17.1) — Write a C++ program using a Function Template to find the maximum of two values and a Class Template (Pair<T1, T2>) to store values of any data type."
            ])
        ],
        "books": [
            "Brian W. Kernighan & Dennis M. Ritchie — The C Programming Language (Prentice Hall)",
            "E. Balagurusamy — Programming in ANSI C & Object Oriented Programming with C++ (McGraw Hill)",
            "Bjarne Stroustrup — The C++ Programming Language (Addison-Wesley)"
        ]
    }
}

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title} | {course_title}</title>
  <link rel="stylesheet" href="../style.css" />
  <style>
    .sub-nav {{ display:flex; flex-wrap:wrap; gap:0.5rem; margin:1.25rem 0; }}
    .sub-nav a {{ padding:0.5rem 0.9rem; border-radius:0.5rem; background:var(--surface); border:1px solid var(--border); color:var(--text); text-decoration:none; font-weight:600; font-size:0.9rem; }}
    .sub-nav a.active, .sub-nav a:hover {{ background:var(--primary); color:#fff; border-color:var(--primary); }}
    .content-box {{ background:var(--surface); border:1px solid var(--border); border-radius:1rem; padding:1.5rem; margin-bottom:1.25rem; box-shadow:var(--shadow); }}
    .content-box h2 {{ margin-bottom:0.75rem; color:var(--primary); }}
    .content-box ul {{ padding-left:1.25rem; }}
    .content-box li {{ margin-bottom:0.6rem; }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="container hero-inner">
      <div>
        <span class="badge">{code} • {credits}</span>
        <h1>{course_title}</h1>
        <p>{page_title}</p>
      </div>
      <div>
        <a href="../index.html" class="btn-secondary" style="text-decoration:none;">⬅ Back to Main Portal</a>
      </div>
    </div>
  </header>
  <main class="container">
    <nav class="sub-nav">
      <a href="index.html">🏠 Overview</a>
      <a href="syllabus.html">📋 Syllabus</a>
      <a href="notes.html">📚 All Notes</a>
      {unit_nav}
      <a href="references.html">📖 References</a>
    </nav>
    {body_content}
  </main>
</body>
</html>
"""

def build_all():
    for folder, data in SUBJECTS.items():
        os.makedirs(folder, exist_ok=True)
        is_theory = len(data["units"]) == 5

        unit_nav = ""
        if is_theory:
            unit_nav = " ".join(
                [f'<a href="notes-unit{i}.html">Unit {i}</a>' for i in range(1, 6)]
            )

        # 1. Fix any existing HTML files in this folder that wrongly link to ../ai/ or ai/
        if folder != "ai":
            for fname in os.listdir(folder):
                fpath = os.path.join(folder, fname)
                if os.path.isfile(fpath) and fname.endswith(".html"):
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        html = f.read()
                    fixed = re.sub(r'(\.\./)?ai/', '', html)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(fixed)

        # 2. Generate Overview (index.html)
        cos_html = "<div class='content-box'><h2>🎯 Course Outcomes (COs)</h2><ul>" + "".join(
            [f"<li>{co}</li>" for co in data["cos"]]
        ) + "</ul></div>"
        units_overview = "<div class='content-box'><h2>📂 Quick Access Units</h2><ul>"
        for idx, (u_title, _) in enumerate(data["units"], 1):
            link = f"notes-unit{idx}.html" if is_theory else f"notes.html#part-{idx}"
            units_overview += f'<li><a href="{link}" style="color:var(--primary);font-weight:600;">{u_title}</a></li>'
        units_overview += "</ul></div>"

        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(PAGE_TEMPLATE.format(
                page_title="Course Hub & Quick Access",
                course_title=data["title"],
                code=data["code"],
                credits=data["credits"],
                unit_nav=unit_nav,
                body_content=cos_html + units_overview
            ))

        # 3. Generate Official Syllabus (syllabus.html)
        syl_blocks = cos_html
        for idx, (u_title, topics) in enumerate(data["units"], 1):
            syl_blocks += f"<div class='content-box'><h2>{u_title}</h2><ul>" + "".join(
                [f"<li>{t}</li>" for t in topics]
            ) + "</ul></div>"
        with open(os.path.join(folder, "syllabus.html"), "w", encoding="utf-8") as f:
            f.write(PAGE_TEMPLATE.format(
                page_title="Official Syllabus (Batch 2026–2030)",
                course_title=data["title"],
                code=data["code"],
                credits=data["credits"],
                unit_nav=unit_nav,
                body_content=syl_blocks
            ))

        # 4. Generate All Notes / Lab Manual (notes.html)
        notes_blocks = ""
        for idx, (u_title, topics) in enumerate(data["units"], 1):
            unit_btn = f'<p style="margin-top:0.75rem;"><a href="notes-unit{idx}.html" style="color:var(--primary);font-weight:700;">➡ Open Dedicated Unit {idx} Page</a></p>' if is_theory else ""
            notes_blocks += f"<div id='part-{idx}' class='content-box'><h2>{u_title}</h2><ul>" + "".join(
                [f"<li>{t}</li>" for t in topics]
            ) + f"</ul>{unit_btn}</div>"
        with open(os.path.join(folder, "notes.html"), "w", encoding="utf-8") as f:
            f.write(PAGE_TEMPLATE.format(
                page_title="Complete Study Notes & Lab Guide",
                course_title=data["title"],
                code=data["code"],
                credits=data["credits"],
                unit_nav=unit_nav,
                body_content=notes_blocks
            ))

        # 5. Generate Individual Unit Pages (notes-unit1.html .. notes-unit5.html)
        if is_theory:
            for idx, (u_title, topics) in enumerate(data["units"], 1):
                unit_path = os.path.join(folder, f"notes-unit{idx}.html")
                if folder in ["ai", "basics-of-electrical-electronics"] and os.path.exists(unit_path):
                    continue  # Preserves your existing custom unit notes in AI & BEEE
                unit_body = f"<div class='content-box'><h2>{u_title}</h2><ul>" + "".join(
                    [f"<li>{t}</li>" for t in topics]
                ) + "</ul></div>"
                with open(unit_path, "w", encoding="utf-8") as f:
                    f.write(PAGE_TEMPLATE.format(
                        page_title=f"Unit {idx} Study Notes",
                        course_title=data["title"],
                        code=data["code"],
                        credits=data["credits"],
                        unit_nav=unit_nav,
                        body_content=unit_body
                    ))

        # 6. Generate References (references.html)
        ref_html = "<div class='content-box'><h2>📖 Recommended Textbooks & References</h2><ul>" + "".join(
            [f"<li>{b}</li>" for b in data["books"]]
        ) + "</ul></div>"
        with open(os.path.join(folder, "references.html"), "w", encoding="utf-8") as f:
            f.write(PAGE_TEMPLATE.format(
                page_title="Reference Books & Reading List",
                course_title=data["title"],
                code=data["code"],
                credits=data["credits"],
                unit_nav=unit_nav,
                body_content=ref_html
            ))

    print("✅ All 10 subject folders updated and Quick Access links fixed!")

if __name__ == "__main__":
    build_all()