"""
AuthEngine: Modern Password Hashing and Security Testing Engine
MR23-1CS0432 Ethical Hacking Laboratory - Malla Reddy University
"""

import hashlib
import hmac
import secrets
import math
import time

class AuthEngine:
    def __init__(self, max_failed_attempts=5, lockout_duration_seconds=30):
        # Database in-memory store: {username: {"salt": bytes, "hash": str, "algo": str}}
        self.user_db = {}
        # Failed login tracker: {username: {"failed_count": int, "lockout_until": float}}
        self.login_tracker = {}
        self.max_failed_attempts = max_failed_attempts
        self.lockout_duration = lockout_duration_seconds

    @staticmethod
    def calculate_entropy(password: str) -> float:
        """Calculates password entropy in bits: E = L * log2(R)"""
        if not password:
            return 0.0
        charset = 0
        if any(c.islower() for c in password):
            charset += 26
        if any(c.isupper() for c in password):
            charset += 26
        if any(c.isdigit() for c in password):
            charset += 10
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            charset += 32

        if charset == 0:
            charset = 128
        return len(password) * math.log2(charset)

    @staticmethod
    def hash_password_insecure_md5(password: str) -> str:
        """INSECURE: Fast unsalted MD5 hash (Demonstration only)"""
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_password_pbkdf2(password: str, salt: bytes = None, iterations: int = 100000) -> tuple[str, bytes]:
        """SECURE: PBKDF2-HMAC-SHA256 with CSPRNG Salt and high iteration count"""
        if salt is None:
            salt = secrets.token_bytes(16)
        derived_key = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode('utf-8'),
            salt=salt,
            iterations=iterations,
            dklen=32
        )
        return derived_key.hex(), salt

    def register_user(self, username: str, password: str) -> bool:
        """Registers user with PBKDF2 salted hash"""
        if username in self.user_db:
            return False
        pwd_hash, salt = self.hash_password_pbkdf2(password)
        self.user_db[username] = {
            "salt": salt,
            "hash": pwd_hash,
            "algo": "pbkdf2_hmac_sha256"
        }
        self.login_tracker[username] = {"failed_count": 0, "lockout_until": 0.0}
        return True

    def authenticate_user(self, username: str, password: str) -> tuple[bool, str]:
        """Authenticates user with rate limiting and constant-time hash comparison"""
        if username not in self.user_db:
            return False, "Invalid credentials"

        tracker = self.login_tracker[username]
        current_time = time.time()

        # Check account lockout status
        if current_time < tracker["lockout_until"]:
            remaining = int(tracker["lockout_until"] - current_time)
            return False, f"Account locked due to multiple failed attempts. Try again in {remaining} seconds."

        user_record = self.user_db[username]
        salt = user_record["salt"]
        stored_hash = user_record["hash"]

        computed_hash, _ = self.hash_password_pbkdf2(password, salt=salt)

        # Constant-time comparison to prevent timing attacks
        if hmac.compare_digest(computed_hash, stored_hash):
            tracker["failed_count"] = 0
            tracker["lockout_until"] = 0.0
            return True, "Authentication successful!"
        else:
            tracker["failed_count"] += 1
            if tracker["failed_count"] >= self.max_failed_attempts:
                tracker["lockout_until"] = current_time + self.lockout_duration
                return False, f"Account locked! Exceeded max failed attempts ({self.max_failed_attempts})."
            attempts_left = self.max_failed_attempts - tracker["failed_count"]
            return False, f"Invalid credentials. Attempts remaining before lockout: {attempts_left}"
