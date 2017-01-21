key='ABCÇDEFGĞHIJKLMNOÖPRSŞTUÜVYZQWX.@,-_! 0123456789'

keyrec='4ÇQÜMGK6NJ2C5SP0ZW3E7HVOY1ÖĞI8?-,.@=+!FTADULŞRXB'

print('1: Veriyi Şifreleme\n2: Şifreyi Çözme')

e=input('Hangi işlemi yapmak istiyorsunuz: ')

if e == '1':
	encryption=input('Şifrelenecek veriyi giriniz: ')
	f=str.maketrans(key,keyrec)
	encryption=encryption.upper().translate(f)
	print(encryption)

elif e == '2':
	decryption=input('Şifreli veriyi giriniz: ')
	p=str.maketrans(keyrec,key)
	decryption=decryption.upper().translate(p)
	print(decryption)

else:
	print('Geçersiz girdi girdiniz.')
