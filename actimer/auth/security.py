import hashlib

def encrypt(data):
    hashed_data = hashlib.sha256(data.encode("utf-8")).hexdigest()
    return hashed_data