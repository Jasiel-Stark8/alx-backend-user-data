#!/usr/bin/env python3
"""Password Encryption Module"""
import bcrypt

def hash_password(password: str) -> str:
    """Password hashing function"""
    return bcrypt.hashpw(password)
