key={
	'A':'4',
	'B':'Ç',
	'C':'Q',
	'Ç':'Ü',
	'D':'M',
	'E':'G',
	'F':'K',
	'G':'6',
	'Ğ':'N',
	'H':'J',
	'I':'2',
	'J':'C',
	'K':'5',
	'L':'S',
	'M':'P',
	'N':'0',
	'O':'Z',
	'Ö':'W',
	'P':'3',
	'R':'E',
	'S':'7',
	'Ş':'H',
	'T':'V',
	'U':'O',
	'Ü':'Y',
	'V':'1',
	'Y':'Ö',
	'Z':'Ğ',
	'Q':'I',
	'W':'8',
	'X':'?',
	'.':'-',
	'@':',',
	',':'.',
	'-':'@',
	'_':'=',
	'!':'+',
	' ':'!',
	'0':'F',
	'1':'T',
	'2':'A',
	'3':'D',
	'4':'U',
	'5':'L',
	'6':'Ş',
	'7':'R',
	'8':'X',
	'9':'B'
}


keyrec={
	'4':'A',
	'Ç':'B',
	'Q':'C',
	'Ü':'Ç',
	'M':'D',
	'G':'E',
	'K':'F',
	'6':'G',
	'N':'Ğ',
	'J':'H',
	'2':'I',
	'C':'J',
	'5':'K',
	'S':'L',
	'P':'M',
	'0':'N',
	'Z':'O',
	'W':'Ö',
	'3':'P',
	'E':'R',
	'7':'S',
	'H':'Ş',
	'V':'T',
	'O':'U',
	'Y':'Ü',
	'1':'V',
	'Ö':'Y',
	'Ğ':'Z',
	'I':'Q',
	'8':'W',
	'?':'X',
	'-':'.',
	',':'@',
	'.':',',
	'@':'-',
	'=':'_',
	'+':'!',
	'!':' ',
	'F':'0',
	'T':'1',
	'A':'2',
	'D':'3',
	'U':'4',
	'L':'5',
	'Ş':'6',
	'R':'7',
	'X':'8',
	'B':'9'
}

print('1: Veriyi Şifreleme')

print('2: Şifreyi Çözme')

e=input('Hangi işlemi yapmak istiyorsunuz: ')

if int(e) in [1]:
	encryptio=input('Şifrelenecek veriyi giriniz: ')
	encryption=encryptio.upper()
	def  f(encryption):
		for l in encryption:
			encryption=encryption.replace(l,key[l])
		return encryption
	i=f(encryption)
	print(i)	

elif int(e) in [2]:
	decryptio=input('Şifreli veriyi giriniz: ')
	decryption=decryptio.upper()
	def p(decryption):
		for l in decryption:
			decryption=decryption.replace(l,keyrec[l])
		return decryption
	t=p(decryption)
	print(t)

else:
	print('Geçersiz girdi girdiniz.')
