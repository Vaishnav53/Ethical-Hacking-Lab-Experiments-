# Laboratory Setup & Virtualization Architecture Guide

---

## 📋 Overview

This document provides step-by-step instructions for establishing an isolated, secure, and reproducible Ethical Hacking Laboratory environment using hypervisors such as **Oracle VirtualBox** or **VMware Workstation Pro/Player**.

All practical exercises for **MR23-1CS0432: Ethical Hacking** at Malla Reddy University are designed to operate exclusively within this isolated virtual network.

---

## 🏗️ Conceptual Laboratory Architecture

```text
+-------------------------------------------------------------------------+
|                              HOST SYSTEM                                |
|                        (Windows / macOS / Linux)                        |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  |                 HYPERVISOR (VirtualBox / VMware)                  |  |
|  |                                                                   |  |
|  |  +------------------------+             +----------------------+  |  |
|  |  |     ATTACKER VM        |             |      TARGET VM       |  |  |
|  |  |    (Kali Linux)        |             |   (Metasploitable)   |  |  |
|  |  |  IP: 192.168.56.101/24 |             | IP: 192.168.56.102/24|  |  |
|  |  +-----------+------------+             +----------+-----------+  |  |
|  |              |                                     |              |  |
|  |              +------------------+------------------+              |  |
|  |                                 |                                 |  |
|  |                  VIRTUAL ISOLATED NETWORK                         |  |
|  |                  Host-Only Network Adapter                        |  |
|  |                  Subnet: 192.168.56.0/24                          |  |
|  |                  DHCP: Enabled (192.168.56.100 - .200)             |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## 🌐 Virtual Network Configurations Explained

Understanding hypervisor virtual network adapters is critical for maintaining lab safety and preventing unauthorized external network interactions:

| Network Mode | Host Communication | Internet Access | Target-to-Host Risk | Recommended for Lab Target? |
| :--- | :--- | :--- | :--- | :--- |
| **NAT (Network Address Translation)** | Host can talk to VM via port forwarding | Yes (VM reaches Internet) | Low | ❌ No (For vulnerable targets) |
| **Bridged Adapter** | VM gets IP on physical LAN | Yes (Direct LAN access) | **CRITICAL HIGH** | ⛔ **NEVER** (Exposes vulnerable targets to real LAN) |
| **Host-Only Network** | Host & VMs communicate on isolated virtual NIC | **No** (No external traffic) | Minimal / Isolated | ✅ **PREFERRED / REQUIRED** |
| **Internal Network** | VMs talk only to each other (Host excluded) | **No** | None | ✅ **EXCELLENT FOR AIR-GAPPED LABS** |

> [!CAUTION]
> **NEVER configure Metasploitable, DVWA, or WebGoat with a Bridged Network Adapter!**
> Bridged mode assigns the vulnerable VM a public/physical IP address on your home or university Wi-Fi/Ethernet network, making it reachable and vulnerable to external attackers.

---

## 🛠️ Step-by-Step Laboratory Setup

### Phase 1: Hypervisor Installation
1. Download and install **Oracle VM VirtualBox** (v7.0+) or **VMware Workstation Pro/Player** on your host workstation.
2. Install the **VirtualBox Extension Pack** (matches hypervisor version) for USB and RDP passthrough support.

### Phase 2: Host-Only Network Configuration
1. Open VirtualBox -> **Tools** -> **Network Manager** -> **Host-only Networks**.
2. Click **Create** to initialize `vboxnet0` (Linux/macOS) or `VirtualBox Host-Only Ethernet Adapter` (Windows).
3. Configure Adapter Settings:
   - **IPv4 Address:** `192.168.56.1`
   - **IPv4 Network Mask:** `255.255.255.0`
4. Configure DHCP Server:
   - **Enable Server:** Checked
   - **Server Address:** `192.168.56.2`
   - **Server Mask:** `255.255.255.0`
   - **Lower Address Bound:** `192.168.56.100`
   - **Upper Address Bound:** `192.168.56.200`

### Phase 3: Attacker VM Setup (Kali Linux)
1. Download the pre-built **Kali Linux VirtualBox/VMware Image** (`.vbox` or `.ova`) from [kali.org](https://www.kali.org/get-kali/#kali-virtual-machines).
2. Import the appliance into VirtualBox.
3. Machine Settings:
   - **RAM:** 4096 MB (4 GB)
   - **Processors:** 2 vCPUs
   - **Network Adapter 1:** Host-Only Adapter (`VirtualBox Host-Only Ethernet Adapter`)
   - *(Optional)* **Network Adapter 2:** NAT (Only enabled when updating system packages, disabled during security experiments).

### Phase 4: Target VM Setup (Metasploitable 2/3 & DVWA)
1. Download **Metasploitable 2** zip archive and extract the `.vmdk` disk image.
2. Create a new Linux machine in VirtualBox (Ubuntu 64-bit profile).
3. Attach the existing `Metasploitable.vmdk` disk.
4. Machine Settings:
   - **RAM:** 512 MB – 1024 MB
   - **Processors:** 1 vCPU
   - **Network Adapter 1:** Host-Only Adapter (`VirtualBox Host-Only Ethernet Adapter`) **ONLY**.

---

## 🔍 Pre-Flight Lab Connectivity Verification

Before executing any experiment, run the following environment checks in Kali Linux:

```bash
# 1. Verify Kali IP assignment on the Host-Only network
ip a show eth0

# Expected output should display an IP in 192.168.56.x range
# Example: inet 192.168.56.101/24

# 2. Discover Target VM IP address using ARP Ping
sudo arping -c 3 -I eth0 192.168.56.102

# 3. Test ICMP Reachability
ping -c 4 192.168.56.102
```

---

## 📝 Safety Checklist Before Each Experiment

- [ ] Hypervisor network is set to **Host-Only** or **Internal Network**.
- [ ] No network adapter is set to **Bridged Mode**.
- [ ] Kali Linux can reach the target IP address via `ping` / `nmap`.
- [ ] Output directory (`outputs/`) and screenshot directory (`screenshots/`) exist for the target experiment.
- [ ] Target IP address is noted for replacing `<TARGET_LAB_IP>` placeholders.
