key=[
	'A',
	'B',
	'C',
	'Ç',
	'D',
	'E',
	'F',
	'G',
	'Ğ',
	'H',
	'I',
	'İ',
	'J',
	'K',
	'L',
	'M',
	'N',
	'O',
	'Ö',
	'P',
	'R',
	'S',
	'Ş',
	'T',
	'U',
	'Ü',
	'V',
	'Y',
	'Z',
	'Q',
	'W',
	'X',
	' ',
	'0',
	'1',
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9'
]

print('1:Veriyi şifreleme')
print('2: Şifreyi çözme')

e=input('Hangi işlemi yapmak istiyorsunuz? ')

if int(e) in [1]:
	m1=input('Şifrelenecek metni giriniz: ')
	m=m1.upper()
	def f(encrypt):
		while 1:
			for l in encrypt:
				t=key.index(l)
				encrypt=encrypt.replace(key[t],key[t+3])
			return encrypt
	q=f(m)
	print(q)


elif int(e) in [2]:
	c1=input('Şifrelenecek veriyi giriniz: ')
	c=c1.upper()
	def p(decrypt):
		while 1:
			for l in decrypt:
				t=key.index(l)
				decrypt=decrypt.replace(key[t],key[t-3])
			return decrypt
	a=p(c)
	print(a)

else:
	print('Geçersiz girdi girdiniz.')
