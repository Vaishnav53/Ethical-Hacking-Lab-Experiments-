# Safety Policy and Ethical Scope Guidelines

---

## 🏛️ Educational Scope & Legal Boundary Policy

This repository forms an integral part of the academic curriculum for **MR23-1CS0432: Ethical Hacking** at **Malla Reddy University (MRU)**.

The primary goal of ethical hacking education is to understand offensive security methodologies, vulnerability concepts, and technical exploitation vectors solely to construct effective defensive controls, implement secure coding standards, and harden enterprise systems.

---

## 🛑 Absolute Prohibitions (Zero Tolerance Rules)

> [!CAUTION]
> Violation of these rules constitutes academic misconduct under Malla Reddy University regulations and may constitute a criminal offense under the Information Technology Act (2000 / Amendment 2008) of India.

1. **Unauthorized Public Targets:**
   - NEVER execute port scans, vulnerability scans, exploit tools, web application attacks, or credential brute-forcing against any public Internet target, domain name, public IP address, or third-party web service.
2. **University Infrastructure Protection:**
   - NEVER target Malla Reddy University networks, Wi-Fi access points, learning management systems (LMS), administrative servers, host workstations, or student computers.
3. **No Ransomware, Malware, or Rootkit Development:**
   - DO NOT write, test, compile, or distribute ransomware, bootkits, keyloggers, fileless malware, or destructive payloads.
4. **No Uncontrolled Propagation:**
   - Network tools must remain bound to local subnet ranges (`192.168.56.0/24`). Automatic scanning across external interfaces or public subnets is strictly forbidden.
5. **No Host Weakening:**
   - Students must not disable Windows Defender, endpoint detection software, or host firewalls on physical lab or personal host workstations.

---

## ✅ Permitted Scope & Authorized Targets

All security testing procedures in this repository are strictly authorized **ONLY** under the following conditions:

- **Target System 1:** Metasploitable 2 / 3 Virtual Machine operating inside VirtualBox/VMware on a Host-Only virtual network.
- **Target System 2:** Damn Vulnerable Web Application (DVWA) / WebGoat hosted within local docker containers or dedicated lab VMs.
- **Target System 3:** The educational local authentication test application provided in `experiment-07-password-authentication/`.
- **Target Network:** Isolated virtual Ethernet network (`192.168.56.0/24` or equivalent Host-Only virtual interface).

---

## ⚖️ Legal & Regulatory Reference (India)

Students must strictly abide by relevant sections of the **Information Technology Act, 2000 (India)**:

- **Section 43:** Penalty and compensation for damage to computer, computer system, etc. (Unauthorized access, downloading data, introducing viruses).
- **Section 66:** Computer related offenses (Dishonestly or fraudulently committing acts referred to in section 43).
- **Section 66B:** Punishment for dishonestly receiving stolen computer resource or communication device.
- **Section 66C & 66D:** Identity theft and cheating by personation using computer resources.

---

## 🔒 Responsible Vulnerability Handling & Non-Fabrication

1. **Non-Fabrication Policy:**
   - All screenshots, terminal outputs, vulnerability assessment reports, and execution timestamps must represent real execution conducted by the student in Kali Linux.
   - Fabricating scan output, CVE results, or exploitation proof is prohibited and invalidates lab assessment.
2. **Cleanup & State Recovery:**
   - After completing an experiment, target virtual machines must be reset to clean snapshots (`Initial-Clean-State`) to ensure reproducibility for peer students and evaluators.
