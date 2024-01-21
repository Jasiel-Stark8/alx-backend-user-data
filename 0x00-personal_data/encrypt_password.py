#!/usr/bin/env python3
"""Password Encryption Module"""
import bcrypt

def hash_password(password: str) -> str:
    """Password hashing function"""
    encoded_pass = password.encode('utf-8')

    hashed = bcrypt.hashpw(encoded_pass, bcrypt.gensalt())

    return hashed
