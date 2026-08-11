# Experiment 07: Step-by-Step Practical Procedure

---

## 🛠️ Local & Kali Practical Instructions

This experiment features both a local educational test application (`scripts/app.py`) and Kali Linux authentication testing procedures.

### Step 1: Run Local Automated Unit Tests
Verify password entropy calculations, CSPRNG salting, and account lockout rate limiting:
```bash
python -m unittest discover -s scripts/tests -p "test_*.py" -v
```

---

### Step 2: Execute Interactive CLI Authentication Testing Engine
Run the CLI demonstration script:
```bash
python scripts/app.py
```
*Observations to Record:*
1. Compare raw MD5 output vs PBKDF2 salt outputs.
2. Note how two identical input passwords yield completely unique hashes when generated with unique 16-byte CSPRNG salts.
3. Observe how 3 consecutive invalid login attempts trigger account lockout.

---

## 📷 Screenshot Checklist

1. `07-01-auth-test-app-run.png`: Terminal execution output of `python scripts/app.py`.
2. `07-02-unit-test-pass.png`: Terminal output showing automated unit tests passing (`Ran 4 tests ... OK`).
