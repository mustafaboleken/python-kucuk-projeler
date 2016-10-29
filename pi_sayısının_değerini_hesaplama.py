n=0
s=0

r=int(input('Son değişkeni giriniz(varsayılan=1000000): '))
#Son değişkeni ne kadar büyük yaparsak pi sayısının gerçek değerine o kadar yaklaşmış oluruz.

while n<r:
	s=s+((-1)**n)/(2*n+1)
	n=n+1
print('Pi sayısının değeri:',4*s)
