# Experiment 01: Network Reconnaissance and Information Gathering

**Course:** MR23-1CS0432 — Ethical Hacking Laboratory | **Institution:** Malla Reddy University

## Summary

Systematic network reconnaissance from Kali Linux — covering interface identification, gateway discovery, DNS information gathering, host discovery, port/service scanning, and OS fingerprinting.

## Evidence Status: ✅ COMPLETE — Authentic Kali Linux execution

All screenshots extracted from the original laboratory record (`ilovepdf_merged.pdf`).

| Step | Command | Result | Screenshot |
|---|---|---|---|
| 1 | `ip addr` | eth0 at 10.0.2.15/24 — UP | `01-01-ip-addr-network-interface.jpg` |
| 2 | `ip route` | Gateway: 10.0.2.2 | `01-02-ip-route-gateway.jpg` |
| 3 | `ping -c 4 8.8.8.8` | 0% loss, 65.797 ms avg | `01-03-ping-connectivity.jpg` |
| 4 | `cat /etc/resolv.conf` | DNS: 192.168.137.1 | `01-04-resolv-conf-dns.jpg` |
| 5 | `nslookup google.com 8.8.4.4` | 6 A + 4 AAAA records | `01-05-nslookup-dns-query.jpg` |
| 6 | `host google.com` | MX: smtp.google.com | `01-06-host-dns-records.jpg` |
| 7 | `dig google.com MX` | Priority 10, 27 ms | *(no screenshot — text only)* |
| 8 | `sudo nmap -sn 10.0.2.0/24` | 3 hosts discovered | `01-07`, `01-08` |
| 9 | `sudo nmap -sS -sV 10.0.2.2` | 135, 445, 5432 open | `01-09-nmap-service-scan.jpg` |
| 10 | `sudo nmap -sC -sV -p 135,445,5432 10.0.2.2` | SMB signing REQUIRED | *(text only)* |
| 11 | `sudo nmap -O -p 135,445,5432 10.0.2.2` | OS inconclusive (NAT bridge) | `01-10`, `01-11` |

## Report

📄 [Experiment-01-Final-Report.pdf](reports/Experiment-01-Final-Report.pdf)
