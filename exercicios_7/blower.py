import blowfish

BS = 16

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

cipher = blowfish.Cipher("ABCDE".encode('ascii'))
cripted = b"".join(cipher.encrypt_ecb(pad("SABONETESABONETESABONETE").encode('utf-8')))
print(cripted.hex())
decripted = unpad(b"".join(cipher.decrypt_ecb(cripted)).decode('utf-8'))
decripted = unpad(b"".join(cipher.decrypt_ecb(bytes.fromhex('841091472604b96a841091472604b96a'))).decode('utf-8'))
print(decripted)
