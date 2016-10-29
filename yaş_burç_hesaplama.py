import time
import datetime

print('Bugünün tarihi:',time.strftime('%c'))

a=int(input('Doğdugunuz günü giriniz: '))
b=int(input('Doğdugunuz ayı sayı olarak giriniz: '))
c=int(input('Doğdugunuz yılı giriniz: '))

if ((a>20) & (b==3)) or ((a<21) & (b==4)):
    y='Koç'
elif ((a>20) & (b==4)) or ((a<21) & (b==5)):
    y='Boğa'
elif ((a>20) & (b==5)) or ((a<22) & (b==6)):
    y='İkizler'
elif ((a>21) & (b==6)) or ((a<23) & (b==7)):
    y='Yengeç'
elif ((a>22) & (b==7)) or ((a<23) & (b==8)):
    y='Aslan'
elif ((a>22) & (b==8)) or ((a<23) & (b==9)):
    y='Başak'
elif ((a>22) & (b==9)) or ((a<24) & (b==10)):
    y='Terazi'
elif ((a>23) & (b==10)) or ((a<23) & (b==11)):
    y='Akrep'
elif ((a>22) & (b==11)) or ((a<22) & (b==12)):
    y='Yay'
elif ((a>21) & (b==12)) or ((a<21) & (b==1)):
    y='Oğlak'
elif ((a>20) & (b==1)) or ((a<19) & (b==2)):
    y='Kova'
else:
    y='Balık'


q=time.localtime()
c=(q.tm_year)-(c)

print('Yaşınız: {} yaşındasınız.'.format(c))
print('Burcunuz: {}'.format(y))
