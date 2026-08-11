"""
Automated Unit Tests for AuthEngine
MR23-1CS0432 Ethical Hacking Laboratory - Malla Reddy University
"""

import unittest
import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auth_engine import AuthEngine

class TestAuthEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AuthEngine(max_failed_attempts=3, lockout_duration_seconds=2)

    def test_entropy_calculation(self):
        low_entropy = self.engine.calculate_entropy("abc")
        high_entropy = self.engine.calculate_entropy("P@ssw0rd2026!#$")
        self.assertGreater(high_entropy, low_entropy)

    def test_salting_uniqueness(self):
        pwd = "LabPassword123!"
        hash1, salt1 = self.engine.hash_password_pbkdf2(pwd)
        hash2, salt2 = self.engine.hash_password_pbkdf2(pwd)
        self.assertNotEqual(salt1, salt2)
        self.assertNotEqual(hash1, hash2)

    def test_user_registration_and_authentication(self):
        username = "alice"
        password = "SecurePassword123!"
        self.assertTrue(self.engine.register_user(username, password))
        
        # Successful login
        success, msg = self.engine.authenticate_user(username, password)
        self.assertTrue(success)
        self.assertIn("successful", msg.lower())

    def test_account_lockout(self):
        username = "bob"
        password = "CorrectPassword123!"
        self.engine.register_user(username, password)

        # Trigger 3 failed attempts
        self.engine.authenticate_user(username, "wrong1")
        self.engine.authenticate_user(username, "wrong2")
        success, msg = self.engine.authenticate_user(username, "wrong3")
        
        self.assertFalse(success)
        self.assertIn("locked", msg.lower())

        # Correct password should now be blocked during lockout window
        success_during_lockout, msg_during = self.engine.authenticate_user(username, password)
        self.assertFalse(success_during_lockout)
        self.assertIn("locked", msg_during.lower())

if __name__ == "__main__":
    unittest.main()
