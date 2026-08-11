# Ethical Hacking Laboratory Troubleshooting & Diagnostics Guide

---

## 🔧 Common Laboratory Setup & Network Issues

### Issue 1: Target VM (Metasploitable/DVWA) Not Obtaining IP Address
**Symptom:** Running `ifconfig` or `ip a` on Metasploitable shows no IPv4 address on `eth0`.
**Cause:** VirtualBox DHCP server disabled or host adapter misconfigured.
**Resolution:**
1. In VirtualBox, go to **Tools -> Network Manager -> Host-only Networks**.
2. Select your adapter (e.g., `VirtualBox Host-Only Ethernet Adapter`).
3. Ensure **Enable Server** is checked under the DHCP Server tab.
4. Reboot Metasploitable: `sudo reboot` or `sudo dhclient eth0`.

---

### Issue 2: Kali Linux Cannot Ping Target VM
**Symptom:** `ping <TARGET_LAB_IP>` returns `Destination Host Unreachable` or 100% packet loss.
**Cause:** VMs attached to different virtual network adapters or interface down.
**Resolution:**
1. Check VM Network Settings in VirtualBox:
   - Both Kali Linux and Target VM **must** be attached to `Host-Only Adapter`.
   - Ensure both VMs use the exact same adapter name (e.g., `VirtualBox Host-Only Ethernet Adapter`).
2. On Kali, check interface state:
   ```bash
   sudo ip link set eth0 up
   sudo dhclient eth0
   ```
3. Run ARP scan to find target IP:
   ```bash
   sudo netdiscover -i eth0 -r 192.168.56.0/24
   ```

---

### Issue 3: Nmap Scan Returns "All 1000 scanned ports are filtered"
**Symptom:** Nmap scan output shows no open ports.
**Cause:** Target IP is incorrect, VM is suspended, or target firewall blocking probes.
**Resolution:**
1. Verify target VM status in VirtualBox (ensure it is running, not paused).
2. Verify target IP address by logging directly into the Metasploitable terminal console (`msfadmin:msfadmin`) and running `ifconfig`.
3. Try Nmap ICMP bypass flags:
   ```bash
   sudo nmap -Pn -sS <TARGET_LAB_IP>
   ```

---

### Issue 4: Python Test Application Import Error in Experiment 07
**Symptom:** `ModuleNotFoundError: No module named 'cryptography'` or similar when running `python app.py`.
**Cause:** Missing standard Python dependencies.
**Resolution:**
1. Ensure Python 3.10+ is installed: `python --version`.
2. Install standard dependencies from Experiment 07 requirements file:
   ```bash
   pip install -r experiment-07-password-authentication/scripts/requirements.txt
   ```

---

### Issue 5: Wireshark Promiscuous Mode Permission Denied on Kali
**Symptom:** Wireshark shows error "No interfaces found" or "Permission denied on /dev/bpf* / raw socket".
**Cause:** Wireshark executed without administrative privileges.
**Resolution:**
1. Execute Wireshark with `sudo`:
   ```bash
   sudo wireshark
   ```
2. Or add non-root user to `wireshark` group:
   ```bash
   sudo usermod -aG wireshark $USER
   newgrp wireshark
   ```

---

## 🆘 Reporting Unresolved Lab Issues

If an issue persists after trying the above steps:
1. Capture terminal error message or screenshot.
2. Note your Hypervisor version, host OS, and IP configurations (`ip a` or `ipconfig`).
3. Log the issue following `templates/evidence-log-template.md`.
