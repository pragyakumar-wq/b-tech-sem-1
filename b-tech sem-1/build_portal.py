import os
import re

# Complete Syllabus Data from B.Tech 1st Semester Group-A (Batch 2026-2030)
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
                "1.2 Consistency of System of Linear Equations.",
                "1.3 Eigenvalues & Eigenvectors, Cayley-Hamilton Theorem (and finding integral powers/inverse of a matrix).",
                "1.4 Similarity of Matrices & Diagonalization of Square Matrices. Quadratic Form, Canonical Form of Matrices."
            ]),
            ("Unit 2.0: Differential Calculus: Single Variable (8 hrs)", [
                "2.1 Higher order derivatives; Successive differentiation and Leibnitz's Theorem.",
                "2.2 Mean Value Theorems (Rolle's, Lagrange's, Cauchy).",
                "2.3 Indeterminate Forms; L'Hospital's Rule.",
                "2.4 Tangents & Normals of Algebraic & Polar Curves, Curvature."
            ]),
            ("Unit 3.0: Differential Calculus: Several Variables (9 hrs)", [
                "3.1 Partial differentiations; Euler's theorems on homogeneous functions.",
                "3.2 Limit, Continuity and differentiability of functions of Several Variables.",
                "3.3 Taylor's theorem with various forms of remainders, Maclaurin's theorem and related problems.",
                "3.4 Maxima & Minima for functions of several variables; Lagrange's Multiplier Method."
            ]),
            ("Unit 4.0: Integral Calculus (9 hrs)", [
                "4.1 Differentiation under the integral sign; Leibnitz's rule.",
                "4.2 Double integral; Change the order of integration; Evaluation of double integration by changing into polar coordinates.",
                "4.3 Triple Integral; Evaluation of Triple integral in Spherical Polar & Cylindrical polar coordinates.",
                "4.4 Beta, Gamma, Elliptic integrals; Relation between Beta & Gamma functions, General Properties."
            ]),
            ("Unit 5.0: Vector Calculus (8 hrs)", [
                "5.1 Scalar and vector valued functions; Gradient, Divergence and Curl and their geometrical/physical significance; Tangent plane; Directional derivative.",
                "5.2 Line, surface and volume integrals.",
                "5.3 Statement of Green's, Stokes' and Gauss divergence theorems — verification and evaluation of vector integrals."
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
                "1.1 Interference, Division of amplitude, Newton's Ring experiment, Michelson interferometer.",
                "1.2 Diffraction, Fraunhofer diffraction, Single and double slit, & Circular aperture.",
                "1.3 Diffraction Grating (n-slit Fraunhofer diffraction pattern).",
                "1.4 Rayleigh criterion, resolving power of telescope.",
                "1.5 Polarization, double-refracting crystal, Nicol prism."
            ]),
            ("Unit 2.0: Lasers and Optical Fiber (8 hrs)", [
                "2.1 Characteristics of laser light, Einstein's A & B coefficients, Population inversion, pumping mechanism, Optical resonator.",
                "2.2 Ruby laser, He-Ne laser, and Semiconductor laser.",
                "2.3 Structure of optical fibre, Basic principles (TIR, Acceptance angle and Numerical Aperture), Types of optical fibres.",
                "2.4 Propagation mechanism of light in fibre, Attenuation in optical fibres.",
                "2.5 Applications of optical fibres, Fibre optic sensors in communications, medical, defense, and industries."
            ]),
            ("Unit 3.0: Electromagnetism & Propagation of Waves (8 hrs)", [
                "3.1 Electric fields, Gauss' Law, Dielectrics and Capacitors.",
                "3.2 Magnetic fields & Magnetic Materials (Dia-, Para-, and Ferromagnetic classification).",
                "3.3 Maxwell's Equations in integral and differential form with physical significance.",
                "3.4 Electromagnetic waves & Poynting Theorem (magnitude and direction of energy transport)."
            ]),
            ("Unit 4.0: Quantum Mechanics (8 hrs)", [
                "4.1 Introduction to Quantum Mechanics.",
                "4.2 De-Broglie hypothesis, Heisenberg uncertainty principle.",
                "4.3 Wave function and its characteristics & physical significance.",
                "4.4 Schrödinger's equation (time-dependent and time-independent).",
                "4.5 Particle in a 1D infinite potential box: Energy Eigenvalues and Eigenfunctions.",
                "4.6 Potential barrier and Quantum Tunneling."
            ]),
            ("Unit 5.0: Semiconductors & Nano-materials (10 hrs)", [
                "5.1 Introduction, Band structures of metal, semiconductor and insulator.",
                "5.2 Intrinsic and extrinsic semiconductors, P-type and N-type, Diffusion, Drift current density and Fermi level.",
                "5.3 Photodiode, P-N junction transistor, LED.",
                "5.4 Hall effect and significance of Hall coefficient.",
                "5.5 Solar cell and its I-V characteristics.",
                "5.6 Introduction to nanoscience & nanotechnology, significance of nanoscale.",
                "5.7 Unique properties: Bulk vs nanomaterials, large surface-to-volume ratio, change in band gap, optical/electrical/mechanical properties.",
                "5.8 Classification of Nanostructured Materials: 0D (Quantum Dot), 1D (Nanowire)."
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
                "1.3 Intelligent agents: agent-environment interaction, PEAS (Performance measure, Environment, Actuators, Sensors) description.",
                "1.4 Types of environments (observable, deterministic, episodic, static, discrete, single/multi-agent).",
                "1.5 Types of agents: simple reflex, model-based, goal-based, utility-based, learning agents.",
                "1.6 Overview of AI application domains across engineering disciplines."
            ]),
            ("Unit 2.0: Problem Solving by Search (9 hrs)", [
                "2.1 Problem formulation and state-space representation.",
                "2.2 Uninformed search: BFS, DFS, Uniform Cost Search, Depth-Limited and Iterative Deepening Search.",
                "2.3 Informed (heuristic) search: Greedy Best-First Search, A* algorithm.",
                "2.4 Heuristic function design, admissibility and consistency.",
                "2.5 Local search algorithms: Hill Climbing, Simulated Annealing.",
                "2.6 Adversarial search: Minimax algorithm, Alpha-Beta pruning.",
                "2.7 Constraint Satisfaction Problems (CSP): concept and backtracking overview."
            ]),
            ("Unit 3.0: Knowledge Representation and Reasoning (8 hrs)", [
                "3.1 Knowledge representation issues; Propositional logic syntax and semantics.",
                "3.2 Inference in propositional logic: Resolution.",
                "3.3 First-order predicate logic syntax and quantifiers.",
                "3.4 Inference in first-order logic: Forward chaining, Backward chaining, Resolution.",
                "3.5 Structured knowledge representation: Semantic networks and Frames.",
                "3.6 Rule-based (production) systems."
            ]),
            ("Unit 4.0: Reasoning Under Uncertainty (7 hrs)", [
                "4.1 Sources of uncertainty; review of basic probability theory.",
                "4.2 Bayes' theorem and its application to AI reasoning.",
                "4.3 Bayesian networks: representation and manual inference.",
                "4.4 Introduction to fuzzy logic, fuzzy sets, and fuzzy operations.",
                "4.5 Certainty factors and rule-based uncertainty."
            ]),
            ("Unit 5.0: Introduction to Machine Learning and AI Applications (10 hrs)", [
                "5.1 Machine learning paradigms: Supervised, Unsupervised, Reinforcement learning.",
                "5.2 Overview of regression and classification concepts (Linear Regression, k-NN, Decision Trees).",
                "5.3 Overview of clustering concept (k-Means).",
                "5.4 Introduction to Artificial Neural Networks (ANN): Perceptron and basic architecture.",
                "5.5 Overview of Natural Language Processing (NLP): concept and applications.",
                "5.6 Overview of Computer Vision: concept and applications.",
                "5.7 Expert systems: architecture and applications.",
                "5.8 Robotics and AI: overview of intelligent robotic systems.",
                "5.9 Ethics, bias, responsible AI, societal impact, and AI for Sustainable Development Goals (SDGs)."
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
                "1.1 Classification of computers, Functional units.",
                "1.2 Central Processing Unit (CPU) organization and working (ALU, CU, Instruction Cycle).",
                "1.3 Memory: Architecture, Memory Representation, Memory Hierarchy.",
                "1.4 CPU Registers, Impact of Cache Memory on System Performance.",
                "1.5 Motherboard and its components (Chipset, Buses, Expansion Slots, BIOS/UEFI).",
                "1.6 The Von-Neumann Architecture.",
                "1.7 Machine language, assembly language, high-level programming languages; Compiler vs Interpreter."
            ]),
            ("Unit 2.0: Data Representation (8 hrs)", [
                "2.1 Data Representation & Number Systems (Base-2, Base-8, Base-10, Base-16).",
                "2.2 Conversion between decimal and binary systems.",
                "2.3 Conversion among binary, octal, and hexadecimal systems.",
                "2.4 Binary arithmetic (addition, subtraction).",
                "2.5 Signed number representation (1's complement).",
                "2.6 Signed number representation (2's complement).",
                "2.7 ASCII and Unicode character encoding schemes; Data representation in memory."
            ]),
            ("Unit 3.0: Computer Software and Operating Systems (9 hrs)", [
                "3.1 Introduction to Software, Types of Software.",
                "3.2 System Software (OS, Device Drivers, Utilities, Language Translators).",
                "3.3 Application Software (General purpose vs Tailor-made).",
                "3.4 Operating System (OS) and Objectives of an Operating System.",
                "3.5 Types of OS: Batch, Time-sharing, Distributed, Real-time.",
                "3.6 Functions of OS: Process Management and Memory Management.",
                "3.7 User Interface: Command Line Interface (CLI) vs Graphical User Interface (GUI).",
                "3.8 File system basics & comparison across Windows, Linux, and macOS."
            ]),
            ("Unit 4.0: Computer Networks and Internet Basics (9 hrs)", [
                "4.1 Introduction to Computer Networks & 4.2 Importance of Networking.",
                "4.3 Data Transmission Media (Guided: Twisted Pair, Coaxial, Fiber Optic; Unguided: Radio, Microwave, Infrared).",
                "4.4 Data Transmission in a Network (Simplex, Half-Duplex, Full-Duplex; Serial vs Parallel).",
                "4.5 Network Types: Local Area Network (LAN), Metropolitan Area Network (MAN), Wide Area Network (WAN).",
                "4.6 Network Topologies (Star, Bus, Ring, Mesh) & Communication Protocols.",
                "4.7 Network Devices (Hub, Switch, Router, Modem, Gateway) & Wireless Networking.",
                "4.8 Introduction to Internet: IP Address (IPv4 & IPv6).",
                "4.9 TCP, UDP, HTTP, FTP, DNS, URL, and Client-Server Architecture."
            ]),
            ("Unit 5.0: Emerging Technologies (8 hrs)", [
                "5.1 Internet of Things (IoT): Concept, architecture, and applications (Smart homes, Smart cities).",
                "5.2 Cyber Security: Basic security terminologies, CIA Triad (Confidentiality, Integrity, Availability), Cyber threats & countermeasures.",
                "5.3 Artificial Intelligence (AI): Introduction, AI agents, and applications.",
                "5.4 Machine Learning (ML): Types of learning paradigms and real-world applications.",
                "5.5 Blockchain: Concept of distributed ledger, Blocks, cryptographic hashing, decentralization.",
                "5.6 Data Science: Data Lifecycle and role of data in decision making."
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
                "1.1 Self-Exploration as the process for Value Education (Natural Acceptance and Experiential Validation).",
                "1.2 Continuous Happiness and Prosperity as basic human aspirations.",
                "1.3 Right Understanding as the foundation of human life."
            ]),
            ("Unit 2.0: Relationship, Physical Facility and Human Being (5 hrs)", [
                "2.1 Priority order: Right Understanding, Relationship and Physical Facility.",
                "2.2 Distinguishing between excitement/sensation and Continuous Happiness & Prosperity.",
                "2.3 Human being as a co-existence of the sentient 'Self' (I) and the material 'Body' (needs, activities, and response)."
            ]),
            ("Unit 3.0: Values in Human Relationships and Harmony in Society (5 hrs)", [
                "3.1 Foundational values in human-human relationships: Trust (Vishwas), Respect (Samman), Affection, Care, Guidance, Reverence, Glory, Gratitude, and Love.",
                "3.2 Harmony in the Society: Resolution, Prosperity, Fearlessness (Trust), and Co-existence as comprehensive human goals."
            ]),
            ("Unit 4.0: Harmony in Nature and Existence (6 hrs)", [
                "4.1 Harmony in the Nature.",
                "4.2 Interconnectedness, self-regulation and mutual fulfilment among the Four Orders of Nature (Material, Pranic/Bio, Animal, and Human Order).",
                "4.3 Existence as Co-existence of mutually interacting units submerged in all-pervasive space.",
                "4.4 Holistic perception of harmony at all levels of existence."
            ]),
            ("Unit 5.0: Implications of Holistic Understanding on Professional Ethics (7 hrs)", [
                "5.1 Natural acceptance of human values.",
                "5.2 Definitiveness of Ethical Human Conduct.",
                "5.3 Basis for Humanistic Education, Humanistic Constitution and Humanistic Universal Order.",
                "5.4 Competence in Professional Ethics (eco-friendly and people-friendly production systems).",
                "5.5 Strategy for transition from the present state to Universal Human Order at the level of individual and society."
            ])
        ],
        "books": [
            "R. R. Gaur, R. Sangal, G. P. Bagaria — A Foundation Course in Human Values and Professional Ethics (Excel Books)",
            "AICTE Universal Human Values (UHV-I & UHV-II) Student Handbooks and Reference Material"
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
                "1.1 Meaning of the Constitution of India.",
                "1.2 Historical perspective of the Constitution of India (Constituent Assembly, drafting & enactment).",
                "1.3 Salient features and characteristics of the Constitution of India.",
                "1.4 Preamble to the Constitution of India (Sovereign, Socialist, Secular, Democratic, Republic; Justice, Liberty, Equality, Fraternity)."
            ]),
            ("Unit 2.0: Fundamental Rights and Duties (8 hrs)", [
                "2.1 Fundamental Rights under Part-III (Articles 12–35: Right to Equality, Freedom, Against Exploitation, Freedom of Religion, Cultural & Educational Rights, Constitutional Remedies).",
                "2.2 Fundamental Duties (Part-IVA, Article 51A) and their significance in general and in the engineering profession."
            ]),
            ("Unit 3.0: Directive Principles (8 hrs)", [
                "3.1 Relevance of Directive Principles of State Policy (DPSP) under Part-IV and situations where Directive Principles prevail over Fundamental Rights.",
                "3.2 Different articles of State policies under Part-IV (Socialistic, Gandhian, and Liberal-Intellectual principles, Articles 36–51)."
            ]),
            ("Unit 4.0: Governance (9 hrs)", [
                "4.1 System of Governance under Part-VI (The States: Governor, Chief Minister, Council of Ministers).",
                "4.2 State Legislature: Unicameral & Bicameral legislatures; differentiation between Legislative Assembly (Vidhan Sabha) and Legislative Council (Vidhan Parishad)."
            ]),
            ("Unit 5.0: Amendments of Constitution (9 hrs)", [
                "5.1 Amendment of Constitutional Powers and Procedure (Article 368).",
                "5.2 Major Constitutional Amendments and their impact: 42nd, 44th, 74th, 76th, 86th, and 91st Amendments."
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
                "1.1 Electrical Circuit Elements: Resistance, inductance, and capacitance as active and passive elements.",
                "1.2 Classification of Elements: Unilateral and bilateral; linear and nonlinear elements.",
                "1.3 Basic Circuit Laws: Ohm's law and Kirchhoff's Current Law (KCL) & Voltage Law (KVL).",
                "1.4 Circuit Configurations: Series and parallel circuits, voltage/current sources, source transformation.",
                "1.5 Circuit Analysis Methods: Mesh analysis and Nodal analysis techniques.",
                "1.6 Network Theorems & Transformations: Current divider rule, voltage divider rule, and Star-Delta (Y-Δ) transformation."
            ]),
            ("Unit 2.0: A.C. Circuits (8 hrs)", [
                "2.1 Signals and Waveforms: Common electrical signals and waveform characteristics.",
                "2.2 AC Quantities: Instantaneous, peak, average, and RMS values of alternating signals.",
                "2.3 Waveform Factors: Peak factor and Form factor of sinusoidal waves.",
                "2.4 Phase and Phasors: Phase difference, lagging, leading, in-phase quantities; rectangular and polar phasor forms.",
                "2.5 AC Circuit Parameters: Impedance, admittance, power factor, and power triangle (Active, Reactive, Apparent power).",
                "2.6 Three-Phase Systems: Necessity, advantages, phase sequence, balanced and unbalanced supply/load concepts."
            ]),
            ("Unit 3.0: Basic Electrical Machines (8 hrs)", [
                "3.1 Electromagnetic Principles: Faraday's & Lenz's laws, self-inductance, and mutual inductance.",
                "3.2 DC Machines: Principle of operation, construction, classification, and applications.",
                "3.3 Single-Phase Transformers: Necessity, working principle, construction, and E.M.F. equation.",
                "3.4 Transformer Performance: Voltage ratio, current ratio, and voltage regulation with significance.",
                "3.5 Induction Motors: Single-phase and three-phase induction motors and their working principles.",
                "3.6 Motor Applications: Applications of induction motors and fractional horsepower motors."
            ]),
            ("Unit 4.0: Semiconductor Devices (8 hrs)", [
                "4.1 Semiconductor Materials: Intrinsic and extrinsic semiconductor types.",
                "4.2 p-n Junction Diode: Construction, V-I characteristics, forward bias, and reverse bias operation.",
                "4.3 Diode Behavior: Temperature effects and breakdown mechanisms (Zener and Avalanche breakdown).",
                "4.4 Diode Applications: Half-wave rectifier, Full-wave rectifier, filters, and Zener diode as voltage regulator.",
                "4.5 BJT Fundamentals: PNP and NPN transistors, construction, and operating principles.",
                "4.6 BJT Applications: Common Emitter (CE) configuration as amplifier and transistor as a switch."
            ]),
            ("Unit 5.0: Fundamentals of Digital, Analog Electronics, Measurement & Electrical Safety (10 hrs)", [
                "5.1 Binary, octal, and hexadecimal number systems; binary addition and basic number operations.",
                "5.2 Basic logic gates, universal gates (NAND, NOR), and Boolean algebra.",
                "5.3 LEDs, seven-segment display and truth table; overview of digital and analog integrated circuits.",
                "5.4 Functions and applications of IC 7805 and IC 7912 voltage regulators; features and uses of Multimeter and CRO.",
                "5.5 Fundamentals, types, and uses of sensors and transducers; generation, transmission, and distribution of electrical power.",
                "5.6 Safe handling practices, prevention of electrical hazards; functions and applications of Fuse, MCB, and MCCB.",
                "5.7 Purpose, importance, and methods of earthing systems."
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
                "LE-1: Diffraction Grating — Measure the wavelength of a given light source using a plane diffraction grating (LSO 1.1).",
                "LE-2: Newton's Ring Experiment — Measure the wavelength of a monochromatic light source and radius of curvature of a plano-convex lens (LSO 1.2, 1.3).",
                "LE-3: Resolving Power of Telescope — Determine the resolving power of a given telescope (LSO 1.4).",
                "LE-4: Polarimeter — Determine the specific rotation of cane sugar solution using a polarimeter (LSO 1.5)."
            ]),
            ("Experiments LE-5 to LE-8: Fiber Optics, Dielectrics & Quantum Mechanics", [
                "LE-5: Numerical Aperture of Optical Fiber (Virtual Lab) — Determine the Numerical Aperture of a given optical fiber (LSO 2.1).",
                "LE-6: Dielectric Constant — Measure the dielectric constant of given dielectric materials (LSO 3.1).",
                "LE-7: Measurement of Planck's Constant — Determine the value of Planck's constant using a photocell (LSO 4.1).",
                "LE-8: Stern-Gerlach / Electron Diffraction (Virtual Lab) — Determine the wavelength of a given electron beam (LSO 4.2)."
            ]),
            ("Experiments LE-9 to LE-12: Semiconductors & Nanomaterials", [
                "LE-9: p-n Junction Diode — Determine the I-V characteristics of a given p-n junction diode (LSO 5.1).",
                "LE-10: Hall Effect Experiment — Determine hole and electron density in a given semiconductor (LSO 5.2).",
                "LE-11: Energy Band Gap Measurement — Use the four-probe method to determine resistivity and band gap of a semiconductor (LSO 5.3).",
                "LE-12: Nanoparticle Optical Absorption — Demonstrate the change in absorption of light on changing the size of nanoparticles (LSO 5.4)."
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
                "LE-1: Identification of active and passive components and Ohm's Law verification (LSO 1.1, 1.2).",
                "LE-2: Application of Kirchhoff's Laws (KVL & KCL) and voltage/current division in series and parallel circuits (LSO 2.1, 2.2).",
                "LE-3: Improvement of power factor of a single-phase load using a capacitor (LSO 3.1, 3.2).",
                "LE-4: Determination of voltage and turns ratios of a single-phase transformer (LSO 4.1, 4.2).",
                "LE-5: Identification of main parts of DC machines and induction machines using cut-section models (LSO 5.1, 5.2)."
            ]),
            ("Experiments LE-6 to LE-10: Analog & Digital Electronics", [
                "LE-6: Determination of V-I characteristics of a P-N junction diode in forward and reverse bias (LSO 6.1, 6.2).",
                "LE-7: Performance of half-wave and full-wave rectifiers with and without filters using sinusoidal input (LSO 7.1, 7.2).",
                "LE-8: Analysis of the operation of a voltage regulator using a Zener Diode (LSO 8.1, 8.2).",
                "LE-9: Input and output characterization of Common Emitter (CE) Bipolar Junction Transistor (LSO 9.1, 9.2).",
                "LE-10: Implementation of basic logic gates (AND, OR, NOT, XOR) using Universal gates (NAND & NOR) (LSO 10.1, 10.2)."
            ]),
            ("Experiments LE-11 to LE-16: CRO, Protection Devices, Wiring & Earthing", [
                "LE-11: Measurement of signal amplitude, time period, and frequency using a Cathode Ray Oscilloscope (CRO) (LSO 11.1, 11.2).",
                "LE-12: Identification and safe handling of different types of electrical cables, wires, and fuses (LSO 12.1, 12.2).",
                "LE-13: Operation and evaluation of protection devices: Fuse, MCB, and MCCB under fault/overload conditions (LSO 13.1, 13.2).",
                "LE-14: Demonstration of earthing techniques and electrical safety practices (LSO 14.1, 14.2).",
                "LE-15: Domestic wiring of single lamp and fan with regulator controlled by a switch with fuse/MCB protection (LSO 15.1, 15.2).",
                "LE-16: Handling of Meggers and measurement of insulation and earth resistance (LSO 16.1, 16.2)."
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
                "LE-1: Algorithmic Logic & Basic I/O — C program to calculate area of circle, triangle, and rectangle using appropriate data types and type casting, with flowchart.",
                "LE-2: Decision Making Systems — Student Grading and Classification System using if-else ladder and switch-case (marks grading & fee waiver classification).",
                "LE-3: Iterative Problem Solving — C program using while and for loops to: (i) Find all prime numbers between 1 and N, (ii) Generate Fibonacci sequence up to N.",
                "LE-4: 1-D Array Operations — C program to: (i) Find maximum/minimum element using Linear Search, (ii) Calculate average of elements in a 1-D array.",
                "LE-5: Matrix Manipulation (2-D Arrays) — C program for: (i) Matrix Multiplication, (ii) Transpose of a matrix."
            ]),
            ("Experiments LE-6 to LE-10: Pointers, Recursion, Structures & Files in C", [
                "LE-6: Pointer Arithmetic & Strings — C program to: (i) Reverse a string, (ii) Count vowels and consonants using pointers.",
                "LE-7: Recursion vs. Iteration — C program using both iterative and recursive functions to: (i) Find factorial of N, (ii) Find GCD of two numbers.",
                "LE-8: Parameter Passing Mechanisms — C program that swaps two values and updates an array using both Call by Value and Call by Reference.",
                "LE-9: User-Defined Data Types — Create an 'Employee Payroll System' using Structures and Unions in C and compare memory allocation with sizeof.",
                "LE-10: File Handling Operations — C program to create a text file, write student records, read and display records, and search records by keyword."
            ]),
            ("Experiments LE-11 to LE-17: Object-Oriented Programming in C++", [
                "LE-11: Classes, Objects & Encapsulation — Design a Bank Account class with private balance and public deposit(), withdraw(), and display() methods.",
                "LE-12: Constructors & Memory Management — Implement a String class using Default, Parameterized, and Copy Constructors and a Destructor with dynamic memory allocation.",
                "LE-13: Static Members & Friend Functions — Program using a static member to count objects created and a friend function to compare private data of two classes.",
                "LE-14: Implementation of Inheritances — C++ program demonstrating arithmetic operations across Single, Multiple, Multilevel, Hierarchical, and Hybrid/Virtual inheritance.",
                "LE-15: Polymorphism & Abstract Classes — (i) Abstract Class Shape with pure virtual draw(), (ii) Area using function overloading, (iii) Complex number addition using operator overloading.",
                "LE-16: Robust Error Management — C++ exception handling using try, catch, and throw for 'Division by Zero' and 'Negative Stock Input'.",
                "LE-17: Template Implementation — C++ function template to find max of two values and class template (Pair) to store values of any data type."
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
    .content-box li {{ margin-bottom:0.5rem; }}
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

        # 1. Fix any existing files in this folder that wrongly point to ../ai/ or ai/
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
                [f"<li><strong>Key Topic:</strong> {t}</li>" for t in topics]
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

        # 5. Generate Individual Unit Pages (notes-unit1.html .. notes-unit5.html) if not already populated
        if is_theory:
            for idx, (u_title, topics) in enumerate(data["units"], 1):
                unit_path = os.path.join(folder, f"notes-unit{idx}.html")
                if folder in ["ai", "basics-of-electrical-electronics"] and os.path.exists(unit_path):
                    continue  # Preserve your existing custom notes in AI & BEEE
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