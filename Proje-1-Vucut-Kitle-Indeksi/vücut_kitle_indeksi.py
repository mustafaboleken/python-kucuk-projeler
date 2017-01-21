def vki(x,y):
    global bki
    bki=x/((y/100)**2)
    print('Vücut kitle indeksiniz: ',bki)
    return bki

x=float(input('Kütlenizi giriniz(kg): '))
y=float(input('Boyunuzu giriniz(cm): '))

vki(x,y)

if bki<18.5:
    print('Zayıfsınız.')
elif bki<24.9:
    print('Normalsiniz.')
elif bki<29.9:
    print('Fazla kilosunuz.')
elif bki<39.9:
    print('Şişmansınız.')
else:
    print('Obezsiniz.')
