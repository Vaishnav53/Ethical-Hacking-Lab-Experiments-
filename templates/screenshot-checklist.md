# Experiment Screenshot Verification Checklist

---

## 📋 Checklist Standard

Every experiment submission must include valid screenshots stored in the experiment's `screenshots/` directory.

Use this checklist to confirm all required images are captured prior to final submission.

---

## 📸 Image Verification Matrix

| Exp # | Image Filename | Stage / Execution Point | Required Elements Visible | Captured? |
| :---: | :--- | :--- | :--- | :---: |
| **01** | `01-01-environment-check.png` | Network Ping Sweep | Terminal prompt, `ping` command, ICMP reply from `<TARGET_LAB_IP>` | [ ] |
| **01** | `01-02-dns-whois-recon.png` | DNS / WHOIS Query | Domain lookup command, record responses, system date | [ ] |
| **02** | `02-01-nmap-tcp-scan.png` | TCP Port Scanning | `nmap -sS -p- <TARGET_LAB_IP>` command & open ports output | [ ] |
| **02** | `02-02-service-os-fingerprint.png` | Service & OS Detection | `nmap -sV -O <TARGET_LAB_IP>` output showing OS guess & version info | [ ] |
| **03** | `03-01-vuln-scan-execution.png` | Vulnerability Scan | Nmap `--script vuln` or Nikto command line | [ ] |
| **03** | `03-02-cve-correlation.png` | CVE Identification | Identified CVE details matching specific service version | [ ] |
| **04** | `04-01-web-app-mapping.png` | Web App Directory Scan | Dirb / Gobuster / cURL output showing web endpoints | [ ] |
| **04** | `04-02-http-header-analysis.png` | HTTP Response Inspection | `curl -i` showing server banners & security headers | [ ] |
| **05** | `05-01-sqli-vulnerable-endpoint.png` | SQLi Payload Injection | Browser/cURL URL with SQLi payload triggering DB error or bypass | [ ] |
| **05** | `05-02-sqli-parameterized-fix.png` | Parameterized Query Defense | Code screenshot or CLI test showing blocked payload | [ ] |
| **06** | `06-01-xss-reflected-execution.png` | Reflected XSS PoC | Browser alert box or HTTP response containing encoded/executed script | [ ] |
| **06** | `06-02-xss-stored-execution.png` | Stored XSS PoC | Persistent payload rendering upon page reload | [ ] |
| **07** | `07-01-auth-test-app-run.png` | Password App Execution | Terminal running local Python auth application test suite | [ ] |
| **07** | `07-02-hash-salt-comparison.png` | Hash & Salt Output | Terminal output comparing MD5 (unsalted) vs Argon2/PBKDF2 (salted) | [ ] |
| **08** | `08-01-wireshark-interface-capture.png` | Packet Sniffing Start | Wireshark capturing on Host-Only interface (`eth0`) | [ ] |
| **08** | `08-02-plaintext-credential-exposure.png` | HTTP POST Stream Follow | Wireshark HTTP stream showing exposed credentials in POST body | [ ] |
| **09** | `09-01-pre-exploit-verification.png` | Pre-Exploit Check | Target state check before launching controlled exploit | [ ] |
| **09** | `09-02-controlled-shell-session.png` | Shell Privilege Verification | Terminal showing `whoami` & `id` on target after exploit | [ ] |
