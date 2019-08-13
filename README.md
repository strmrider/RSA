# RSA algorithm

Python implementation of [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) encryption and digital signature algorithms.

Includes the implementation of Miller–Rabin primality test and the Extended Euclidean algorithm.

## Example
Simulated communcation between 'Bob' and 'Alice' (view [example.py](https://github.com/strmrider/RSA/blob/master/example.py) for more detailed example).

Import module
```
import rsa
```
Create decryptor and public key
```
alice = rsa.Decryptor()
public_key = rsa.get_public_key()
```
Create encryptor
```
alice_encryptor = rsa.Encryptor(public_key[0], public_key[1]
```
Encrypt message
```
message_for_alice = alice_encryptor.encrypt(MESSAGE_FOR_ALICE)
```
Decrypt message
```
message_from_bob = alice.decrypt(MESSAGE_FROM_BOB)
```
Sign message
```
signature = alice.sign_message(MESSAGE_FOR_BOB)
```
Verify signature
```
alice.verify_signature(signature, MESSAGE_FROM_ALICE)
```
