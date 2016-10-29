import random
import time

p=[]
k=[
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

print('Şifre oluşturucuya hoş geldiniz.')
b=input('Şifreniz kaç haneli olsun? ')
if b.isnumeric():
    a=int(b)
    i=1
    while i <= a:
        t=random.choice(k)
        p.append(t)
        time.sleep(0.2)
        i=i+1
    o=''.join(p)
    print('Oluşturulan şifre: {}'.format(o))
else:
    print('Hatalı girdi girdiniz.Lütfen sadece sayı giriniz.')
