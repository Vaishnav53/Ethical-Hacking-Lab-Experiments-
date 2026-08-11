"""
CLI Educational Demonstration: Password Hashing, Salting & Brute-Force Testing
MR23-1CS0432 Ethical Hacking Laboratory - Malla Reddy University
"""

import sys
import os
from auth_engine import AuthEngine

def print_banner():
    print("=" * 65)
    print("  EXPERIMENT 07: PASSWORD SECURITY & AUTHENTICATION ENGINE  ")
    print("  Course: MR23-1CS0432 - Ethical Hacking Laboratory (MRU)   ")
    print("=" * 65)

def main():
    print_banner()
    engine = AuthEngine(max_failed_attempts=3, lockout_duration_seconds=10)

    # 1. Compare Insecure MD5 vs Secure PBKDF2 Hashing
    sample_pwd = "LaboratoryPassword2026!"
    print(f"\n[1] Password Hashing & Salt Demonstration")
    print(f"Raw Input Password: {sample_pwd}")
    print(f"Password Entropy:   {engine.calculate_entropy(sample_pwd):.2f} bits")

    md5_hash = engine.hash_password_insecure_md5(sample_pwd)
    print(f"\n[INSECURE] Unsalted MD5 Hash: {md5_hash}")

    pbkdf2_hash1, salt1 = engine.hash_password_pbkdf2(sample_pwd)
    pbkdf2_hash2, salt2 = engine.hash_password_pbkdf2(sample_pwd)

    print(f"\n[SECURE] PBKDF2 (Run 1):")
    print(f"   Salt 1 (Hex):  {salt1.hex()}")
    print(f"   Hash 1 (Hex):  {pbkdf2_hash1}")

    print(f"\n[SECURE] PBKDF2 (Run 2 - Same Password, New CSPRNG Salt):")
    print(f"   Salt 2 (Hex):  {salt2.hex()}")
    print(f"   Hash 2 (Hex):  {pbkdf2_hash2}")

    # 2. Register synthetic laboratory user
    test_user = "student_admin"
    print(f"\n[2] Registering Synthetic User '{test_user}'...")
    registered = engine.register_user(test_user, sample_pwd)
    print(f"Registration Status: {'SUCCESS' if registered else 'FAILED'}")

    # 3. Simulate Brute-Force & Rate-Limiting Account Lockout
    print(f"\n[3] Simulating Failed Login Attacks & Account Lockout Defense:")
    fake_passwords = ["123456", "admin123", "wrong_pass", "LaboratoryPassword2026!"]

    for pwd in fake_passwords:
        success, msg = engine.authenticate_user(test_user, pwd)
        status_icon = "[SUCCESS]" if success else "[DENIED]"
        print(f"Attempting '{pwd}' -> {status_icon}: {msg}")

    print("\n" + "=" * 65)
    print("  LOCAL PRACTICAL EXECUTION TEST COMPLETED SUCCESSFULLY  ")
    print("=" * 65)

if __name__ == "__main__":
    main()
