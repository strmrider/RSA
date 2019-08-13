import utilities as math
import hashlib


class Decryptor:
    def __init__(self):
        p = math.generate_prime_number(2, 100)
        q = math.generate_prime_number(2, 100)

        self.n = p * q
        # Euler's totient function
        self.phi = (p - 1) * (q - 1)
        # public key
        self.e = self.generate_public_key()
        # private key
        self.d = math.multiplicative_inverse(self.e, self.phi)

    def generate_public_key(self):
        public_key = 2
        while public_key < self.phi:
            if math.gcd(public_key, self.phi) == 1:
                return public_key
            public_key += 1

    def get_public_key(self):
        return self.n, self.e

    def decrypt(self, data):
        return "".join([chr(pow(char, self.d, self.n)) for char in data])

    # Digital signature
    def sign_message(self, message):
        message_hash = hashlib.sha256(message.encode("UTF-8")).hexdigest()
        signature = [(pow(ord(char), self.d) % self.n) for char in message_hash]
        return signature


class Encryptor:
    def __init__(self, n, e):
        self.n = n
        self.e = e

    def encrypt(self, data):
        return [pow(ord(char), self.e, self.n) for char in data]

    def verify_signature(self, signature, message):
        try:
            message_hash = hashlib.sha256(message.encode("UTF-8")).hexdigest()
            signature_hash_value = "".join([chr(pow(char, self.e, self.n)) for char in signature])
            if signature_hash_value == message_hash:
                return True
            else:
                return False
        except Exception:
            print "Error: Signature verification process failed"
            return False
