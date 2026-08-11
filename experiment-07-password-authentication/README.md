# Experiment 07: Password Security and Authentication Testing

[![Course: MR23-1CS0432](https://img.shields.io/badge/Course-MR23--1CS0432-blue.svg)](file:///d:/Ethical%20Hacking%20Experiments/README.md)
[![Status: Ready for Practical](https://img.shields.io/badge/Status-Locally%20Tested%20%26%20Verified-green.svg)](file:///d:/Ethical%20Hacking%20Experiments/EXPERIMENT_STATUS.md)

---

## 📌 Experiment Metadata

- **Experiment Number:** `07`
- **Title:** Password Security and Authentication Testing
- **Course Mapping:** `MR23-1CS0432` — Ethical Hacking Laboratory (Malla Reddy University)
- **Target Application:** Educational Local Authentication Engine (`scripts/app.py`)
- **Execution Platform:** Windows Host & Kali Linux VM (Python 3.10+)

---

## 🎯 Aim & Objectives

### Aim
To analyze modern authentication mechanisms, evaluate cryptographic password hashing algorithms, understand salt generation using CSPRNGs, enforce password entropy policies, build failed-login rate limiting, and compare legacy insecure designs against modern secure authentication engineering.

---

## 📂 Directory Layout

```text
experiment-07-password-authentication/
├── README.md         # Summary & metadata
├── THEORY.md         # Cryptographic hashes (MD5 vs PBKDF2/Argon2), Salting, Rainbow Tables, Entropy
├── PROCEDURE.md      # CLI application usage guide & test suite execution
├── VIVA.md           # 10+ Viva Voce questions and answers
├── scripts/
│   ├── requirements.txt   # Dependency file (Python standard library compatible)
│   ├── auth_engine.py     # Core cryptographic hashing & auth security module
│   ├── app.py             # Interactive CLI educational auth testing application
│   └── tests/
│       └── test_auth.py   # Automated unit test suite verifying auth controls
├── outputs/          # Execution output logs (.gitkeep)
├── screenshots/      # (.gitkeep)
└── reports/          # (.gitkeep)
```

---

## 🧪 Local Execution Verification

The local Python application and automated test suite have been built and tested on host.

Run test suite:
```bash
python -m unittest discover -s experiment-07-password-authentication/scripts/tests -p "test_*.py" -v
```
