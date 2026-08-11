# Vulnerability Reporting & Risk Severity Guidelines

---

## 📊 CVSS v3.1 Rating Scale

Vulnerabilities discovered during laboratory assessments are categorized according to the **Common Vulnerability Scoring System (CVSS) v3.1**:

| Severity Rating | CVSS Base Score Range | Example Vulnerabilities | Action / Remediation Priority |
| :--- | :--- | :--- | :--- |
| **Critical** | `9.0 - 10.0` | Remote Code Execution (vsftpd 2.3.4 backdoor), Unauthenticated SQLi | Immediate Emergency Mitigation |
| **High** | `7.0 - 8.9` | Authenticated Command Injection, Stored XSS in Admin Portal | High Priority Patching |
| **Medium** | `4.0 - 6.9` | Reflected XSS, Weak Password Policy, Missing CSRF Tokens | Scheduled Remediation |
| **Low** | `0.1 - 3.9` | Information Disclosure (Server Version Banners, Verbose Errors) | Low Priority / Hardening |
| **None / Info** | `0.0` | Open Ports running secure services (HTTPS with TLS 1.3) | Informational |

---

## 📄 Structure of a Vulnerability Finding Entry

Every identified vulnerability report entry in student lab submissions must include:

1. **Vulnerability Title:** Concise, descriptive title (e.g., *Vsftpd 2.3.4 Backdoor Command Execution*).
2. **Target Identifier:** IP address and Port/Service affected (e.g., `192.168.56.102:21/TCP`).
3. **CVE ID:** Common Vulnerabilities and Exposures identifier (e.g., `CVE-2011-2523`).
4. **CVSS v3.1 Score:** Base score and vector string.
5. **Technical Description:** Concise explanation of why the vulnerability exists (e.g., unsanitized input, hardcoded credentials).
6. **Proof of Concept (PoC):** Step-by-step reproduction steps with exact CLI commands or HTTP request payloads.
7. **Impact Analysis:** Potential real-world damage if exploited by an attacker (Confidentiality, Integrity, Availability).
8. **Remediation & Secure Code Fix:** Actionable steps to patch the vulnerability (e.g., upgrading software package, implementing parameterized SQL queries, configuring strict CSP headers).
