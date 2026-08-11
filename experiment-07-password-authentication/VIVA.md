# Experiment 07: Viva Voce Examination Questions & Answers

---

### Q1: Why is MD5 completely unsuitable for password hashing in modern systems?
**Answer:** MD5 is a fast cryptographic hash function capable of computing billions of hashes per second on consumer GPUs. It lacks salt support, is vulnerable to collision attacks, and allows attackers to compute rainbow tables or perform offline brute-force attacks in seconds.

---

### Q2: What is a Cryptographic Salt and why must it be unique per user?
**Answer:** A salt is a random sequence of bytes generated via a CSPRNG and stored alongside the password hash. A unique salt ensures that two users with identical passwords produce distinct stored hashes, rendering precomputed rainbow table attacks useless and forcing attackers to brute-force each user hash individually.

---

### Q3: What is a Key Derivation Function (KDF) and how does it differ from a standard hash function?
**Answer:** A KDF (such as PBKDF2, bcrypt, or Argon2) is intentionally designed to be computationally slow and resource-intensive by applying configurable iteration counts or memory-hard cost factors, dramatically slowing down offline brute-force attacks.

---

### Q4: Explain the difference between Argon2d, Argon2i, and Argon2id.
**Answer:** Argon2 won the Password Hashing Competition (PHC). Argon2d maximizes resistance against GPU cracking (suitable for cryptocurrency); Argon2i uses data-independent memory access to prevent side-channel attacks (suitable for passphrases); Argon2id is a hybrid combining both, recommended for general password hashing.

---

### Q5: What is Password Entropy?
**Answer:** Password entropy measures the unpredictability and randomness of a password expressed in bits of information ($E = L \times \log_2(R)$). Higher entropy indicates exponential difficulty for brute-force cracking tools.

---

### Q6: What is a Timing Attack in authentication systems and how is it mitigated?
**Answer:** A timing attack measures minor variations in string comparison execution times (e.g., standard `if hash1 == hash2`) to determine how many initial characters match. It is mitigated using constant-time comparison functions like `hmac.compare_digest()`.

---

### Q7: Explain Credential Stuffing.
**Answer:** Credential stuffing is an automated attack where bots test stolen pairs of usernames and passwords (obtained from prior third-party data breaches) against login portals of unrelated web applications, exploiting user password reuse habits.

---

### Q8: What is the recommended minimum iteration count for PBKDF2-HMAC-SHA256 according to OWASP / NIST?
**Answer:** NIST / OWASP recommends at least **600,000 iterations** for PBKDF2-HMAC-SHA256 (or 210,000 for PBKDF2-HMAC-SHA512) to ensure sufficient offline brute-force resistance.

---

### Q9: Why is storing plain-text passwords considered a critical flaw?
**Answer:** Storing passwords in plaintext exposes all user credentials immediately if the database is accessed via SQL injection, stolen backups, or unauthorized insider access, compromising user accounts across multiple services.

---

### Q10: How does Account Lockout rate-limiting protect against online brute-force attacks?
**Answer:** Account lockout tracks consecutive invalid authentication attempts and temporarily suspends authentication for a specified duration (e.g., 15 minutes after 5 failed attempts), throttling automated dictionary attacks down to negligible speeds.
