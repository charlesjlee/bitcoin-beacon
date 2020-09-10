'''
API doc
https://blockchain.info/q/

or
https://rest.bitcoin.com/
'''

from datetime import datetime
import requests
import hashlib
# from binascii import hexlify, unhexlify
import hmac
from math import ceil
import json
hash_len = 32


def latest_block_hash():
    """Return the latest block hash."""
    r = requests.get('https://blockchain.info/q/latesthash')
    
    if r.status_code != 200:
        # throw error
        pass
    
    return r.text

def block_header_raw(block_hash):
    """Return a raw block header given its hash."""
    r = requests.get(f"https://blockchain.info/block/{block_hash}?format=hex")
    
    if r.status_code != 200:
        # throw error
        pass
    
    return r.text[:160]

def block_info(block_hash):
    """Return block info given its hash."""
    r = requests.get(f"https://blockchain.info/rawblock/{block_hash}")
    
    if r.status_code != 200:
        # throw error
        pass
    
    return r.json()

def hmac_sha256(key, data):
    """Generate pseudo-random-keyed (PRK-keyed) hash-block"""
    return hmac.new(key, data, hashlib.sha256).digest()

def hkdf(length, ikm, salt=b"", info=b""):
    """Generate cryptographically strong output key material (OKM) of any desired length.
    
    Repeatedly generate pseudo-random-keyed (PRK-keyed) hash-blocks, append them into
    the output key material, and finally truncate to the desired length.
    
    """
    prk = hmac_sha256(salt, ikm)
    t = b""
    okm = b""
    for i in range(ceil(length / hash_len)):
        t = hmac_sha256(prk, t + info + bytes([1+i]))
        okm += t
    return okm[:length]

latest_block_hash = latest_block_hash()
print(f"{latest_block_hash=}")

latest_block_info = block_info(latest_block_hash)
print(f"latest_block_number={latest_block_info['height']}")

block_header_raw = block_header_raw(latest_block_hash)
print(f"{block_header_raw[:10]=}")

# compute and verify the block hash
# headerHex = block_header_raw
# headerUnhex = unhexlify(headerHex) # convert to binary
# headerHash = hashlib.sha256(hashlib.sha256(headerUnhex).digest()).digest() # hash twice using SHA256
# computedHash = str(hexlify(headerHash[::-1]), 'utf-8') # flip to big-endian

# if latest_block_hash != computedHash:
#     print(f"hash mis-match! latest_block_hash is {latest_block_hash} but computedHash is {computedHash}")
#     # throw error
    
# convert inputs to binary
# (prepend then strip '1' to preserve leading zeros)
header_bin = bin(int('1'+block_header_raw, 16))[3:] # 640 bits
blockHash_bin = bin(int('1'+latest_block_hash, 16))[3:] # 256 bits

# build input and feed to hkdf()
extractorInput = int(header_bin,2) | int(blockHash_bin,2)
extractorInput = bin(extractorInput)[2:].zfill(640)
print(f"extractorInput ({len(extractorInput)} bits):\n{extractorInput}")

extractorInputBytes = extractorInput.encode('utf-8') # convert to bytes
extractorOutputBytes = hkdf(4, extractorInputBytes)
extractorOutput = bin(int.from_bytes(extractorOutputBytes, 'big'))[2:].zfill(32)
print(f"extractorOutput aka beacon output ({len(extractorOutput)} bits):\n{extractorOutput}")
print(f"{int(extractorOutput,2)}")

data = {
    'block_hash': latest_block_hash,
    'timestamp': datetime.utcfromtimestamp(int(latest_block_info['time'])).strftime('%Y-%m-%d %H:%M:%S'),
    'random_binary': extractorOutput,
    'random_int': int(extractorOutput,2),
    'block':latest_block_info['height'],
}

print(f"json: {json.dumps(data)}")

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"{dir_path=}")

import os
cwd = os.getcwd()
print(f"{cwd=}")

import os.path
print(os.path.isfile("../data/random.json"))
print(os.path.isfile("./data/random.json"))
print(os.path.isfile("data/random.json"))

with open('data/random.json', 'w') as outfile:
    json.dump(data, outfile)