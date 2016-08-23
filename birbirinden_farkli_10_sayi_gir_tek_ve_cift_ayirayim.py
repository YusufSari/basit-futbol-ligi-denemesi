"""
Kullanıcıdan 10 adet farklı sayı girmesini istiyoruz ,
    Eğer daha önce girdiği sayıyı tekrar girmek isterse uyarı veriyoruz
İşlem sonunda girilen sayılardan tek olanları ve çift olanları ayrı ayrı ekrana basıyoruz.
"""
sira = 1
liste = []
cif_sayilar = []
tek_sayilar = []
while True:
    if sira == 11:
        tek_sayilar = [s for s in liste if s % 2 != 0]
        cif_sayilar = [s for s in liste if s%2==0]
        print("Tek sayılar : {}".format(tek_sayilar))
        print("Çift sayılar : {}".format(cif_sayilar))
        break
    i = input("{} . sayıyı giriniz : ".format(sira))
    if i.isnumeric():
        i = int(i)
        if not i in liste:
            liste.append(i)
        else:
            print("Aynı sayıyı iki defa giremezsiniz..!")
            continue
        sira+=1
    else:
        print("Sadece sayı girmeniz gerekiyor..!")
        continue

