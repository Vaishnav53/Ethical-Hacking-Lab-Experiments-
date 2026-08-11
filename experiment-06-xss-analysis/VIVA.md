# Experiment 06: Viva Voce Examination Questions & Answers

---

### Q1: Define Cross-Site Scripting (XSS).
**Answer:** XSS is a client-side code injection vulnerability occurring when a web application includes unsanitized user input in rendered web pages, allowing attackers to execute arbitrary JavaScript code within a victim's browser session.

---

### Q2: Compare Reflected XSS and Stored XSS.
**Answer:** Reflected XSS is non-persistent; the injected script travels inside the HTTP request payload and is echoed back in the immediate server response, requiring the victim to click a specially crafted link. Stored XSS is persistent; the script is saved permanently in the application backend database/storage and automatically executes whenever any user accesses the affected page.

---

### Q3: What is DOM-based XSS?
**Answer:** DOM-based XSS occurs entirely within the client-side browser DOM. Malicious input read from an untrusted source (like `location.search` or `location.hash`) is passed directly to an unsafe client-side sink (such as `eval()` or `innerHTML`) without going through server-side processing.

---

### Q4: How does HTML Entity Output Encoding mitigate XSS?
**Answer:** Output encoding converts dangerous HTML meta-characters into their corresponding harmless HTML entity representations (e.g., `<` becomes `&lt;`, `>` becomes `&gt;`, `"` becomes `&quot;`). When the browser DOM parser encounters these entities, it renders them as harmless literal text characters rather than executable HTML tags or script blocks.

---

### Q5: What browser security header helps block unauthorized script execution?
**Answer:** The **Content-Security-Policy (CSP)** HTTP response header (e.g., `Content-Security-Policy: default-src 'self'`).

---

### Q6: What cookie attribute prevents JavaScript from reading session tokens during an XSS attack?
**Answer:** The **`HttpOnly`** flag.

---

### Q7: Explain JavaScript DOM Sources and Sinks.
**Answer:** A **Source** is a DOM property that accepts untrusted client data (e.g., `location.search`, `document.referrer`, `window.name`). A **Sink** is a DOM function or element that executes or renders data passed to it (e.g., `element.innerHTML`, `document.write()`, `eval()`). Passing unvalidated data from a Source to a Sink creates DOM XSS.

---

### Q8: Is input validation alone sufficient to prevent XSS?
**Answer:** No. Input validation checks if data matches expected formats (e.g., email address structure). Context-aware output encoding applied at the exact point of rendering (HTML body, attribute, JavaScript block, CSS) is necessary because input valid for one context can be dangerous in another.

---

### Q9: What impact can an attacker achieve via successful Stored XSS?
**Answer:** An attacker can steal user session cookies (if missing `HttpOnly`), perform session hijacking, redirect users to phishing portals, capture keystrokes, modify page content (defacement), or trigger unauthorized actions on behalf of the victim user (CSRF escalation).

---

### Q10: Why should `eval()` be avoided in modern JavaScript development?
**Answer:** `eval()` executes arbitrary text strings as code statements with full access to surrounding scope variables, creating severe DOM XSS vulnerabilities if passed dynamic or user-controlled input strings.
