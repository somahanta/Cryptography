from Crypto.Cipher import DES

des = DES.new('01234567', DES.MODE_ECB)
text = 'abcdefgh'
cipher_text = des.encrypt(text)
print(cipher_text)
decrtext=des.decrypt(cipher_text)
print(decrtext)
