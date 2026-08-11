# Experiment 04: Step-by-Step Practical Procedure

---

## 🛑 MANUAL LAB EXECUTION CHECKPOINT

```text
============================================================
MANUAL LAB EXECUTION REQUIRED
============================================================
Experiment:          04 — Web Application Security Assessment
Target:              DVWA / OWASP BWA VM (http://<LAB_TARGET>/dvwa/)
Required Environment: Kali Linux VM + Target Web VM on Host-Only Network
Purpose:             Perform web application mapping, enumerate hidden endpoints, inspect security headers
Expected Evidence:   1. HTTP response header dump (outputs/http-headers.txt)
                     2. Directory brute-force log (outputs/dirb-mapping.txt)
                     3. Screenshot showing security header analysis (screenshots/04-01-headers.png)
============================================================
```

---

## 🛠️ Practical Procedure

### Step 1: Inspect HTTP Response Headers & Server Banners
Use `curl` to fetch server response headers from the target web server:
```bash
curl -i -s http://<LAB_TARGET>/ | tee outputs/http-headers.txt
```

*Audit Checklist:*
- Is `Server` banner disclosing exact version? (e.g., `Apache/2.2.8 (Ubuntu)`).
- Are `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options` present?

---

### Step 2: Web Application Directory & Endpoint Mapping
Discover hidden endpoints and unlinked directories using `dirb` or `gobuster`:
```bash
dirb http://<LAB_TARGET>/ /usr/share/dirb/wordlists/common.txt -o outputs/dirb-mapping.txt
```

---

### Step 3: Analyze Session Cookie Security Flags
Fetch login cookie headers using `curl` and inspect security attributes:
```bash
curl -i -c outputs/cookies.txt http://<LAB_TARGET>/dvwa/login.php
cat outputs/cookies.txt
```
*Audit:* Verify whether `HttpOnly` and `Secure` flags are enabled on `PHPSESSID`.

---

## 📷 Screenshot Checklist

1. `04-01-http-header-analysis.png`: Terminal output showing `curl -i` response headers and missing security flags.
2. `04-02-dirb-directory-enum.png`: Terminal output showing `dirb` discovering `/admin/`, `/config/`, or `/phpmyadmin/`.
