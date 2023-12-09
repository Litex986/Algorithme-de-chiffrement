import random
import hashlib

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

class Key:
    def __init__(self, key):
        self.KEY = key
        self.key_base = []  # will contain 4 keys to generate self.keys
        self.keys = [[], [], [], []]  # [[keys for layer(0)], [keys for mainLoop()], [keys for layer(2)], [keys for intermediate step]]

    def deriveKeys(self, key, num_keys, exit=32):  # deriveKeys(self, key to be derived, number of keys needed, length of output keys)
        '''
        Allows derivation of a key into multiple keys without reversible possibility using sha256.
        Uses HKDF for creating sub-keys.
        '''
        master_key_bytes = key.encode('utf-8')
        random.seed(hashlib.sha256(key.encode('utf-8')).hexdigest())
        salt = random.randbytes(256)
        derived_keys = [
            hashlib.sha256(
                HKDF(
                    algorithm=hashes.SHA256(),
                    length=exit,  # output length
                    salt=salt,  # salt for regenerating keys with the same key and parameters
                    info=str(i).encode('utf-8'),  # info contains the key number
                    backend=default_backend()
                ).derive(master_key_bytes)
            ).hexdigest()
            for i in range(num_keys)
        ]
        return derived_keys  # returns the list of sub-keys