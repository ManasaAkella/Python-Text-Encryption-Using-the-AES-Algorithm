from cryptography.fernet import Fernet

def generate_key():
  """Generates a random key for encryption."""
  key = Fernet.generate_key()
  return key

def encrypt(message, key):
  """Encrypts a message using the given key."""
  cipher = Fernet(key)
  encrypted_text = cipher.encrypt(message.encode())
  return encrypted_text

def decrypt(encrypted_text, key):
  """Decrypts an encrypted message using the given key."""
  cipher = Fernet(key)
  decrypted_text = cipher.decrypt(encrypted_text).decode()
  return decrypted_text

# Example usage
key = generate_key()
message = "This is a message created by me"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
