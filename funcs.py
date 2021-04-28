import math

import phe.encoding
from phe import paillier


class EncodedNumber(phe.encoding.EncodedNumber):
    BASE = 64
    LOG2_BASE = math.log(BASE, 2)

class BytesIntEncoder:

    @staticmethod
    def encode(b: bytes) -> int:
        return int.from_bytes(b, byteorder='big')

    @staticmethod
    def decode(i: int) -> bytes:
        return i.to_bytes(((i.bit_length() + 7) // 8), byteorder='big')



def encodeNencrypt(n,public_key):
    encoded = EncodedNumber.encode(public_key,n)
    encrypted = public_key.encrypt(encoded)
    return encrypted

def dencodeNdencrypt(n,private_key):
    decrypted_but_encoded = \
        private_key.decrypt_encoded(n,EncodedNumber)
    return decrypted_but_encoded.decode()

def sameChecking(x,y):
    encrypted_c = x - y
    
    return encrypted_c


