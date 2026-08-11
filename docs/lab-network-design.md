# Lab Network Design & Subnet Architecture

---

## 📡 Subnet Plan

| Component | Interface | Network Type | Subnet Range | Static / DHCP IP | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Virtual Host Interface** | `vboxnet0` / Host Adapter | Host-Only | `192.168.56.0/24` | `192.168.56.1` | Host Hypervisor Virtual Gateway |
| **DHCP Server** | VirtualBox DHCP | Host-Only | `192.168.56.0/24` | `192.168.56.2` | Assigns IPs `.100` to `.200` |
| **Kali Attacker VM** | `eth0` | Host-Only | `192.168.56.0/24` | `192.168.56.101` | Penetration Testing System |
| **Metasploitable Target** | `eth0` | Host-Only | `192.168.56.0/24` | `192.168.56.102` | Server Target VM |
| **DVWA Web Target** | `eth0` | Host-Only | `192.168.56.0/24` | `192.168.56.103` | Web App Vulnerability Target |

---

## 🔒 Isolation Rules & Interface Bindings

1. **No External Forwarding:** IP Forwarding (`sysctl net.ipv4.ip_forward`) is permanently set to `0` on the physical host machine.
2. **Strict Host-Only Adapter Association:** Target VMs must NOT possess a second NIC set to NAT, NAT Network, or Bridged.
3. **No Dual-Homed Target Vulnerabilities:** Placing target VMs on NAT networks exposes vulnerable services to external networks via UPnP or automatic port mappings.

---

## 🛠️ Verification Commands

Run the following commands inside Kali Linux to confirm network state:

```bash
# Display IP configuration
ip addr show eth0

# Check default gateway (Should show no external WAN gateway)
ip route show

# Verify ARP table entries for target discovery
ip neighbor show
```
