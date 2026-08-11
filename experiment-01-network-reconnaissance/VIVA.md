# Experiment 01: Viva Voce Examination Questions & Answers

---

### Q1: What is the fundamental difference between passive and active reconnaissance?
**Answer:** Passive reconnaissance gathers information without directly sending network packets to the target system (e.g., querying WHOIS databases, DNS records, or OSINT search engines). Active reconnaissance involves sending packets directly to the target system (e.g., ICMP pings, port scans), which carries a risk of detection by firewalls and Intrusion Detection Systems (IDS).

---

### Q2: Why is ARP pinging preferred over ICMP echo pinging during local network discovery?
**Answer:** ARP (Address Resolution Protocol) operates at Layer 2 (Data Link Layer) and cannot be blocked by operating system host firewalls (such as Windows Firewall or iptables). On a local Ethernet segment, host firewalls frequently drop ICMP Echo requests (Layer 3), but hosts must respond to ARP requests to maintain network communication.

---

### Q3: What DNS record type performs reverse name resolution (IP address to domain name)?
**Answer:** The **PTR (Pointer) record**, stored in `in-addr.arpa` domain zones, maps an IPv4 address to its corresponding fully qualified domain name (FQDN).

---

### Q4: Explain the function of the Nmap option `-sn`.
**Answer:** The `-sn` flag tells Nmap to perform "Host Discovery Only" (formerly known as `-sP` or ping scan) and skip port scanning. It identifies which target hosts are online without scanning individual TCP/UDP ports.

---

### Q5: How does a TCP SYN ping (`-PS`) determine if a host is alive?
**Answer:** Nmap sends an empty TCP packet with the SYN flag set to a destination port (e.g., port 80). If the host is alive and the port is open, it responds with a SYN-ACK packet. If the port is closed, it responds with a RST (Reset) packet. In both cases, receiving a packet confirms the host is active.

---

### Q6: What information does a WHOIS query provide?
**Answer:** WHOIS provides domain registration records, including domain registrar, creation and expiration dates, authoritative name servers, and administrative/technical contact details (unless protected by WHOIS privacy proxy).

---

### Q7: Why must active reconnaissance be strictly limited to authorized lab IP ranges?
**Answer:** Active scanning against unauthorized targets can be interpreted as an attempted network intrusion under cybercrime laws (e.g., Section 43/66 of India's IT Act 2000), trigger automated IP bans, and violate ISP terms of service.

---

### Q8: What does the Nmap output status `Host is up` signify?
**Answer:** It indicates that Nmap received at least one valid response (ICMP Echo reply, ARP reply, TCP SYN-ACK, or TCP RST) from the target IP address during the host discovery phase.

---

### Q9: How does DIG differ from NSLOOKUP?
**Answer:** `dig` (Domain Information Groper) is a flexible CLI tool that outputs raw DNS server responses directly, displaying precise flags, TTL values, and section headers. `nslookup` is an older, legacy lookup utility that formats DNS output for display.

---

### Q10: How can network administrators mitigate active network discovery probes?
**Answer:** Mitigation includes configuring host and network firewalls to drop ICMP echo requests, disabling unused network ports, enforcing strict VLAN isolation, and employing Intrusion Prevention Systems (IPS) to detect and block port sweeps.
