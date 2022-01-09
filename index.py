#pip install cryptography
from cryptography.fernet import Fernet
# need to generate a key to encrypt and decrypt data.
# generate a key using Fernet for encryption and decryption
key = Fernet.generate_key()
f = Fernet(key)
# encrypting the string
token = f.encrypt(b"Hello, how are you guyz.")
print('encrypted data = ',token)
# decrypting the encrypted data
decrypt = f.decrypt(token)
print('decrypted data = ', decrypt)

 
