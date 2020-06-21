from Crypto.Random import get_random_bytes, random
import sys, secrets, string
import json
from Crypto.Cipher import AES


# Hashed password as encryption secret key
key = get_random_bytes(16)


# Create dictionary of secrets
print("_" * 20)
print("Dictionary")
dictionary = {
  "name": "Alice",
  "Secret1": 1,
  "Secret2": "My second secret"
}
print(dictionary)


# Converting dictionary to binary string
print("_" * 20)
print("Binary String")
binaryString = json.dumps(dictionary).encode()
print(binaryString)


# Encrypt binary string and send cipthertext and nonce to server storage
print("_" * 20)
print("Encrypted")
cipher = AES.new(key, AES.MODE_EAX)
cipthertext, nonce = cipher.encrypt(binaryString), cipher.nonce
print(cipthertext)


# Get encrypted secret and nonce from server and decrypt
print("_" * 20)
print("Decrypted")
cipher2 = AES.new(key, AES.MODE_EAX, nonce=nonce)
dec = cipher2.decrypt(cipthertext).decode()
print(dec)


# Create secret dictionary from string 
print("_" * 20)
print("Dictionary")
end = json.loads(dec)
print(end)

assert(end == dictionary)
