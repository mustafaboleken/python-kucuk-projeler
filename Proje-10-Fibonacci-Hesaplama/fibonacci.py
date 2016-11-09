def fibonacci(t):
    if t==0 or t==1:
        return t
    else:
        return fibonacci(t-1)+fibonacci(t-2)
sayı=int(input('Kaçıncı elemanı? '))
if sayı >= 0:
    sonuç=fibonacci(sayı-1)
    print('Fibonacci dizisinin {}. elemanı={}'.format(sayı,sonuç))
else:
    print('Negatif sayı girdiniz.')
