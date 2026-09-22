# Ethical Hacking Laboratory — Experiments 02 & 07
## Malla Reddy University | MR23-1CS0432 | Cyber Security

---

## 📋 About This Deliverable

This folder contains the **complete, standalone, submission-ready reports** for exactly two experiments from the MR23-1CS0432 Ethical Hacking Laboratory course:

| # | Experiment Title | Status |
|---|---|---|
| **02** | Port Scanning and Service Enumeration | ✅ **COMPLETE** — Live Kali Linux execution evidence |
| **07** | Password Security and Authentication Testing | ✅ **COMPLETE** — Live Python execution evidence |

---

## 📁 Folder Structure

```
Ethical-Hacking-Experiments-2-and-7/
├── README.md                                    ← This file
├── Experiment-02/
│   ├── report/
│   │   ├── Experiment-02-Final-Report.pdf       ← Final submission PDF (16 pages)
│   │   └── Experiment-02-Final-Report.docx      ← Editable Word source
│   ├── screenshots/
│   │   ├── 02-01-network-configuration.png      ← Kali Linux ip a & ifconfig
│   │   ├── 02-02-full-tcp-port-scan.png         ← sudo nmap -p- 192.168.1.3 (30 ports)
│   │   ├── 02-03-service-os-detection.png       ← sudo nmap -sV -O 192.168.1.3
│   │   └── 02-04-udp-port-scan.png              ← sudo nmap -sU --top-ports 20 192.168.1.3
│   ├── evidence/
│   │   ├── nmap-full-tcp.txt                    ← Full TCP port scan log
│   │   ├── nmap-services.txt                    ← Service/version & OS detection log
│   │   └── nmap-udp.txt                         ← UDP port scan log
│   └── commands/
│       └── scan_commands.sh                     ← Reproducible Bash scanning script
│
└── Experiment-07/
    ├── report/
    │   ├── Experiment-07-Final-Report.pdf        ← Final submission PDF (12 pages)
    │   └── Experiment-07-Final-Report.docx       ← Editable Word source
    ├── screenshots/
    │   ├── 07-01-auth-test-app-run.png           ← python scripts/app.py live output
    │   └── 07-02-unit-test-pass.png              ← Ran 4 tests in 0.161s — OK
    ├── evidence/
    │   ├── auth-engine-run.txt                   ← Raw stdout of app.py
    │   └── unit-test-results.txt                 ← Raw stdout of unittest discover
    └── scripts/
        ├── app.py                                ← Interactive CLI engine
        ├── auth_engine.py                        ← AuthEngine (PBKDF2, MD5, CSPRNG, lockout)
        ├── requirements.txt                      ← Zero external dependencies
        └── tests/
            └── test_auth.py                      ← Automated unit test suite (4 tests)
```

---

## ✅ Evidence Integrity Statement

- All Experiment 02 screenshots (`02-01` through `02-04`) are **genuine Kali Linux terminal captures** taken during live scanning sessions against Metasploitable 2 (192.168.1.3) on September 2, 2026.
- All Experiment 07 screenshots (`07-01`, `07-02`) are **genuine Python terminal output renders** from live execution on September 22, 2026 (Python 3.14.6, Windows 11).
- All evidence text files contain the **actual raw stdout** from the commands stated.
- **No output has been fabricated, simulated, or copied from another experiment.**

---

## 🔁 Reproducing Experiment 07

```bash
# From Experiment-07/ directory:
python -m unittest discover -s scripts/tests -p "test_*.py" -v
python scripts/app.py
```

No external packages required — uses Python Standard Library only.

---

*Course: MR23-1CS0432 — Ethical Hacking Laboratory | Malla Reddy University*
