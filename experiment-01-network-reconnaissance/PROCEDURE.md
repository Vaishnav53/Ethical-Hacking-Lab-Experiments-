# Experiment 01: Step-by-Step Practical Procedure

---

## 🛑 MANUAL LAB EXECUTION CHECKPOINT

```text
============================================================
MANUAL LAB EXECUTION REQUIRED
============================================================
Experiment:          01 — Network Reconnaissance and Information Gathering
Target:              Metasploitable 2 / Isolated VM
Required Environment: Kali Linux VM + Metasploitable VM on Host-Only Network (192.168.56.0/24)
Purpose:             Discover live target host IP address and perform passive/active reconnaissance
Expected Evidence:   1. Raw host discovery log (outputs/nmap-recon.txt)
                     2. Terminal screenshot showing active ping/nmap sweep (screenshots/01-01-target-discovery.png)
Where Saved:         experiment-01-network-reconnaissance/outputs/ & screenshots/
Conditions Required: Boot Kali VM & Metasploitable VM in VirtualBox. Verify Host-Only network adapter.
============================================================
```

---

## 🛠️ Step-by-Step Practical Instructions

### Step 1: Verify Attacker Network Configuration
Open terminal in Kali Linux and inspect your network interface:
```bash
ip addr show eth0
```
*Expected Result:* Interface `eth0` should display an IP address in the `192.168.56.x` range (e.g., `192.168.56.101`).

---

### Step 2: Passive Information Gathering (DNS & WHOIS Simulation)
Perform DNS lookup and WHOIS analysis using local domain lookup utilities:
```bash
# Query name servers and A records for target domain
dig +noall +answer example.com A NS

# Query WHOIS database (for public educational domain reference)
whois example.com | head -n 25
```
*Note:* In the isolated laboratory network, DNS lookups query local `/etc/hosts` or isolated DNS servers.

---

### Step 3: Local Network Host Discovery (Active Reconnaissance)
Execute an ARP ping sweep across the Host-Only subnet `192.168.56.0/24` to locate the target Metasploitable VM:
```bash
sudo netdiscover -i eth0 -r 192.168.56.0/24
```
*Alternative using Nmap:*
```bash
sudo nmap -sn 192.168.56.0/24 -oN outputs/nmap-host-discovery.txt
```

---

### Step 4: Reachability Verification & Round-Trip Timing
Once target IP is identified (e.g., `<TARGET_LAB_IP>` = `192.168.56.102`), send 4 ICMP echo requests:
```bash
ping -c 4 <TARGET_LAB_IP> | tee outputs/ping-verification.txt
```

---

### Step 5: Advanced Host Probing with Nmap
Execute combined ICMP + TCP SYN host discovery probe against the target:
```bash
sudo nmap -sn -PE -PS22,80,443 <TARGET_LAB_IP> -oN outputs/nmap-recon.txt
```

*Command Breakdown:*
- `-sn`: Host discovery only (disable port scanning).
- `-PE`: ICMP Echo Request ping.
- `-PS22,80,443`: TCP SYN ping to ports 22, 80, 443.
- `-oN outputs/nmap-recon.txt`: Save raw output in human-readable text format.

---

## 📷 Screenshot Checklist

1. `01-01-environment-check.png`: Terminal showing `ip addr` and `ping -c 4 <TARGET_LAB_IP>`.
2. `01-02-host-discovery-nmap.png`: Terminal showing `nmap -sn` discovery output.

---

## 🧹 Post-Lab Cleanup

```bash
# Verify outputs directory contains recorded logs
ls -la outputs/

# Reset target VM state in VirtualBox if required
```
