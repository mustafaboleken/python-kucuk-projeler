import random
import time

a=['Taş','Kağıt','Makas']

def sonuc():
    if b==i:
        print('Berabere')
    elif (b=='Taş') and (i=='Kağıt'):
        print('{} kazandı.'.format(l))
    elif (b=='Taş') and (i=='Makas'):
        print('{} kazandı.'.format(k))
    elif (b=='Kağıt') and (i=='Taş'):
        print('{} kazandı.'.format(k))
    elif (b=='Kağıt') and (i=='Makas'):
        print('{} kazandı.'.format(l))
    elif (b=='Makas') and (i=='Taş'):
        print('{} kazandı.'.format(l))
    else:
        print('{} kazandı.'.format(k))

k=input('Birinci kullanıcının  adını giriniz: ')
l=input('İkinci kullanıcının adını giriniz: ')
while 1:
    time.sleep(0.3)
    b=random.choice(a)
    time.sleep(0.3)
    i=random.choice(a)
    #Kodları Linux Shell üzerinden çalıştırınca karışık göründüğü için aralara boşluk kattım.
    print('                             ')
    print('{}='.format(k),b)
    print('                             ')
    print('{}='.format(l),i)
    print('                             ')
    sonuc()
    print('                             ')
    x=input('Tamam mı devam mı? Oyunu bitirmek için (ç), tekrar oynamak için herhangi bir girdi giriniz: ')
    if x in ['Ç','ç']:
        break
