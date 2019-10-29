import time
import hashlib
import bcrypt
import math

n = 1000000
key = b"STR"

print(f"Hashing {n}x") 

start_time = time.time()
for i in range(n):
    hash(key)
end_time = time.time()
print (f"  Python hash runtime: {end_time - start_time} seconds")

sha_start_time = time.time()
for i in range(n):
    hashlib.sha256(key)
sha_end_time = time.time()
print (f"  SHA256 hash runtime: {sha_end_time - sha_start_time} seconds")


def djb2(key):
    '''
    DJB2 hash
    '''
    # Start from an arbitrary large prime
    hash_value = 5381
    # Bit-shift and sum value for each character
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value

start_time = time.time()
for i in range(n):
    djb2(key)
end_time = time.time()
print(f"  DJB2 hash runtime: {end_time - start_time} seconds")

bcrypt_n=5
print(f"\nHashing {bcrypt_n}x")
salt = bcrypt.gensalt()
start_time = time.time()
for i in range(bcrypt_n):
    bcrypt.hashpw(b"KEY",salt)
end_time = time.time()
print(f"  bcrypt hash runtime: {end_time - start_time} seconds")

sha_time = sha_end_time - sha_start_time
bcrypt_time = end_time - start_time
difference = (bcrypt_time / sha_time) * (n / bcrypt_n)
print(f"\n** Bcrypt {math.floor(difference)} times slower than SHA256! **")