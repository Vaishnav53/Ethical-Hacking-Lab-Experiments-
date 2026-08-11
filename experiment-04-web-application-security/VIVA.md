# Experiment 04: Viva Voce Examination Questions & Answers

---

### Q1: What is the OWASP Top 10?
**Answer:** The OWASP (Open Worldwide Application Security Project) Top 10 is a regularly updated awareness document outlining the ten most critical security risks facing web applications globally, serving as a benchmark for web application security auditing.

---

### Q2: Explain the purpose of the `HttpOnly` flag on session cookies.
**Answer:** The `HttpOnly` flag instructs client web browsers that the cookie must not be accessed via client-side scripts (such as `document.cookie` in JavaScript). This mitigates the risk of session hijacking in the event of a Cross-Site Scripting (XSS) vulnerability.

---

### Q3: What risk does a missing `X-Frame-Options` header introduce?
**Answer:** Missing `X-Frame-Options` allows an attacker to embed the target website within a transparent `<iframe>` on a malicious site, facilitating **Clickjacking** attacks where users are tricked into performing unintended actions.

---

### Q4: What is the function of `Content-Security-Policy` (CSP)?
**Answer:** CSP is an HTTP header that allows site administrators to declare approved dynamic resources (JavaScript, CSS, Images, Frames) that the browser is allowed to load and execute, significantly mitigating XSS and data injection attacks.

---

### Q5: How does directory brute-forcing work (e.g., using `dirb` or `gobuster`)?
**Answer:** Directory brute-forcing utilities send sequential HTTP GET/HEAD requests for common directory and file names loaded from a dictionary wordlist (e.g., `/admin`, `/backup`, `/db`) and analyze returned HTTP status codes (`200`, `403`, `301`) to map hidden endpoints.

---

### Q6: What is Security Misconfiguration (OWASP A05:2021)?
**Answer:** Security Misconfiguration occurs when web servers, database engines, or frameworks are left with default configuration settings, default administrative credentials, open storage buckets, enabled verbose error messages disclosing stack traces, or missing security headers.

---

### Q7: Explain the difference between HTTP GET and HTTP POST requests regarding sensitive data.
**Answer:** GET request parameters are appended directly to the URL query string, causing sensitive data (passwords, tokens) to be exposed in browser history, proxy logs, web server access logs, and HTTP Referer headers. POST requests transmit parameters inside the HTTP request body, which is not logged in server URL logs and remains encrypted over TLS.

---

### Q8: What does the `X-Content-Type-Options: nosniff` header do?
**Answer:** It prevents client web browsers from performing MIME-type sniffing (inferring a file's format independently of the `Content-Type` header), forcing the browser to adhere strictly to the declared MIME type and preventing executable code injection via uploaded text or image files.

---

### Q9: How can web server banner disclosure (e.g., `Server: Apache/2.2.8`) assist an attacker?
**Answer:** Detailed server banners inform attackers of exact software vendor versions operating on the target, allowing them to search CVE databases for known unpatched exploits specifically matching those versions.

---

### Q10: What is Broken Access Control (OWASP A01:2021)?
**Answer:** Broken Access Control occurs when application authorization checks fail to enforce user role boundaries, allowing unauthenticated or low-privileged users to view, modify, or delete sensitive data or execute administrative functions belonging to other users.
