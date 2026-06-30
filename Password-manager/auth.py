import hashlib
import hmac
import logging
import os
from typing import Optional, Tuple

from database import get_master, store_master

logger = logging.getLogger(__name__)

# PBKDF2 Configuration
ITERATIONS = 200_000
HASH_NAME = "sha256"


def register_master(password: str) -> None:
    """
    Register a new master password by securely hashing it with PBKDF2-HMAC.
    """
    if not password:
        raise ValueError("Master password cannot be empty.")

    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        HASH_NAME,
        password.encode("utf-8"),
        salt,
        ITERATIONS,
    ).hex()

    store_master(password_hash, salt.hex())


def verify_master(password: str) -> Tuple[bool, Optional[str]]:
    """
    Verify the master password.

    Returns:
        (True, salt_hex) if authentication succeeds,
        otherwise (False, None).
    """
    try:
        data = get_master()

        if data is None:
            return False, None

        stored_hash, salt_hex = data
        salt = bytes.fromhex(salt_hex)

        test_hash = hashlib.pbkdf2_hmac(
            HASH_NAME,
            password.encode("utf-8"),
            salt,
            ITERATIONS,
        ).hex()

        if hmac.compare_digest(test_hash, stored_hash):
            return True, salt_hex

        return False, None

    except Exception:
        logger.exception("Failed to verify master password.")
        return False, None
