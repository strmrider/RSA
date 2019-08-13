import rsa

alice = rsa.Decryptor()
bob = rsa.Decryptor()

alice_encryptor = rsa.Encryptor(alice.get_public_key()[0], alice.get_public_key()[1])
bob_encryptor = rsa.Encryptor(bob.get_public_key()[0], bob.get_public_key()[1])


bob_message = "Hello Alice! This is Bob."
alice_message = "Hello Bob!"

# send messages
encrypted_bob = alice_encryptor.encrypt(bob_message)
print alice.decrypt(encrypted_bob)
encrypted_alice = bob_encryptor.encrypt(alice_message)
print bob.decrypt(encrypted_alice)

# using digital signature
bob_signature =  bob.sign_message(bob_message)
decrypted_bob = alice.decrypt(encrypted_bob)
if bob_encryptor.verify_signature(bob_signature, decrypted_bob):
    print "Message is from Bob"
print decrypted_bob

alice_signature = alice.sign_message(alice_message)
decrypted_alice = bob.decrypt(encrypted_alice)
if alice_encryptor.verify_signature(alice_signature, decrypted_alice):
    print "Message is from Alice"
print decrypted_alice