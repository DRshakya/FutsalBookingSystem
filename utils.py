import uuid
from datetime import datetime
from django.contrib.auth.hashers import (
    PBKDF2PasswordHasher, SHA1PasswordHasher, BCryptSHA256PasswordHasher
)
import time

def print_timestamp(timestamp):
    dt_object = datetime.fromtimestamp(timestamp/1000)
    return dt_object.strftime('%Y-%m-%d %H:%M:%S')


def password_verify(raw_password, hashed_password):
    hash = PBKDF2PasswordHasher()
    return hash.verify(raw_password, hashed_password)

def password_hash(raw_password):
    hash = PBKDF2PasswordHasher()
    password_salt = hash.salt()
    return hash.encode(raw_password, password_salt)

def generate_uuid():
    return str(uuid.uuid4())

def timestamp():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return int(round(timestamp * 1000))