---
# ══════════════════════════════════════════════════════════════════
# Master resume — source of truth.
# Edit here; run `python build.py render-all` to regenerate output.
# ══════════════════════════════════════════════════════════════════

name: Ahmed Masud
title: "Enterprise Architect · AI Security Pioneer · Founder"
location: "Ottawa, ON, Canada"

contact:
  email:    ahmed.masud@linux.com
  phone:    "(613) 879-6913"
  linkedin: linkedin.com/in/ahmedmasud
  website:  ahmed-masud.github.io

summary: |
  Cybersecurity executive and enterprise architect with 30+ years building
  mission-critical systems across defence, government, and enterprise sectors.
  Founder of saf.ai (US Patent 12,045,224 — Cybernetic Engrams®, AI-enhanced
  self-defending data) and Trustifier (100+ enterprise clients). Led $100M+ DoD/DND
  programs in SCIF environments. CWID 2009 Blue Ribbon Winner. SINET 2010 Innovator
  Award. Former Secret clearances — Canada, US, NATO (expired; eligible for
  re-sponsorship). TOGAF-grounded. Deep hands-on engineering background alongside
  executive delivery capability.

highlights:
  - "US Patent 12,045,224"
  - "Secret Clearance Eligible"
  - "CWID 2009 Blue Ribbon"
  - "SINET 2010 Innovator"
  - "TOGAF / SABSA"
  - "NIST 800-53"
  - "DND / DoD / NATO"

# ── Experience ────────────────────────────────────────────────────
# Each entry has an `id` used for selective inclusion / override in job files.
# tags: used for human filtering; not rendered directly.
# bullets: markdown strings — *italic*, **bold**, etc. are supported.

experience:
  - id: safai
    title: "Founder & CEO"
    company: "saf.ai, Inc."
    dates: "2018 – Present"
    location: "Ottawa, ON"
    tags: [ai, security, founder, startup, patent, architecture, embedded, rust]
    desc: |
      Leading development of Resiliate — an AI-enhanced self-defending filesystem
      with sub-100ms policy enforcement and <0.1s ransomware rollback, targeting
      Azure Marketplace enterprise deployment.
    bullets:
      - "US Patent 12,045,224 — *Methods For Self-Aware, Self-Healing, And Self-Defending Data* (Cybernetic Engrams®): data blocks encoded as neural network weights for active self-defense and verification"
      - "F5 Networks: deployed Resiliate for real-time anomaly detection processing ~1 billion HTTP requests/hour in production"
      - "Designed 5-layer security orchestration (SoDAC, SoDynTBAC, SoNFSv4ACL, SoBibaMIC, SoBLPMAC) — NIST 800-53 High-Impact across FedRAMP, CMMC, HIPAA, DoD IL4/IL5"
      - "Built enterprise-grade platform: 26 Rust crates, 1M+ lines of code, 42 git submodules"
      - "SINET 2010 Innovator Award — National Press Club, Washington DC"

  - id: trustifier
    title: "CEO & CTO"
    company: "Trustifier Inc."
    dates: "2005 – Present"
    location: "Ottawa, ON"
    tags: [security, enterprise, saas, ecommerce, founder, platform, web, php, java]
    desc: |
      Cybersecurity consultancy serving 100+ enterprise clients across government,
      healthcare, and financial sectors.
    bullets:
      - "CWID 2009 Blue Ribbon Winner — Trustifier KSE platform achieved DoD Red Team's first-ever failed breach attempt in cross-domain scenario"
      - "NIST 800-53 High-Impact mappings across all 16 control families at AUGMENTED levels across five product ecosystems"
      - "Kaiser Permanente (~2014): designed session-aware HTTP/HTTPS proxy (WebSphere/Java) that transparently mobilized desktop apps to iPad — zero rewrites, zero downtime"
      - "Built and commercialized KSE, RYU, Fahrenheit, HPCE, CloudFort, Luminate — serving Fortune 500 and federal agency clients"
      - "TOGAF and SABSA-grounded enterprise architecture; OAuth2/OIDC/SAML at protocol level across multi-tenant IAM platforms"

  - id: dod
    title: "Senior Program Manager & Architect"
    company: "DoD / DND Programs"
    dates: "2008 – 2018"
    location: "Ottawa, ON / Washington, DC"
    tags: [defence, government, nato, clearance, embedded, architecture, classified]
    desc: |
      Led $100M+ mission-critical programs for the US Department of Defense and Canadian DND,
      including enterprise architecture modernization and national security infrastructure
      delivery in SCIF environments.
    bullets:
      - "DND Enterprise Architecture — national security infrastructure modernization across DoD and DND standards"
      - "DoD PEO STRI Senior Consultant (2008–2009) — strategic advisory on training and simulation systems architecture"
      - "MKS Technologies / US Navy (2011) — Chief Designer for experimental stealth CPU with hardware-level OTP encryption"
      - "FreeRTOS (deep development); Cortex-M core; TI DSP; UART/SPI/I2C peripheral drivers for UAV signal processing (Allied Forces/NATO)"
      - "Cross-agency coordination: DoD, DND, NATO partners; former Secret clearances — Canada, US, NATO (eligible for re-sponsorship)"

  - id: googgun
    title: "Founder & Principal Engineer"
    company: "Googgun Technologies"
    dates: "1998 – 2007"
    location: "Ottawa, ON"
    tags: [consulting, engineering, web, php, data, government, publishing]
    desc: |
      Founded software engineering R&D lab and consultancy serving federal government and
      enterprise clients across Canada and the US. All work as prime contractor.
    bullets:
      - "Allen & Unwin (Australia, 2002–2003): solved Harry Potter *Order of the Phoenix* data leakage problem IBM couldn't fix in 2.5 years — resolved remotely in 5 days; travelled on-site for zero-downtime hardening"
      - "NRC: designed cross-platform Oracle database synchronization across Mainframe, HP-UX, Solaris, Linux, and Windows NT in real time"
      - "MaxTran — proprietary DSL for real-time GPS data correction deployed for continental-scale geospatial infrastructure (Geodetics Survey)"
      - "gScarlet — world's first web UI for IPv4/IPv6 Linux firewall (C + PHP5); sold to Morgen Taler Clinic, NRCan, NRC, CDND"
      - "SnapLinux — custom Linux distribution for embedded field systems; sold commercially to NRCan and Geodetics Survey Division"

  - id: remedium
    title: "Founder & CTO"
    company: "Remedium Security Systems Inc."
    dates: "1994 – 1997"
    location: "Ottawa, ON"
    tags: [security, founder, unix, embedded, early]
    desc: ""
    bullets:
      - "Founded cybersecurity startup with Safdar Masud; developed Exorcist — first kernel-level Unix/Linux daemon monitoring and self-correction system"
      - "Pioneer in proactive Unix/Linux security — detecting and correcting daemon anomalies before they became exploits"

  - id: nrc
    title: "Senior Systems Developer"
    company: "NRCan / NRC"
    dates: "1992 – 1998"
    location: "Ottawa, ON"
    tags: [government, geospatial, embedded, linux, data]
    desc: ""
    bullets:
      - "Built real-time GPS correction systems for Canadian national geospatial infrastructure"
      - "Delivered mission-critical systems with 99.9%+ uptime requirements across federal science agencies"

# ── Skills ────────────────────────────────────────────────────────
# Keys are section labels; values are plain text (use · as separator).
# Job files can replace this entire block via skills_override.

skills:
  Architecture: "Enterprise Architecture (TOGAF/SABSA) · Solution Architecture · DND EA Standards · Conceptual / Logical / Physical Design · Reference Architectures · NIST 800-53 (all 16 control families)"
  Security: "Zero-trust · RBAC/ABAC/MAC · OAuth2/OIDC/SAML · FedRAMP · CMMC · HIPAA · DoD IL4/IL5 · SSL/TLS · PKI · Ransomware defense · Incident response"
  Languages: "Rust · Python · TypeScript · JavaScript (Node.js) · C/C++ · Java (J2EE – IBM Java 9) · PHP (3/4/5/6) · SQL/PL-SQL · Go (actively learning)"
  "Cloud & Infra": "Azure · AWS · Kubernetes/AKS · CSI drivers · Docker · Linux/Unix · High-availability systems"
  Integration: "REST/GraphQL/SOAP/XML/JSON · SOA · Microservices · Apache Camel 4.x · EIP patterns · HTTP/HTTPS proxy · WebSphere · gRPC · WebSockets"
  "Data & AI": "Oracle 7–12c · PostgreSQL · Oracle↔MSSQL sync · LLM integration · Agentic workflows · Neural network architectures · Prometheus · Grafana · Splunk · GitHub Copilot"
  Embedded: "FreeRTOS · Cortex-M · TI DSP · UART/SPI/I2C · Hardware OTP encryption · Kernel-level Unix/Linux security"

# ── Patents ───────────────────────────────────────────────────────

patents:
  - number: "12,045,224"
    issued: 2024
    assignee: "saf.ai, Inc."
    title: "Methods For Self-Aware, Self-Healing, And Self-Defending Data"
    desc: "Cybernetic Engrams® — transforming data blocks into neural network weights for active self-verification, self-healing, and self-defense. Also pending: CA 3,127,068 · EP 3915060."

# ── Awards ────────────────────────────────────────────────────────

awards:
  - year: 2009
    title: "CWID Blue Ribbon Winner"
    detail: "Coalition Warrior Interoperability Demonstration; DoD Red Team's first-ever failed breach attempt in a cross-domain scenario"
  - year: 2010
    title: "SINET Innovator Award"
    detail: "National Press Club, Washington DC, alongside Invincea and FireEye"

# ── Education ─────────────────────────────────────────────────────

education:
  - degree: "Research Fellow — Number Theory"
    school: "University of Ottawa"
    dates: "1991–1992"
    note: "Mock-theta functions, q-hypergeometric series under Dr. Bassam Nassrallah"
  - degree: "Bachelor of Engineering (Incomplete)"
    school: "University of Ottawa"
    dates: "1991–1994"
    note: "Chemical & Electrical Engineering — pursued concurrently with active professional practice"
  - degree: "Associate of Applied Science"
    school: "Vanier College"
    dates: "1990"
    note: ""

certifications:
  - "TOGAF (Enterprise Architecture)"
  - "Certified Data Centre Management Professional (CDCMP, 2010)"
  - "Certified Data Centre Professional (CDCP, 2004)"
  - "PMP — formerly held (also taught PMP certification)"

# ── Clearances ────────────────────────────────────────────────────

clearances: "Former Secret clearances — Canada, US, NATO (expired; eligible for re-sponsorship). Extensive SCIF and classified environment delivery experience."
---
