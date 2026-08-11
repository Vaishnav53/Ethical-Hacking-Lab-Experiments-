# Educational Laboratory Architecture & Component Design

---

## 🏛️ System Architecture Diagram

```mermaid
graph TD
    subgraph Host Workstation ["Host Workstation (Windows / macOS / Linux)"]
        HV["Hypervisor (VirtualBox / VMware)"]
        
        subgraph Isolated Network ["Host-Only Virtual Network (192.168.56.0/24)"]
            KALI["Attacker VM: Kali Linux 2024.x<br/>IP: 192.168.56.101<br/>Tools: Nmap, Wireshark, Burp, Python"]
            META["Target VM 1: Metasploitable 2/3<br/>IP: 192.168.56.102<br/>Services: FTP, SSH, Telnet, HTTP, MySQL, SMB"]
            DVWA["Target VM 2: OWASP BWA / DVWA<br/>IP: 192.168.56.103<br/>Services: HTTP (Apache/MySQL/PHP)"]
        end
    end
    
    KALI -->|"Active Recon / Scanning (Exps 01-03)"| META
    KALI -->|"Web Vulnerability Assessments (Exps 04-06)"| DVWA
    KALI -->|"Traffic Sniffing (Exp 08)"| Isolated Network
    KALI -->|"Controlled Exploitation (Exp 09)"| META
    
    style Host Workstation fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Isolated Network fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style KALI fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
    style META fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style DVWA fill:#ffe0b2,stroke:#f57c00,stroke-width:2px
```

---

## 🧱 Component Specification

### 1. Attacker Workstation (Kali Linux)
- **Role:** Primary security testing platform.
- **Operating System:** Kali Linux 2024.x (64-bit).
- **Core Toolset:** Nmap, Wireshark, Burp Suite Community, Netcat, Python 3, OpenSSL, Git.
- **Network Interface:** `eth0` assigned via Host-Only DHCP (`192.168.56.101`).

### 2. Infrastructure Target (Metasploitable 2)
- **Role:** Intentionally vulnerable Linux virtual machine simulating unpatched enterprise servers.
- **Vulnerabilities Present:** Unpatched Linux kernel, weak passwords (`msfadmin:msfadmin`), legacy services (vsftpd 2.3.4, bind9, Samba 3.0.20, distcc).
- **Network Interface:** `eth0` assigned via Host-Only DHCP (`192.168.56.102`).

### 3. Application Target (DVWA / OWASP BWA)
- **Role:** Intentionally vulnerable web application platform.
- **Vulnerabilities Present:** OWASP Top 10 vulnerabilities (SQLi, XSS, Command Injection, CSRF, Insecure Deserialization).
- **Network Interface:** `eth0` assigned via Host-Only DHCP (`192.168.56.103`).

---

## 🔐 Isolation Controls Matrix

- **Network Routing:** Subnet `192.168.56.0/24` has no default gateway pointing to the physical router.
- **DNS Resolution:** Local `/etc/hosts` file mappings only; no external DNS resolution.
- **Packet Filtering:** Host firewall permits traffic between VM interfaces while dropping outbound forwarding to physical network adapters (`eth0` on physical host).
