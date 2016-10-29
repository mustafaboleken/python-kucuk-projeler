import time

zaman = time.localtime()
yıl = zaman[0]
ay = zaman[1]
gün = zaman[2]
saat = zaman[3]
dakika = zaman[4]
saniye = zaman[5]

def tarihvesaat():
    print('\ntarih: {}/{}/{}\nsaat : {}:{}:{}\n'.format(gün, ay, yıl, saat, dakika, saniye))

tarihvesaat()
