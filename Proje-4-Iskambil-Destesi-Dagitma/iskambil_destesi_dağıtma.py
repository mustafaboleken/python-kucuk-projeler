# -*- coding: utf-8 -*-

import random
import time

simgeler=['Karo','Maça','Sinek','Kupa']
sayılar=[1,2,3,4,5,6,7,8,9,10,'Bacak','Kız','Papaz']
kağıtlar=[]
a=[]
b=[]
c=[]
d=[]

for i in simgeler:
	for j in sayılar:
		kağıtlar.append(i+' '+str(j))

i=52
while i!=39:
	ü=random.choice(kağıtlar)
#bilgisayarda rastgele diye birşey yoktur bende kartların daha iyi dağılması için 
#random.choice'in her seçiminin arasına 0.2 saniye bekleme kattım
	time.sleep(0.2)
	a.append(ü)
	kağıtlar.remove(ü)
	i=i-1

while i!=26:
	ü=random.choice(kağıtlar)
	time.sleep(0.2)
	b.append(ü)
	kağıtlar.remove(ü)
	i=i-1

while i!=13:
	ü=random.choice(kağıtlar)
	time.sleep(0.2)
	c.append(ü)
	kağıtlar.remove(ü)
	i=i-1

while i!=0:
	ü=random.choice(kağıtlar)
	time.sleep(0.2)
	d.append(ü)
	kağıtlar.remove(ü)
	i=i-1

print('Oyuncu 1:')
for l in a:
	print(l)

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('Oyuncu 2:')
for l in b:
	print(l)

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('Oyuncu 3:')
for l in c:
	print(l)

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('Oyuncu 4:')
for l in d:
	print(l)
