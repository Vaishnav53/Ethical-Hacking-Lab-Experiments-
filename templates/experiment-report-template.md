# Official Experiment Report Template

**Course:** MR23-1CS0432 Ethical Hacking Laboratory  
**Institution:** Malla Reddy University (MRU)  
**Department:** Computer Science & Engineering (Cybersecurity)  

---

## 📌 Experiment Information

- **Experiment Number:** `[e.g., 01]`
- **Experiment Title:** `[e.g., Network Reconnaissance and Information Gathering]`
- **Student Name:** `[Student Name]`
- **Roll Number:** `[Hall Ticket / Roll Number]`
- **Date of Execution:** `[YYYY-MM-DD]`
- **Environment:** Kali Linux VM (`192.168.56.101`) -> Target VM (`192.168.56.X`)

---

## 🎯 1. Aim & Objectives

### Aim
`[State the primary aim of the experiment as per syllabus]`

### Objectives
1. `[Objective 1]`
2. `[Objective 2]`
3. `[Objective 3]`

---

## 📖 2. Theoretical Background & Key Concepts

`[Provide a textbook-grade theoretical summary of key concepts involved in this experiment]`

---

## 🏗️ 3. Laboratory Architecture & Target Topology

```text
Attacker System: Kali Linux 2024.x (IP: 192.168.56.101)
Target System:   [Metasploitable 2 / DVWA] (IP: <TARGET_LAB_IP>)
Network Mode:    VirtualBox Host-Only Adapter (192.168.56.0/24)
```

---

## 🛠️ 4. Tools & Prerequisites

- **Attacker OS:** Kali Linux
- **Tools Used:** `[e.g., Nmap, Wireshark, Burp Suite]`
- **Target OS/App:** `[e.g., Metasploitable 2 / DVWA]`

---

## 📝 5. Step-by-Step Practical Procedure & Command Logs

### Step 1: Environment Verification & Reachability Test
```bash
ping -c 4 <TARGET_LAB_IP>
```
*Observation:* `[Record ICMP response status]`

### Step 2: Primary Execution Phase
```bash
[Insert exact command executed in Kali terminal]
```
*Command Breakdown:*
- `[flag 1]`: `[Explanation of option]`
- `[flag 2]`: `[Explanation of option]`

*Observation / Raw Output Summary:*
```text
[Paste terminal stdout or output summary]
```

---

## 📷 6. Screenshot Evidence Verification

| Fig # | Description | Filename | Verified? |
| :---: | :--- | :--- | :---: |
| 1 | Target Connectivity & Ping Check | `01-target-discovery.png` | [ ] |
| 2 | Main Execution & Results | `02-scan-results.png` | [ ] |

---

## 🔒 7. Vulnerability Analysis & Risk Interpretation

`[If vulnerabilities were identified, document CVSS score, impact, and root cause]`

---

## 🛡️ 8. Defensive Mitigation & Secure Configuration

`[Explain how system administrators or developers can prevent or mitigate the identified risk]`

---

## 🔄 9. Post-Lab State Reset & Cleanup

`[Document steps taken to restore target VM snapshots or clear temporary execution logs]`

---

## 🏁 10. Result & Conclusion

`[Summarize the outcome of the experiment and confirm objective completion]`

---

## ❓ 11. Viva Voce Q&A

1. **Q:** `[Question 1]`  
   **A:** `[Answer 1]`
2. **Q:** `[Question 2]`  
   **A:** `[Answer 2]`
