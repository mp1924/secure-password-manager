import hashlib
import base64
import os
from cryptography.fernet import Fernet


# ---------------- KEY DERIVATION ----------------
def derive_key(password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    )
    return base64.urlsafe_b64encode(key)


# ---------------- ENCRYPT / DECRYPT ----------------
def create_cipher(key):
    return Fernet(key)


def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()


def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()
