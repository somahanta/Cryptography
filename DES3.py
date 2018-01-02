from Crypto.Cipher import DES3

des = DES3.new('0123456776543210', DES3.MODE_ECB)
text = 'adcfdefg'
cipher_text = des.encrypt(text)
print('encrypted text is:'+cipher_text)
decrtext=des.decrypt(cipher_text)
print(decrtext)
