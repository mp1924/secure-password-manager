import hashlib
import os
from database import store_master, get_master
from crypto_utils import derive_key


# ---------------- REGISTER ----------------
def register_master(password):
    salt = os.urandom(16).hex()
    master_hash = hashlib.sha256((password + salt).encode()).hexdigest()

    store_master(master_hash, salt)


# ---------------- VERIFY ----------------
def verify_master(password):
    data = get_master()

    if not data:
        return False, None

    stored_hash, salt = data
    test_hash = hashlib.sha256((password + salt).encode()).hexdigest()

    if test_hash == stored_hash:
        return True, salt

    return False, None
