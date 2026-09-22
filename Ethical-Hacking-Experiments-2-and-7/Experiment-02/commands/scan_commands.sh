#!/usr/bin/env bash
# ==============================================================================
# Experiment 02: Port Scanning and Service Enumeration
# Course: MR23-1CS0432 - Ethical Hacking Laboratory (Malla Reddy University)
# Target: Metasploitable 2 VM (192.168.1.3 / Host-Only Network)
# Attacker: Kali Linux (192.168.1.4)
# ==============================================================================

TARGET_IP="192.168.1.3"

echo "[*] Step 1: Discovering and confirming target on local subnet..."
ip a
sudo nmap -sn 192.168.1.0/24

echo "[*] Step 2: Executing full TCP port scan (all 65,535 ports)..."
sudo nmap -p- $TARGET_IP -oN ../evidence/nmap-full-tcp.txt

echo "[*] Step 3: Executing service version and operating system detection..."
sudo nmap -sV -O $TARGET_IP -oN ../evidence/nmap-services.txt

echo "[*] Step 4: Executing UDP port scan on top 20 ports..."
sudo nmap -sU --top-ports 20 $TARGET_IP -oN ../evidence/nmap-udp.txt

echo "[+] Experiment 02 scanning sequence completed successfully."
