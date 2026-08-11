# Experiment 06: Cross-Site Scripting (XSS) Analysis

[![Course: MR23-1CS0432](https://img.shields.io/badge/Course-MR23--1CS0432-blue.svg)](file:///d:/Ethical%20Hacking%20Experiments/README.md)
[![Status: Ready for Kali](https://img.shields.io/badge/Status-Ready%20for%20Kali-orange.svg)](file:///d:/Ethical%20Hacking%20Experiments/EXPERIMENT_STATUS.md)

---

## 📌 Experiment Metadata

- **Experiment Number:** `06`
- **Title:** Cross-Site Scripting (XSS) Analysis
- **Course Mapping:** `MR23-1CS0432` — Ethical Hacking Laboratory (Malla Reddy University)
- **Target Application:** DVWA (XSS Reflected & Stored modules - `http://<LAB_TARGET>/dvwa/`)
- **Attacker System:** Kali Linux VM (`192.168.56.101`)

---

## 🎯 Aim & Objectives

### Aim
To analyze client-side security risks associated with Cross-Site Scripting (XSS), evaluate Reflected, Stored, and DOM-based XSS attack vectors, inspect HTML entity output encoding defenses, and configure Content Security Policy (CSP) headers.

---

## 📂 Directory Layout

```text
experiment-06-xss-analysis/
├── README.md         # Summary & metadata
├── THEORY.md         # Reflected vs Stored vs DOM XSS, Sources & Sinks, Context-Aware Encoding, CSP
├── PROCEDURE.md      # Practical harmless PoC execution steps & secure encoding verification
├── VIVA.md           # 10+ Viva Voce questions and answers
├── commands/         # (.gitkeep)
├── outputs/          # (.gitkeep)
├── screenshots/      # (.gitkeep)
└── reports/          # (.gitkeep)
```
