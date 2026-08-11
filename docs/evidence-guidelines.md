# Practical Evidence Capture & Verification Guidelines

---

## 📷 Overview & Integrity Standard

In ethical hacking assessments and academic laboratory evaluation, evidence integrity is essential. 

> [!IMPORTANT]
> Practical evidence consists of **verifiable outputs generated during real execution**. Fabricated terminal logs, artificial scan outputs, or synthetic screenshots are strictly prohibited.

---

## 🖼️ Screenshot Standard Operating Procedure (SOP)

### 1. Requirements for Valid Screenshots
- **Terminal Visibility:** Every screenshot must show the complete terminal window, including the command prompt (`user@kali:~$` or `root@kali:~#`).
- **Timestamp & System Context:** The command prompt or terminal title bar must show the system hostname and current time, or `date` must be executed prior to the main command.
- **Target IP Visible:** The target IP address (`<TARGET_LAB_IP>`) must be explicitly visible in the executed command line or application URL bar.
- **Uncropped Full Window:** Do not crop screenshots tightly around text. Capture the entire terminal or application viewport to preserve context.

### 2. Naming Convention for Screenshots
Format: `<EXP_NO>-<STEP_ID>-<SHORT_DESCRIPTION>.png`

*Examples:*
- `01-01-target-discovery.png`
- `02-02-nmap-service-scan.png`
- `05-03-sqli-union-payload.png`
- `08-01-wireshark-http-post.png`

---

## 📄 Raw Output Log Standard

In addition to screenshots, raw text outputs of terminal commands must be saved in the experiment `outputs/` folder using stdout redirection or Nmap output flags (`-oN` / `-oA`).

*Examples:*
```bash
# Save normal Nmap scan output to output file
nmap -sV -O 192.168.56.102 -oN outputs/nmap-service-scan.txt

# Pipe terminal output using tee to capture stderr and stdout
python3 test_auth.py 2>&1 | tee outputs/auth-test-run.log
```

---

## 🔐 Log Integrity & Hashing

To ensure non-repudiation, students can generate SHA-256 checksums of captured raw output files:

```bash
sha256sum outputs/* > evidence/checksums.sha256
```
