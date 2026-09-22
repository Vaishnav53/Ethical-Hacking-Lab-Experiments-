# Ethical Hacking Laboratory — MR23-1CS0432
## Malla Reddy University | Department of CSE (Cyber Security)

---

> [!IMPORTANT]
> **This repository contains completed work for Experiment 01 and Experiment 07 only.**
> Other experiments (02–06, 08–10) are NOT represented as completed here.
> All practical evidence in this repository is from real, authorized laboratory execution.
> No fabricated evidence, screenshots, or outputs are included.

---

## 📋 Completed Experiments

| # | Experiment Title | Status | Evidence |
|---|---|---|---|
| **01** | Network Reconnaissance and Information Gathering | ✅ **COMPLETE** | Authentic Kali Linux execution; 11 screenshots from source report |
| **07** | Password Security and Authentication Testing | ✅ **COMPLETE** | Live Python execution (Sep 22, 2026); 4 tests passed |

---

## 📁 Repository Structure

```
Ethical-Hacking-Lab-Experiments-/
│
├── README.md                                     ← This file
│
├── experiment-01-network-reconnaissance/
│   ├── reports/
│   │   ├── Experiment-01-Final-Report.pdf        ← Final submission PDF
│   │   └── Experiment-01-Final-Report.docx       ← Editable Word source
│   ├── screenshots/                              ← 11 authentic Kali Linux screenshots
│   │   ├── 01-01-ip-addr-network-interface.jpg
│   │   ├── 01-02-ip-route-gateway.jpg
│   │   ├── 01-03-ping-connectivity.jpg
│   │   ├── 01-04-resolv-conf-dns.jpg
│   │   ├── 01-05-nslookup-dns-query.jpg
│   │   ├── 01-06-host-dns-records.jpg
│   │   ├── 01-07-nmap-host-discovery.jpg
│   │   ├── 01-08-nmap-host-discovery-result.jpg
│   │   ├── 01-09-nmap-service-scan.jpg
│   │   ├── 01-10-nmap-os-detection.jpg
│   │   └── 01-11-nmap-os-detection-result.jpg
│   ├── outputs/                                  ← 11 command output evidence files
│   │   ├── 01-step1-ip-addr.txt
│   │   ├── 01-step2-ip-route.txt
│   │   ├── 01-step3-ping-connectivity.txt
│   │   ├── 01-step4-resolv-conf.txt
│   │   ├── 01-step5-nslookup.txt
│   │   ├── 01-step6-host-dns.txt
│   │   ├── 01-step7-dig-mx.txt
│   │   ├── 01-step8-nmap-host-discovery.txt
│   │   ├── 01-step9-nmap-service-scan.txt
│   │   ├── 01-step10-nmap-enumeration.txt
│   │   └── 01-step11-nmap-os-detection.txt
│   ├── PROCEDURE.md
│   ├── THEORY.md
│   ├── VIVA.md
│   └── README.md
│
└── experiment-07-password-authentication/
    ├── reports/
    │   ├── Experiment-07-Final-Report.pdf        ← Final submission PDF
    │   └── Experiment-07-Final-Report.docx       ← Editable Word source
    ├── screenshots/
    │   ├── 07-01-auth-test-app-run.png           ← python scripts/app.py live output
    │   └── 07-02-unit-test-pass.png              ← Ran 4 tests in 0.161s — OK
    ├── evidence/
    │   ├── auth-engine-run.txt                   ← Raw stdout of scripts/app.py
    │   └── unit-test-results.txt                 ← Raw stdout of unittest discover
    ├── scripts/
    │   ├── app.py                                ← Interactive CLI engine
    │   ├── auth_engine.py                        ← PBKDF2, MD5, CSPRNG, lockout
    │   ├── requirements.txt                      ← Zero external dependencies
    │   └── tests/test_auth.py                    ← 4 automated unit tests
    ├── PROCEDURE.md
    ├── THEORY.md
    ├── VIVA.md
    └── README.md
```

---

## 🔬 Experiment 01 — Network Reconnaissance and Information Gathering

**Executed on:** Kali Linux (eth0: 10.0.2.15/24, NAT)  
**Target:** 10.0.2.2 (QEMU/VirtualBox NAT gateway)

| Step | Command | Key Finding |
|---|---|---|
| 1 | `ip addr` | eth0 at 10.0.2.15/24 — UP and RUNNING |
| 2 | `ip route` | Default gateway: 10.0.2.2 via eth0 |
| 3 | `ping -c 4 8.8.8.8` | 0% packet loss, avg RTT 65.797 ms |
| 4 | `cat /etc/resolv.conf` | DNS: 192.168.137.1, search: mshome.net |
| 5 | `nslookup google.com 8.8.4.4` | 6 A records + 4 AAAA records |
| 6 | `host google.com` | MX: smtp.google.com (priority 10) |
| 7 | `dig google.com MX` | MX confirmed, 27 ms query, NOERROR |
| 8 | `sudo nmap -sn 10.0.2.0/24` | 3 hosts: 10.0.2.2, 10.0.2.3, 10.0.2.15 |
| 9 | `sudo nmap -sS -sV 10.0.2.2` | 135/msrpc, 445/SMB, 5432/postgresql |
| 10 | `sudo nmap -sC -sV -p 135,445,5432 10.0.2.2` | SMB signing REQUIRED (hardened) |
| 11 | `sudo nmap -O -p 135,445,5432 10.0.2.2` | OS detection INCONCLUSIVE (NAT bridge) |

---

## 🔐 Experiment 07 — Password Security and Authentication Testing

**Executed on:** Python 3.14.6, Windows 11 — September 22, 2026  
**No external dependencies** — Python Standard Library only

| Metric | Value |
|---|---|
| MD5 hash of "LaboratoryPassword2026!" | `096b1f381d46137f604347537db76776` (deterministic — insecure) |
| PBKDF2 Run 1 salt | `fcd7d5c65d34c46348a007bdae2a3278` (CSPRNG — unique) |
| PBKDF2 Run 2 salt | `aaa275edf37f18f86af01e845afb6fec` (different every run) |
| Password entropy | **150.76 bits** (>> 50-bit minimum) |
| Account lockout | After **3** failed attempts |
| Unit tests | **4/4 PASSED** in 0.161 s |

### Reproduce Experiment 07

```bash
# From experiment-07-password-authentication/ — no packages required:
python -m unittest discover -s scripts/tests -p "test_*.py" -v
python scripts/app.py
```

---

## ✅ Evidence Integrity

All screenshots and terminal outputs in this repository are **authentic** — taken from real execution sessions:

- **Experiment 01** screenshots: Extracted from `ilovepdf_merged.pdf` (original laboratory record submitted to institution)
- **Experiment 07** outputs: Live Python execution on September 22, 2026 (Python 3.14.6, Windows 11)

> [!CAUTION]
> **No fabricated evidence.** No outputs, screenshots, timestamps, IP addresses, hashes, or test results have been invented or simulated.
> All activities were performed within an isolated, authorized laboratory environment.

---

## 📚 Course Details

- **Course Code:** MR23-1CS0432
- **Course Name:** Ethical Hacking Laboratory
- **Institution:** Malla Reddy University
- **Department:** Computer Science and Engineering (Cyber Security)
