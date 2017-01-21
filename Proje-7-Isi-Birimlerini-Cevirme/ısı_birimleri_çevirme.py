class ısı_birimleri:
    def celcius_to_fahrenhayt(l):
        k=((l*9) / 5) + 32
        print(k)

    def celcius_to_kelvin(l):
         k=l+273
         print(k)

    def fahrenhayt_to_celcius(l):
        k=((l-32)*5)/9
        print(k)

    def fahrenhayt_to_kelvin(l):
         k=(((l-32)*5)/9)+273
         print(k)

    def kelvin_to_fahrenhayt(l):
        k=(((l-273)*9)/5)+32
        print(k)

    def kelvin_to_celcius(l):
        k=(l-273)
        print(k)

print('\n1) Celsius-->Fahrenhayt')
print('2) Fahrenhayt-->Celsius')
print('3) Celsius-->Kelvin')
print('4) Kelvin-->Celsius')
print('5) Fahrenhayt-->Kelvin')
print('6) Kelvin-->Fahrenhayt\n')

a=input('Hangi işlemi yapmak istiyorsunuz?')

if int(a)==1:
	l=int(input('Sıcaklığı girin: '))
	ısı_birimleri.celcius_to_fahrenhayt(l)

elif int(a)==2:
	l=int(input('Sıcaklığı girin: '))
	ısı_birimleri.fahrenhayt_to_celcius(l)

elif int(a)==3:
	l=int(input('Sıcaklığı girin: '))
	ısı_birimleri.celcius_to_kelvin(l)

elif int(a)==4:
	l=int(input('Sıcaklığı girin: '))
	ısı_birimleri.kelvin_to_celcius(l)

elif int(a)==5:
	l=int(input('Sıcaklığı girin: '))
	ısı_birimleri.fahrenhayt_to_kelvin(l)

elif int(a)==6:
	l=int(input('Sıcaklığı girin: '))
	ısı_birimleri.kelvin_to_fahrenhayt(l)

else:
	print('Yanlış girdi girdiniz.')
