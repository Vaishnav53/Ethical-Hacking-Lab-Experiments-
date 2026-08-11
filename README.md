# Ethical Hacking Laboratory Repository (MR23-1CS0432)

[![Course: MR23-1CS0432](https://img.shields.io/badge/Course-MR23--1CS0432-blue.svg)](https://www.mallareddyuniversity.ac.in/)
[![University: Malla Reddy University](https://img.shields.io/badge/University-MRU-maroon.svg)](https://www.mallareddyuniversity.ac.in/)
[![Environment: Authorized Educational Lab](https://img.shields.io/badge/Environment-Authorized%20Lab%20Only-green.svg)](#ethical--legal-compliance-warning)
[![Status: Experiments 01--09 Prepared](https://img.shields.io/badge/Status-Ready%20for%20Kali%20Execution-orange.svg)](#experiment-status-matrix)

---

## 📌 Course & Repository Metadata

| Attribute | Details |
| :--- | :--- |
| **Course Code** | `MR23-1CS0432` |
| **Course Title** | Ethical Hacking Laboratory |
| **Institution** | Malla Reddy University (MRU) |
| **Department** | Computer Science & Engineering / Cybersecurity |
| **Primary Target Platform** | Kali Linux (Tester VM) & Metasploitable / DVWA (Target VMs) |
| **Repository Scope** | Experiments 01 through 09 (Experiment 10 is **PENDING / DEFERRED**) |
| **Workspace Platform** | Windows Preparation Workspace -> Cloned to Isolated Kali Linux Lab |

---

## ⚠️ ETHICAL & LEGAL COMPLIANCE WARNING

> [!CAUTION]
> **AUTHORIZED EDUCATIONAL CYBERSECURITY LAB ONLY**
> 
> This repository contains structured laboratory procedures, theoretical analyses, viva voce preparation, and command templates for the **Ethical Hacking (MR23-1CS0432)** course at Malla Reddy University.
> 
> **STRICT RULES OF ENGAGEMENT:**
> 1. **Isolated Testing Only:** All practical security testing activities must strictly take place within deliberately vulnerable target environments (e.g., Metasploitable 2/3, DVWA, WebGoat) hosted on isolated private virtual networks (Host-only / Internal network mode).
> 2. **Prohibited Targets:** Never perform network scanning, vulnerability assessment, web application testing, or exploitation against university infrastructure, public Internet hosts, third-party applications, or unauthorized systems.
> 3. **Non-Fabrication Policy:** This repository strictly separates **Documentation Preparation** from **Practical Execution Evidence**. Documentation, command templates, and procedures are prepared in advance; practical evidence (raw terminal logs, pcap files, screenshots) must be generated through real execution within the isolated Kali Linux laboratory environment.
> 4. **No Host Weakening:** Under no circumstances should host firewall controls, Windows Defender, or security boundaries be disabled on host systems.

---

## 📂 Repository Architecture

```text
Ethical-Hacking-Experiments/
├── README.md                                # Master repository documentation & quickstart
├── LAB_SETUP.md                             # Complete virtualization & networking setup guide
├── SAFETY_AND_SCOPE.md                      # Rules of engagement, ethical guidelines & legal scope
├── ETHICAL_HACKING_LAB_COMPLETE_GUIDE.md    # Master textbook-grade comprehensive lab manual
├── EXPERIMENT_STATUS.md                     # Detailed verification & experiment completion matrix
├── TROUBLESHOOTING.md                       # Diagnostic & resolution guide for lab issues
├── .gitignore                               # Git exclusions for binary logs, PCAPs & VM artifacts
│
├── docs/                                    # Architectural & operational guidelines
│   ├── architecture.md                      # Detailed lab virtualization topology & state diagram
│   ├── lab-network-design.md                # Network subnetting, DHCP, Host-Only vs NAT rules
│   ├── evidence-guidelines.md               # Standards for terminal logs, screenshots & hashing
│   ├── reporting-guidelines.md              # Vulnerability documentation & CVSS v3.1 scoring guide
│   └── command-reference.md                 # Security CLI syntax cheat sheet (Nmap, Wireshark, etc.)
│
├── templates/                               # Standardized reporting templates for students
│   ├── experiment-report-template.md        # University formal experiment report template
│   ├── findings-template.md                 # Individual vulnerability documentation template
│   ├── evidence-log-template.md             # Execution timestamp & raw command log sheet
│   └── screenshot-checklist.md              # Required image capture verification matrix
│
├── experiment-01-network-reconnaissance/    # Passive/Active Recon, DNS, WHOIS, Host Discovery
├── experiment-02-port-service-enumeration/  # TCP/UDP Port Scanning, Service/Version/OS Detection
├── experiment-03-vulnerability-assessment/  # Vulnerability Scanning, CVE Correlation & CVSS Scoring
├── experiment-04-web-application-security/  # Web Mapping, HTTP Analysis, Security Misconfigurations
├── experiment-05-sql-injection/             # SQLi Detection, Parameterized Queries & Prevention
├── experiment-06-xss-analysis/              # Reflected/Stored XSS, Output Encoding, CSP Defenses
├── experiment-07-password-authentication/   # Hashing, Salting, Rate Limiting & Local Python Test App
├── experiment-08-network-traffic-analysis/  # Wireshark Packet Capture, HTTP vs HTTPS & Credential Exposure
├── experiment-09-controlled-exploitation/   # Controlled Exploit Lifecycle, Privilege Boundaries & Cleanup
│
└── experiment-10-integrated-assessment/     # PENDING / DEFERRED — Integrated Lab Capstone
    └── README.md                            # Official Deferral Notice & Scope Requirement
```

---

## 📊 Experiment Status Matrix

| Exp # | Experiment Title | Target Environment | Windows Prep Status | Practical Status |
| :---: | :--- | :--- | :---: | :---: |
| **01** | Network Reconnaissance and Information Gathering | Metasploitable / Isolated Target | ✅ PREPARED | ⏳ READY FOR KALI |
| **02** | Port Scanning and Service Enumeration | Metasploitable VM | ✅ PREPARED | ⏳ READY FOR KALI |
| **03** | Vulnerability Assessment of Deliberately Vulnerable Server | Metasploitable 2/3 VM | ✅ PREPARED | ⏳ READY FOR KALI |
| **04** | Web Application Security Assessment | DVWA / WebGoat VM | ✅ PREPARED | ⏳ READY FOR KALI |
| **05** | SQL Injection Detection and Prevention | DVWA / WebGoat VM | ✅ PREPARED | ⏳ READY FOR KALI |
| **06** | Cross-Site Scripting (XSS) Analysis | DVWA / WebGoat VM | ✅ PREPARED | ⏳ READY FOR KALI |
| **07** | Password Security and Authentication Testing | Local Python Auth App / Kali | ✅ PREPARED | 🧪 LOCALLY TESTED |
| **08** | Network Traffic Analysis and Credential Exposure | Wireshark + Isolated Lab | ✅ PREPARED | ⏳ READY FOR KALI |
| **09** | Controlled Exploitation and Post-Exploitation Analysis | Metasploitable VM | ✅ PREPARED | ⏳ READY FOR KALI |
| **10** | Integrated Ethical Hacking Assessment | Integrated Target Network | ⛔ DEFERRED | ⛔ PENDING |

> [!NOTE]
> **Status Lifecycle:** `NOT STARTED` ➔ `PREPARED` ➔ `READY FOR KALI` ➔ `IN PROGRESS` ➔ `PRACTICAL COMPLETE` ➔ `VERIFIED` ➔ `COMPLETE`.
> 
> *Documentation preparation alone does NOT constitute experiment completion. Experiments 01--06, 08, 09 will transition to `COMPLETE` only after practical execution in Kali Linux with verified screenshot and log evidence.*

---

## 🚀 Quick Start Guide

### 1. Prerequisites (Host Machine)
- Virtualization Hypervisor: **VirtualBox 7.x** or **VMware Workstation 17+**
- Virtual Machines:
  - **Kali Linux 2024.x** (Attacker VM - 4GB RAM, 20GB Disk)
  - **Metasploitable 2** (Target VM - 512MB RAM, 8GB Disk)
  - **OWASP Broken Web Applications (BWA)** or **DVWA container** (Target VM - 1GB RAM)

### 2. Workflow: Cloning into Kali Linux
Once VirtualBox/VMware networking is configured according to [LAB_SETUP.md](file:///d:/Ethical%20Hacking%20Experiments/LAB_SETUP.md):

```bash
# 1. Boot Kali Linux VM and open terminal
# 2. Clone the repository (replace placeholder with real URL)
git clone <YOUR_GITHUB_REPOSITORY_URL> Ethical-Hacking-Experiments

# 3. Enter the project directory
cd Ethical-Hacking-Experiments

# 4. Verify repository layout and status
cat EXPERIMENT_STATUS.md
```

### 3. Executing an Experiment (e.g., Experiment 01)
1. Navigate to the experiment directory:
   ```bash
   cd experiment-01-network-reconnaissance
   ```
2. Read the procedure and manual execution checkpoint:
   ```bash
   cat PROCEDURE.md
   ```
3. Execute commands strictly replacing `<TARGET_LAB_IP>` with your target VM's isolated IP address (e.g., `192.168.56.102`).
4. Save terminal logs to `outputs/` and screenshots to `screenshots/`.
5. Fill out the report in `reports/` following `templates/experiment-report-template.md`.

---

## 🔬 Local Test Application (Experiment 07)

Experiment 07 features a standalone educational Python application demonstrating secure authentication engineering (Argon2id/PBKDF2 hashing, CSPRNG salting, password entropy policies, failed login throttling) vs insecure design patterns.

### Running Local Auth App & Tests on Host/Kali:
```bash
# Navigate to Experiment 07 directory
cd experiment-07-password-authentication/scripts

# Run automated security test suite
python -m unittest discover -s tests -p "test_*.py" -v

# Run the interactive CLI security test application
python app.py
```

---

## 📜 Repository Standards & Policies

- **Command Syntax:** All command templates throughout this repository strictly utilize `<TARGET_LAB_IP>` or `<LAB_TARGET>` as host placeholders. Real IP addresses are identified during live VM execution (Phase 8).
- **Screenshot Policy:** Screenshot checklists (`screenshots/README.md`) specify exact capture requirements. Screenshots must be captured during live laboratory execution; non-genuine or synthetic images are prohibited.
- **Viva Preparation:** Every experiment directory contains a `VIVA.md` file featuring 10+ core theoretical and practical questions with comprehensive technical answers for university oral exams.

---

## 🏫 Institutional Info

- **University:** Malla Reddy University (MRU), Hyderabad, India
- **Course Syllabus Code:** MR23-1CS0432
- **Degree Program:** B.Tech Computer Science & Engineering (Cybersecurity)
- **Maintainer:** Ethical Hacking Laboratory Engineering Team

---
*For environment installation and virtualization architecture, refer to [LAB_SETUP.md](file:///d:/Ethical%20Hacking%20Experiments/LAB_SETUP.md).*
