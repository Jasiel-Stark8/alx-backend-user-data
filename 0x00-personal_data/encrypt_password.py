#!/usr/bin/env python3
"""Password Encryption Module"""
import bycrpt

def hash_password(password: str) -> str:
    """Password hashing function"""
    return bycrpt.hashpw(password)
