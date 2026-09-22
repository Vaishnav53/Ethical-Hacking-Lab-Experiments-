# Experiment 07: Password Security and Authentication Testing

**Course:** MR23-1CS0432 — Ethical Hacking Laboratory | **Institution:** Malla Reddy University

## Summary

Local Python authentication engine demonstrating: unsalted MD5 vs PBKDF2-HMAC-SHA256 with CSPRNG salts, password entropy measurement, account lockout rate-limiting, and automated unit testing.

## Evidence Status: ✅ COMPLETE — Live Python execution (September 22, 2026)

| Step | Command | Result | Evidence |
|---|---|---|---|
| Unit tests | `python -m unittest discover -s scripts/tests -p "test_*.py" -v` | Ran 4 tests in 0.161s — **OK** | `screenshots/07-02-unit-test-pass.png` + `evidence/unit-test-results.txt` |
| Interactive CLI | `python scripts/app.py` | All demonstrations completed | `screenshots/07-01-auth-test-app-run.png` + `evidence/auth-engine-run.txt` |

## Key Results

| Metric | Value |
|---|---|
| MD5 hash of "LaboratoryPassword2026!" | `096b1f381d46137f604347537db76776` (deterministic) |
| PBKDF2 Run 1 salt | `fcd7d5c65d34c46348a007bdae2a3278` (CSPRNG) |
| PBKDF2 Run 2 salt | `aaa275edf37f18f86af01e845afb6fec` (different each run) |
| Password entropy | 150.76 bits (≫ 50-bit minimum threshold) |
| Lockout threshold | 3 failed attempts |
| Tests passed | 4/4 |

## Reproducing

```bash
# From Experiment-07/ directory — no packages to install:
python -m unittest discover -s scripts/tests -p "test_*.py" -v
python scripts/app.py
```

## Report

📄 [Experiment-07-Final-Report.pdf](report/Experiment-07-Final-Report.pdf) — 12 pages
