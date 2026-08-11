# Experiment 04: Theory & Conceptual Background

---

## 🌐 1. HTTP Protocol & Web Architecture

Web applications operate on the Client-Server model over HTTP/HTTPS:
- **HTTP Request Methods:** GET (retrieve data), POST (submit form/JSON payload), PUT/DELETE (resource management).
- **HTTP Status Codes:** `200 OK`, `301/302 Redirect`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `500 Internal Server Error`.
- **Statelessness & Session Management:** Because HTTP is stateless, web apps issue HTTP cookies (`Set-Cookie: PHPSESSID=...`) or JSON Web Tokens (JWT) to track authenticated user state.

---

## 🛡️ 2. OWASP Top 10 (2021) Overview

1. **A01:2021-Broken Access Control:** Users acting outside intended permissions.
2. **A02:2021-Cryptographic Failures:** Plaintext transmission of credentials, weak cipher suites.
3. **A03:2021-Injection:** SQLi, Command Injection, LDAP Injection.
4. **A04:2021-Insecure Design:** Flaws in application workflow architecture.
5. **A05:2021-Security Misconfiguration:** Default admin credentials, verbose error pages, missing security headers.
6. **A06:2021-Vulnerable and Outdated Components:** Outdated PHP/Apache frameworks.
7. **A07:2021-Identification and Authentication Failures:** Weak password rules, brute-force vulnerability.
8. **A08:2021-Software and Data Integrity Failures:** Insecure deserialization.
9. **A09:2021-Security Logging and Monitoring Failures:** Insufficient auditing.
10. **A10:2021-Server-Side Request Forgery (SSRF):** Fetching remote URLs without validation.

---

## 🔒 3. Mandatory Security Headers

- **`Content-Security-Policy` (CSP):** Restricts script execution sources to prevent XSS.
- **`Strict-Transport-Security` (HSTS):** Enforces encrypted HTTPS connections.
- **`X-Frame-Options`:** Prevents Clickjacking by disabling `<frame>` embedding (`DENY` / `SAMEORIGIN`).
- **`X-Content-Type-Options`:** Set to `nosniff` to block MIME-sniffing.
- **Cookie Security Flags:** `HttpOnly` (blocks JavaScript `document.cookie` access) and `Secure` (ensures cookies travel only over TLS).
