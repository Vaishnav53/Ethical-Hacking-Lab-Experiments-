# Experiment 08: Step-by-Step Practical Procedure

---

## 🛑 MANUAL LAB EXECUTION CHECKPOINT

```text
============================================================
MANUAL LAB EXECUTION REQUIRED
============================================================
Experiment:          08 — Network Traffic Analysis and Credential Exposure
Target:              Host-Only Interface eth0 + DVWA / Web Target (192.168.56.102)
Required Environment: Kali Linux VM + Target VM + Wireshark
Purpose:             Capture traffic during HTTP login attempt and reassemble TCP stream to observe plaintext credentials
Expected Evidence:   1. Wireshark PCAP capture file (saved locally in lab)
                     2. Plaintext HTTP POST extract log (outputs/wireshark-post-extract.txt)
                     3. Screenshot showing Follow TCP Stream containing plaintext login credentials (screenshots/08-01-plaintext-credentials.png)
============================================================
```

---

## 🛠️ Practical Procedure

### Step 1: Initialize Wireshark Capture on Host-Only Interface
1. Launch Wireshark in Kali terminal:
   ```bash
   sudo wireshark &
   ```
2. Select interface `eth0` (Host-Only Network) and start capture.

---

### Step 2: Generate Unencrypted HTTP Traffic
1. Open browser in Kali Linux and navigate to `http://<LAB_TARGET>/dvwa/login.php`.
2. Enter Username: `admin` and Password: `password123`. Click Login.

---

### Step 3: Apply Display Filter & Reassemble TCP Stream
1. In Wireshark, enter display filter: `http.request.method == "POST"`.
2. Right-click the captured `POST /dvwa/login.php` packet frame.
3. Select **Follow -> TCP Stream**.
4. *Observation:* The raw HTTP request stream displays plaintext POST body parameters:
   ```text
   POST /dvwa/login.php HTTP/1.1
   Host: 192.168.56.102
   Content-Type: application/x-www-form-urlencoded
   
   username=admin&password=password123&Login=Login
   ```

---

## 📷 Screenshot Checklist

1. `08-01-wireshark-http-post.png`: Wireshark interface displaying filtered HTTP POST request frame.
2. `08-02-tcp-stream-credentials.png`: Wireshark "Follow TCP Stream" window showing `username=admin&password=password123`.
