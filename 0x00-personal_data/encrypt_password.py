#!/usr/bin/env python3
"""Password Encryption and Validation Module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Password hashing function"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Password Validation"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
