# Security Tool Command Reference Guide

---

## 🔍 Nmap Syntax Cheat Sheet

| Task | Command Template | Options & Description |
| :--- | :--- | :--- |
| **Ping Sweep (Host Discovery)** | `nmap -sn <SUBNET_RANGE>` | `-sn`: Disable port scan; perform host discovery only |
| **SYN Stealth Scan** | `sudo nmap -sS -p- <TARGET_LAB_IP>` | `-sS`: Stealth SYN scan; `-p-`: Scan all 65535 ports |
| **Service & OS Detection** | `nmap -sV -O <TARGET_LAB_IP>` | `-sV`: Determine service/version info; `-O`: Enable OS detection |
| **Aggressive Scan** | `nmap -A <TARGET_LAB_IP>` | `-A`: Enables OS detection, version detection, script scanning, and traceroute |
| **Save Scan Output** | `nmap -sV <TARGET_LAB_IP> -oN scan.txt` | `-oN`: Normal output to text file |
| **NSE Vulnerability Script Scan** | `nmap --script vuln <TARGET_LAB_IP>` | `--script vuln`: Execute Nmap Scripting Engine (NSE) vulnerability categories |

---

## 🌐 HTTP & Web Security Commands

```bash
# Inspect Web Server Response Headers
curl -i -s http://<LAB_TARGET>/

# Follow Redirects and Show SSL Certificate Details
curl -v -k https://<LAB_TARGET>/

# Send POST Request with URL-encoded Parameters
curl -X POST -d "username=admin&password=password123" http://<LAB_TARGET>/login.php
```

---

## 🦈 Wireshark CLI (TShark) Filters

```bash
# Capture packets on Host-Only Interface eth0
tshark -i eth0 -w capture.pcap

# Display HTTP POST requests containing potential credentials
tshark -r capture.pcap -Y 'http.request.method == "POST"' -T fields -e http.file_data

# Display SYN Packets (TCP Handshake Initialization)
tshark -r capture.pcap -Y 'tcp.flags.syn == 1 && tcp.flags.ack == 0'
```
