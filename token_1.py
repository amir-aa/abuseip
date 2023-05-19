import secrets

def generate_api_key(length=64):
    """Generate a secure API key"""
    return secrets.token_hex(length)
def GetLog(ip,key):
    with open('/var/log/ipabusekeylogs.log','a+') as filelog:
        filelog.write(f"{ip}:{key}")
        filelog.close()