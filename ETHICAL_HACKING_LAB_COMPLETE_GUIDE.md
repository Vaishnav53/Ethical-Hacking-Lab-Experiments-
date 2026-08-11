# Ethical Hacking Complete Laboratory Guide & Manual

**Course Code:** `MR23-1CS0432`  
**Course Title:** Ethical Hacking Laboratory  
**Institution:** Malla Reddy University (MRU), Hyderabad  
**Department:** Computer Science & Engineering (Cybersecurity)  

---

## 📖 Table of Contents

1. [Course Overview & Educational Objectives](#1-course-overview--educational-objectives)
2. [Laboratory Architecture & Isolation Rules](#2-laboratory-architecture--isolation-rules)
3. [Safety Guidelines & Legal Compliance](#3-safety-guidelines--legal-compliance)
4. [Hypervisor & VM Setup Guide](#4-hypervisor--vm-setup-guide)
5. [Git Repository & Kali Linux Workflow](#5-git-repository--kali-linux-workflow)
6. [Chapter 01: Network Reconnaissance & Information Gathering](#chapter-01-network-reconnaissance--information-gathering)
7. [Chapter 02: Port Scanning & Service Enumeration](#chapter-02-port-scanning--service-enumeration)
8. [Chapter 03: Vulnerability Assessment of Server Systems](#chapter-03-vulnerability-assessment-of-server-systems)
9. [Chapter 04: Web Application Security Assessment](#chapter-04-web-application-security-assessment)
10. [Chapter 05: SQL Injection Detection & Prevention](#chapter-05-sql-injection-detection--prevention)
11. [Chapter 06: Cross-Site Scripting (XSS) Analysis](#chapter-06-cross-site-scripting-xss-analysis)
12. [Chapter 07: Password Security & Authentication Testing](#chapter-07-password-security--authentication-testing)
13. [Chapter 08: Network Traffic Analysis & Credential Exposure](#chapter-08-network-traffic-analysis--credential-exposure)
14. [Chapter 09: Controlled Exploitation & Post-Exploitation Analysis](#chapter-09-controlled-exploitation--post-exploitation-analysis)
15. [Chapter 10: Integrated Assessment (Deferred Notice)](#chapter-10-integrated-assessment-deferred-notice)
16. [Evidence Collection & Reporting Standards](#16-evidence-collection--reporting-standards)
17. [Troubleshooting & Frequently Asked Questions](#17-troubleshooting--frequently-asked-questions)

---

## 1. Course Overview & Educational Objectives

The **Ethical Hacking Laboratory (MR23-1CS0432)** course at Malla Reddy University provides B.Tech Cybersecurity students with hands-on technical proficiency in offensive security methodologies, vulnerability assessment, web application auditing, network traffic analysis, and secure coding practices.

By understanding offensive vectors, students learn to design robust defenses, configure firewall controls, enforce secure authentication standards, and implement parameterized software queries.

---

## 2. Laboratory Architecture & Isolation Rules

```text
+-------------------------------------------------------------------------+
|                        ISOLATED VIRTUAL LABORATORY                      |
|                                                                         |
|  Attacker VM: Kali Linux 2024.x          IP: 192.168.56.101/24         |
|  Target VM 1: Metasploitable 2/3         IP: 192.168.56.102/24         |
|  Target VM 2: DVWA / OWASP BWA           IP: 192.168.56.103/24         |
|                                                                         |
|  Network Mode: Host-Only Adapter (192.168.56.0/24)                      |
|  WAN Routing: Permanently Disabled (No Gateway)                         |
+-------------------------------------------------------------------------+
```

---

## 3. Safety Guidelines & Legal Compliance

> [!CAUTION]
> All testing must strictly remain inside private Host-Only virtual subnets (`192.168.56.0/24`).
> Scanning or attacking public Internet hosts, university Wi-Fi, or unauthorized systems violates the IT Act (2000) of India and results in immediate academic disqualification.

---

## 4. Hypervisor & VM Setup Guide

For full setup procedures, refer to [LAB_SETUP.md](file:///d:/Ethical%20Hacking%20Experiments/LAB_SETUP.md).
- **Hypervisor:** VirtualBox 7.x or VMware Workstation 17+.
- **Adapter Mode:** Host-Only Adapter (`VirtualBox Host-Only Ethernet Adapter`).
- **DHCP Subnet:** `192.168.56.0/24` (Lower: `.100`, Upper: `.200`).

---

## 5. Git Repository & Kali Linux Workflow

```bash
# 1. Boot Kali Linux VM
# 2. Clone repository in Kali terminal
git clone <YOUR_GITHUB_REPOSITORY_URL> Ethical-Hacking-Experiments

# 3. Enter repository directory
cd Ethical-Hacking-Experiments

# 4. Check experiment preparation status
cat EXPERIMENT_STATUS.md
```

---

## Chapter 01: Network Reconnaissance & Information Gathering
- **Target:** Metasploitable VM (`<TARGET_LAB_IP>`)
- **Key Concepts:** Passive vs Active Recon, DNS A/NS/MX records, WHOIS database queries, ARP/ICMP ping sweeps.
- **Primary Commands:**
  ```bash
  sudo netdiscover -i eth0 -r 192.168.56.0/24
  ping -c 4 <TARGET_LAB_IP>
  sudo nmap -sn -PE -PS22,80 <TARGET_LAB_IP> -oN outputs/nmap-recon.txt
  ```

---

## Chapter 02: Port Scanning & Service Enumeration
- **Target:** Metasploitable VM (`<TARGET_LAB_IP>`)
- **Key Concepts:** TCP 3-way handshake, SYN stealth (`-sS`) vs Connect (`-sT`) scans, service banner grabbing (`-sV`), OS fingerprinting (`-O`).
- **Primary Commands:**
  ```bash
  sudo nmap -sS -p- -T4 <TARGET_LAB_IP> -oN outputs/nmap-full-tcp.txt
  sudo nmap -sV -O -p 21,22,23,80,445,3306 <TARGET_LAB_IP> -oN outputs/nmap-services.txt
  ```

---

## Chapter 03: Vulnerability Assessment of Server Systems
- **Target:** Metasploitable 2/3 VM
- **Key Concepts:** Vulnerability management lifecycle, CVE IDs, NVD dictionary, CVSS v3.1 scoring, service version patch auditing vs false positives.
- **Primary Commands:**
  ```bash
  sudo nmap -sV --script vuln <TARGET_LAB_IP> -oN outputs/nmap-vuln-scan.txt
  ```

---

## Chapter 04: Web Application Security Assessment
- **Target:** DVWA (`http://<LAB_TARGET>/dvwa/`)
- **Key Concepts:** OWASP Top 10 (2021), HTTP methods/headers, security headers (`CSP`, `HSTS`, `X-Frame-Options`), session cookie security flags (`HttpOnly`, `Secure`).
- **Primary Commands:**
  ```bash
  curl -i -s http://<LAB_TARGET>/ | tee outputs/http-headers.txt
  dirb http://<LAB_TARGET>/ /usr/share/dirb/wordlists/common.txt -o outputs/dirb-mapping.txt
  ```

---

## Chapter 05: SQL Injection Detection & Prevention
- **Target:** DVWA SQLi Module
- **Key Concepts:** SQL syntax hijacking, In-Band (Error/UNION) vs Blind SQLi, parameterization defense using Prepared Statements (`PDO` / `mysqli`).
- **Primary Commands:**
  ```sql
  -- Detection Payload
  1' ORDER BY 2-- -
  -- UNION Metadata Extraction Payload
  1' UNION SELECT version(), user()-- -
  ```

---

## Chapter 06: Cross-Site Scripting (XSS) Analysis
- **Target:** DVWA XSS Modules
- **Key Concepts:** Reflected vs Stored vs DOM XSS, JavaScript sources and sinks, HTML entity output encoding (`htmlspecialchars()`), CSP header enforcement.
- **Harmless PoC Payload:**
  ```html
  <script>alert('XSS-Lab-06-PoC')</script>
  ```

---

## Chapter 07: Password Security & Authentication Testing
- **Target:** Local Educational Python Application (`experiment-07-password-authentication/scripts/app.py`)
- **Key Concepts:** Legacy MD5/SHA1 vs PBKDF2/bcrypt/Argon2id, CSPRNG 16-byte salting, password entropy calculation, failed-login account lockout rate limiting.
- **Execution:**
  ```bash
  python -m unittest discover -s scripts/tests -p "test_*.py" -v
  python scripts/app.py
  ```

---

## Chapter 08: Network Traffic Analysis & Credential Exposure
- **Target:** Wireshark on Host-Only interface `eth0`
- **Key Concepts:** Promiscuous mode, unencrypted HTTP vs TLS encrypted HTTPS, display filters, TCP stream reassembly.
- **Primary Filters:**
  ```text
  http.request.method == "POST"
  ip.addr == <TARGET_LAB_IP>
  ```

---

## Chapter 09: Controlled Exploitation & Post-Exploitation Analysis
- **Target:** Metasploitable VM (vsftpd 2.3.4 backdoor) — **Strict Scope Control**
- **Key Concepts:** Ethical exploit lifecycle, Bind vs Reverse shells, post-exploit privilege assessment (`whoami`, `id`), mandatory snapshot recovery.
- **Metasploit Commands:**
  ```msf
  use exploit/unix/ftp/vsftpd_234_backdoor
  set RHOSTS <TARGET_LAB_IP>
  exploit
  ```

---

## Chapter 10: Integrated Assessment (Deferred Notice)
- **Status:** **PENDING / DEFERRED**
- **Notice:** Experiment 10 is intentionally postponed until Experiments 01 through 09 have been practically executed in Kali Linux with verified screenshot evidence.

---

## 16. Evidence Collection & Reporting Standards

Refer to [docs/evidence-guidelines.md](file:///d:/Ethical%20Hacking%20Experiments/docs/evidence-guidelines.md) and [templates/experiment-report-template.md](file:///d:/Ethical%20Hacking%20Experiments/templates/experiment-report-template.md).
- Terminal logs must be saved to `outputs/`.
- Uncropped screenshots must be saved to `screenshots/`.
- Non-fabrication policy applies to all submissions.

---

## 17. Troubleshooting & Frequently Asked Questions

Refer to [TROUBLESHOOTING.md](file:///d:/Ethical%20Hacking%20Experiments/TROUBLESHOOTING.md) for VM networking fixes, DHCP errors, Nmap probe fixes, and Python execution fixes.
