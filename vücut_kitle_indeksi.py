x=input('Kütlenizi giriniz(kg): ')
y=input('Boyunuzu giriniz(cm): ')

bki=int(x)/((int(y)/100)**2)
print('Vücut kitle indeksiniz: ',bki)

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
