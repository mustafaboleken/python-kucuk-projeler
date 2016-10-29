def y(a):
    print(' _'*a)

def d(b):
    print((b-1)*('|'+(a*2-1)*' '+'|\n')+'|'+'_'+(a-1)*' _'+'|')

a=int(input('Yan kenarı giriniz: '))

b=int(input('Dik kenarı giriniz: '))

y(a)
d(b)
