#!/usr/bin/env python3
"""Password Encryption Module"""
import bcrypt

def hash_password(password: str) -> bytes:
    """Password hashing function"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
