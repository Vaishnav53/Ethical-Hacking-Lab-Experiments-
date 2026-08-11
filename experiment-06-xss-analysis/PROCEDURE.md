# Experiment 06: Step-by-Step Practical Procedure

---

## 🛑 MANUAL LAB EXECUTION CHECKPOINT

```text
============================================================
MANUAL LAB EXECUTION REQUIRED
============================================================
Experiment:          06 — Cross-Site Scripting (XSS) Analysis
Target:              DVWA XSS Reflected & Stored modules
Required Environment: Kali Linux VM + DVWA target container/VM
Purpose:             Demonstrate harmless proof-of-concept Reflected & Stored XSS and verify HTML entity encoding defenses
Expected Evidence:   1. Reflected & Stored PoC request log (outputs/xss-payloads.txt)
                     2. Screenshot showing execution of harmless alert PoC (screenshots/06-01-xss-reflected.png)
============================================================
```

---

## 🛠️ Practical Procedure

### Step 1: Execute Reflected XSS Proof of Concept
1. Open DVWA in Kali browser, set Security Level to **Low**, and navigate to **XSS (Reflected)**.
2. Enter the harmless alert payload into the `What's your name?` input box:
   ```html
   <script>alert('Reflected-XSS-Lab-06')</script>
   ```
3. Click Submit.
4. *Observation:* The browser displays an JavaScript alert dialog titled `Reflected-XSS-Lab-06`.

---

### Step 2: Execute Stored XSS Proof of Concept
1. Navigate to **XSS (Stored)** module in DVWA.
2. Enter Name: `LabTester` and Message:
   ```html
   <script>alert('Stored-XSS-Lab-06')</script>
   ```
3. Click Submit.
4. Refresh the page or log out and back in as another user.
5. *Observation:* The stored comment automatically triggers the alert modal window upon every page load.

---

### Step 3: Verify Output Encoding Defense
1. Switch DVWA Security Level to **High** or **Impossible**.
2. Resubmit payload `<script>alert('XSS')</script>`.
3. Inspect Page Source (`Ctrl+U`):
   ```html
   <!-- Output rendered safely as harmless text text string -->
   Hello, &lt;script&gt;alert(&#039;XSS&#039;)&lt;/script&gt;
   ```
4. *Result:* Script tags are safely encoded as entity strings and executed as literal text by the browser parser.

---

## 📷 Screenshot Checklist

1. `06-01-xss-reflected.png`: Browser pop-up modal showing `alert('Reflected-XSS-Lab-06')` execution in DVWA.
2. `06-02-xss-encoding-fix.png`: Page source view showing encoded HTML entities (`&lt;script&gt;`).
