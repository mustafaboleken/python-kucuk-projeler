class crytography:
	def f(encrypt,key):
		global e
		e=''
		for l in encrypt:
			a = chr(ord(l) + int(key))
			e = e + a

	def p(decrypt,key):
		global e
		e=''
		for l in decrypt:
			a = chr(ord(l) - int(key))
			e = e + a
		
print('1: Veriyi şifrele')
print('2: Şifreyi çözme')

e = input('Hangi işlemi yapmak istiyorsunuz? ')
k = input('Anahtar\'ı giriniz: ')

if e == '1':
	m=input('Şifrelenecek metni giriniz: ')
	crytography.f(m,k)
	print(e)
	
elif e == '2':
	c=input('Şifrelenecek veriyi giriniz: ')
	crytography.p(c,k)
	print(e)
	
else:
	print('Geçersiz girdi girdiniz.')
