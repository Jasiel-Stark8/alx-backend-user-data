#!/usr/bin/env python3
"""Password Encryption Module"""
import bcrypt

def hash_password(password: str) -> str:
    """Password hashing function"""
    return bcrypt.kdf(
        password=b'{password}',
        salt=b'salt')
    # encoded_pass = b'{password}'
    # return bcrypt.hashpw(encoded_pass, bcrypt.gensalt())
