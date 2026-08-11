# Experiment 02: Step-by-Step Practical Procedure

---

## 🛑 MANUAL LAB EXECUTION CHECKPOINT

```text
============================================================
MANUAL LAB EXECUTION REQUIRED
============================================================
Experiment:          02 — Port Scanning and Service Enumeration
Target:              Metasploitable 2 VM (<TARGET_LAB_IP>)
Required Environment: Kali Linux VM + Metasploitable VM on Host-Only Network
Purpose:             Identify all open TCP/UDP ports, detect running service versions and OS
Expected Evidence:   1. Full 65535 TCP port scan output (outputs/nmap-full-tcp.txt)
                     2. Service version & OS detection log (outputs/nmap-services.txt)
                     3. Terminal screenshot showing service scan (screenshots/02-01-nmap-services.png)
============================================================
```

---

## 🛠️ Practical Procedure

### Step 1: Execute Full TCP Port Scan (All 65535 Ports)
Run a SYN stealth scan across all 65,535 TCP ports on the target VM:
```bash
sudo nmap -sS -p- -T4 <TARGET_LAB_IP> -oN outputs/nmap-full-tcp.txt
```
*Options:* `-sS` (SYN scan), `-p-` (ports 1-65535), `-T4` (aggressive timing template).

---

### Step 2: Perform Service Version & OS Fingerprinting Scan
Run service probe and OS detection against open ports discovered in Step 1:
```bash
sudo nmap -sV -O -p 21,22,23,25,53,80,139,445,3306,5432,6667,8080 <TARGET_LAB_IP> -oN outputs/nmap-services.txt
```

*Command Breakdown:*
- `-sV`: Service version detection.
- `-O`: OS fingerprinting.
- `-p ...`: Target specific open ports for fast banner grabbing.

---

### Step 3: Execute UDP Port Scan on Critical Services
Scan top UDP ports (DNS: 53, TFTP: 69, SNMP: 161):
```bash
sudo nmap -sU --top-ports 20 <TARGET_LAB_IP> -oN outputs/nmap-udp.txt
```

---

## 📷 Screenshot Checklist

1. `02-01-nmap-tcp-scan.png`: Terminal showing full TCP scan completion.
2. `02-02-service-os-fingerprint.png`: Terminal showing service versions (e.g., vsftpd 2.3.4, Apache 2.2.8, Linux kernel version).
