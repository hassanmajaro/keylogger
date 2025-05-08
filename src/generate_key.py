from cryptography.fernet import Fernet
import os

# Define path to save the key
key_path = os.path.join(os.path.dirname(__file__), '../fernet.key')

# Generate key
key = Fernet.generate_key()

# Save the key to a file
with open(key_path, 'wb') as key_file:
    key_file.write(key)

print(f"[+] Key generated and saved to {key_path}")
