# Experiment 02: Viva Voce Examination Questions & Answers

---

### Q1: What is the main operational difference between a SYN scan (`-sS`) and a Connect scan (`-sT`)?
**Answer:** A SYN scan (`-sS`) performs a half-open scan by sending a SYN packet and tearing down the connection with a RST packet as soon as SYN-ACK is received, without completing the 3-way handshake. A Connect scan (`-sT`) completes the full 3-way handshake using the OS `connect()` system call, making it slower and easily logged by target application servers.

---

### Q2: Why requires a TCP SYN scan root privileges in Linux?
**Answer:** A SYN scan requires crafting raw IP packets and manipulating TCP header flags directly, which requires raw socket (`SOCK_RAW`) access restricted to `root` or users with `CAP_NET_RAW` capabilities.

---

### Q3: What does the Nmap port state `filtered` mean?
**Answer:** It means Nmap cannot determine whether the port is open or closed because network packet filtering (such as a firewall rule, router ACL, or host firewall) is dropping probe packets before they reach the target port or blocking response packets.

---

### Q4: How does Nmap perform OS fingerprinting (`-O`)?
**Answer:** Nmap sends up to 16 TCP, UDP, and ICMP probes to open and closed ports on the target host. It analyzes subtle differences in responses—such as TCP Window Size, IP ID sequence generation, TCP Options ordering, and ICMP error quotes—and matches these metrics against its `nmap-os-db` signature file.

---

### Q5: Why is UDP scanning significantly slower than TCP scanning?
**Answer:** UDP is a connectionless protocol that does not use handshakes or SYN/ACK responses. Open UDP ports rarely send responses to probes, while closed UDP ports respond with ICMP Port Unreachable packets. Operating system kernels rate-limit ICMP error responses (e.g., Linux limits ICMP error messages to 1 per second), causing UDP scans across 65,535 ports to take hours.

---

### Q6: What is banner grabbing and how does Nmap `-sV` implement it?
**Answer:** Banner grabbing connects to open ports and records the initial welcome message or protocol banner sent by the listening daemon (e.g., `220 vsFTPd 2.3.4`). Nmap `-sV` sends targeted probe strings defined in `nmap-service-probes` and uses regex matching to parse vendor, product name, and version numbers.

---

### Q7: Explain the timing templates in Nmap (`-T0` through `-T5`).
**Answer:** Nmap timing templates control scan speed and parallelism: `-T0` (Paranoid) and `-T1` (Sneaky) delay probes to evade IDS; `-T2` (Polite) reduces bandwidth consumption; `-T3` (Normal) is default; `-T4` (Aggressive) speeds up scans on reliable local lab networks; `-T5` (Insane) sacrifices accuracy for maximum speed.

---

### Q8: What command scans all 65,535 TCP ports?
**Answer:** `nmap -p- <TARGET_LAB_IP>` or `nmap -p 1-65535 <TARGET_LAB_IP>`.

---

### Q9: How can an administrator prevent version disclosure via banner grabbing?
**Answer:** Administrators can reconfigure service daemons to hide or customize version banners (e.g., setting `ServerTokens Prod` in Apache, `ServerSignature Off`, or editing `banner` parameters in SSH/FTP configs).

---

### Q10: What is the purpose of Nmap Output flags `-oN`, `-oX`, and `-oG`?
**Answer:** `-oN` outputs scan results in human-readable Normal text format; `-oX` outputs structured XML format for parsing by vulnerability management tools; `-oG` outputs Grepable format for shell text processing.
