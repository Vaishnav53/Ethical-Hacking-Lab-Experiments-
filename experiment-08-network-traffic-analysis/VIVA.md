# Experiment 08: Viva Voce Examination Questions & Answers

---

### Q1: What is Promiscuous Mode on a Network Interface Card (NIC)?
**Answer:** Promiscuous mode allows a NIC to capture and pass all network frames passing across the physical or virtual Ethernet segment to the operating system protocol stack, regardless of whether the destination MAC address matches the interface's own address.

---

### Q2: Why is transmitting credentials over unencrypted HTTP insecure?
**Answer:** Unencrypted HTTP transmits data in raw ASCII text across the network. Anyone on the local network path (or operating an ARP spoofing man-in-the-middle attack) can read sensitive POST request bodies, passwords, and session cookies using basic packet sniffers.

---

### Q3: What protocol provides encryption and data integrity for HTTPS?
**Answer:** **Transport Layer Security (TLS)** (specifically TLS 1.2 or TLS 1.3).

---

### Q4: Explain the difference between Wireshark Capture Filters and Display Filters.
**Answer:** Capture Filters (written using pcap syntax before starting capture, e.g., `host 192.168.56.102`) dictate which packets are recorded to disk. Display Filters (written using Wireshark display syntax during or after capture, e.g., `http.request.method == "POST"`) hide unneeded packets from view without discarding recorded raw capture data.

---

### Q5: What does the Wireshark feature "Follow TCP Stream" do?
**Answer:** It extracts, orders, and reassembles fragmented TCP segment payloads belonging to a specific 4-tuple TCP connection (Source IP, Source Port, Destination IP, Destination Port), displaying the complete bidirectional application-layer conversation in plaintext.

---

### Q6: How does HTTPS prevent passive network eavesdropping?
**Answer:** HTTPS uses TLS asymmetric cryptography (RSA / ECDHE) during the initial handshake to authenticate server identity and establish symmetric encryption keys (AES-GCM / ChaCha20). All subsequent HTTP request headers, URIs, cookies, and payloads are encrypted using symmetric keys, appearing as random ciphertext to passive eavesdroppers.

---

### Q7: What display filter isolates DNS lookup packets in Wireshark?
**Answer:** `dns` or `udp.port == 53`.

---

### Q8: What is a PCAP file?
**Answer:** PCAP (Packet Capture) is a standard file format specification (supported by libpcap and WinPcap/Npcap) used to store captured network interface packets for offline analysis by security utilities like Wireshark, TShark, and Snort.

---

### Q9: Can an eavesdropper read HTTP session cookies over unencrypted Wi-Fi?
**Answer:** Yes. On an unencrypted or open Wi-Fi network (or HTTP website lacking TLS), session cookies (e.g., `PHPSESSID`) travel in plaintext within HTTP request `Cookie:` headers, allowing attackers to clone cookies and hijack active user sessions.

---

### Q10: How can organizations protect sensitive traffic from packet analysis on internal networks?
**Answer:** By enforcing mandatory HTTPS (HSTS), enforcing TLS 1.3 across internal web portals, implementing Virtual Private Networks (IPsec / WireGuard) for remote connections, and employing 802.1X network access control with dynamic WPA3 Enterprise encryption.
