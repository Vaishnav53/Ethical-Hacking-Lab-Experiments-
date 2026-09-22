# Experiment 02: Port Scanning and Service Enumeration

**Course:** MR23-1CS0432 — Ethical Hacking Laboratory | **Institution:** Malla Reddy University

## Summary

Full TCP and UDP port scan + service/version enumeration against Metasploitable 2 (192.168.1.3) using Nmap 7.99 from Kali Linux on an isolated VirtualBox Host-Only network.

## Evidence Status: ✅ COMPLETE — Authentic Kali Linux execution

| Step | Command | Evidence |
|---|---|---|
| Network config | `ip a` / `ifconfig` | `screenshots/02-01-network-configuration.png` |
| Full TCP scan | `sudo nmap -p- 192.168.1.3` | `screenshots/02-02-full-tcp-port-scan.png` + `evidence/nmap-full-tcp.txt` |
| Service/OS detection | `sudo nmap -sV -O 192.168.1.3` | `screenshots/02-03-service-os-detection.png` + `evidence/nmap-services.txt` |
| UDP scan | `sudo nmap -sU --top-ports 20 192.168.1.3` | `screenshots/02-04-udp-port-scan.png` + `evidence/nmap-udp.txt` |

## Key Findings

- **30 open TCP ports** discovered (including 4 high-numbered: 35034, 39119, 54575, 59207)
- **vsftpd 2.3.4** — CVE-2011-2523 backdoor identified via service banner
- **Port 1524** — Pre-configured Metasploitable root shell (bindshell)
- **OS:** Linux 2.6.9–2.6.33 (end-of-life kernel)
- **UDP:** DNS (53), NetBIOS-NS (137) confirmed open

## Report

📄 [Experiment-02-Final-Report.pdf](report/Experiment-02-Final-Report.pdf) — 16 pages
