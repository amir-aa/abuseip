import secrets

def generate_api_key(length=64):
    """Generate a secure API key"""
    return secrets.token_hex(length)
