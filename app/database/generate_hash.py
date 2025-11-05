import bcrypt

def generate_bcrypt_hash(password):
    """Generate a bcrypt hash for a password"""
    # Generate salt and hash
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password, hash_value):
    """Verify a password against a bcrypt hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hash_value.encode('utf-8'))

if __name__ == "__main__":
    # Generate hash for admin1234
    password = "admin123"
    hash_value = generate_bcrypt_hash(password)
    print(f"Password: {password}")
    print(f"Hash: {hash_value}")
    
    # Verify the hash
    is_valid = verify_password(password, hash_value)
    print(f"Verification: {is_valid}")
