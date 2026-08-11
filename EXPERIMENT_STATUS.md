# University Experiment Completion & Verification Status Matrix

Course Code: **MR23-1CS0432** | Course: **Ethical Hacking Laboratory** | Institution: **Malla Reddy University**

---

## 🚦 Status Lifecycle Legend

- `NOT STARTED`: Experiment repository structure not yet initialized.
- `PREPARED`: Documentation, theory, step-by-step procedures, viva Q&A, and command templates created.
- `READY FOR KALI`: Ready for practical execution in an isolated Kali Linux hypervisor environment.
- `IN PROGRESS`: Practical execution currently underway by student in Kali Linux.
- `PRACTICAL COMPLETE`: Real terminal logs, outputs, and screenshots captured in Kali Linux.
- `VERIFIED`: Report audited and verified against non-fabrication & evidence standards.
- `COMPLETE`: Full experiment lifecycle completed, committed to Git repository.
- `DEFERRED`: Experiment intentionally postponed per university syllabus directive.

---

## 📋 Comprehensive Status Matrix

| Exp # | Experiment Title | Windows Prep | Kali Execution | Evidence Verified | Overall Status | Last Updated |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **01** | Network Reconnaissance and Information Gathering | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **02** | Port Scanning and Service Enumeration | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **03** | Vulnerability Assessment of Deliberately Vulnerable Server | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **04** | Web Application Security Assessment | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **05** | SQL Injection Detection and Prevention | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **06** | Cross-Site Scripting (XSS) Analysis | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **07** | Password Security and Authentication Testing | ✅ Done | 🧪 Tested | ✅ Code Verified | `READY FOR PRACTICAL` | 2026-08-11 |
| **08** | Network Traffic Analysis and Credential Exposure | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **09** | Controlled Exploitation and Post-Exploitation Analysis | ✅ Done | ⏳ Pending | ⏳ Pending | `READY FOR KALI` | 2026-08-11 |
| **10** | Integrated Ethical Hacking Assessment | ⛔ Deferred | ⛔ Deferred | ⛔ Deferred | `DEFERRED / PENDING` | 2026-08-11 |

---

## 📌 Specific Experiment Checkpoints

### Experiment 01 — Network Reconnaissance
- [x] Theory & Procedure Documented (`experiment-01-network-reconnaissance/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] Active Nmap scan output saved to `outputs/nmap-recon.txt`
- [ ] Screenshot captured (`01-target-discovery.png`)

### Experiment 02 — Port Scanning & Enumeration
- [x] Theory & Procedure Documented (`experiment-02-port-service-enumeration/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] Complete TCP port scan output saved to `outputs/nmap-full-tcp.txt`
- [ ] Version & OS fingerprint output saved to `outputs/nmap-services.txt`

### Experiment 03 — Vulnerability Assessment
- [x] Theory & Procedure Documented (`experiment-03-vulnerability-assessment/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] CVE correlation matrix generated in `reports/vulnerability-report.md`
- [ ] CVSS scoring verified against observed service versions

### Experiment 04 — Web Application Security Assessment
- [x] Theory & Procedure Documented (`experiment-04-web-application-security/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] HTTP request/response headers captured in `outputs/http-headers.txt`
- [ ] Security misconfigurations logged

### Experiment 05 — SQL Injection Detection & Prevention
- [x] Theory & Procedure Documented (`experiment-05-sql-injection/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] Error-based and Union-based PoC evidence logged
- [ ] Vulnerable vs Secure code examples validated

### Experiment 06 — Cross-Site Scripting (XSS) Analysis
- [x] Theory & Procedure Documented (`experiment-06-xss-analysis/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] Reflected & Stored PoC evidence logged
- [ ] Output encoding & CSP defense verified

### Experiment 07 — Password Security & Authentication Testing
- [x] Theory & Procedure Documented (`experiment-07-password-authentication/PROCEDURE.md`)
- [x] Local Python test application created (`scripts/app.py`)
- [x] Automated unit test suite executed and passed (`tests/test_auth_app.py`)
- [ ] Kali Linux execution verified

### Experiment 08 — Network Traffic Analysis
- [x] Theory & Procedure Documented (`experiment-08-network-traffic-analysis/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached
- [ ] PCAP file recorded on Host-Only interface
- [ ] Plaintext credential extraction verified on HTTP vs HTTPS

### Experiment 09 — Controlled Exploitation
- [x] Theory & Procedure Documented (`experiment-09-controlled-exploitation/PROCEDURE.md`)
- [ ] Manual Lab Execution Checkpoint Reached (Strict Scope Control)
- [ ] Pre-exploitation snapshot verified
- [ ] Controlled command shell session logged & cleanup verified

### Experiment 10 — Integrated Ethical Hacking Assessment
- [x] Placeholder README created (`experiment-10-integrated-assessment/README.md`)
- [x] Status explicitly marked **PENDING / DEFERRED**
- [ ] Final capstone execution pending Experiments 01-09 practical completion
