"""
Ligde 8 takım var , 8 takım rastgele kura çekip maç yapıyyor ve kazanan 4 takım yarı finale çıkıyor
Yarı finale çıkan  4 takım kura çekip maç yapıyor ve finale 2 takım kalıyor
Finalde 2 takım maç yapıyor ve kazanan şampiyon oluyor
"""
import random

class FutbolMaci():
    def __init__(self,takimadi="Tanınmayan Takım",takim_gucu=50,moral=50,puan=0):
        """
        :param takimadi: takimlar diye bir liste oluşturup bilinen takımlardan 8 tane yazacağız
        :param takim_gucu: Takim gücü 50-100 arasında olacak
        :param moral: Moral 50-100 arasında olacak
        :param puan: puan 0 dan başlayacak
        Takimin kazanma şansını  moral + takim_gucu belirleyecek
        Kazanan takım 3 puan alacak , berabere olunca iki takımda 1 er puan alacak , yenilene birşey yok
        """
        self.takimadi = takimadi
        self.takim_gucu = takim_gucu
        self.moral = moral
        self.puan = puan

    def musabaka(self):
        gucumuz = self.takim_gucu + self.moral
        return gucumuz

    def sonuc(self , macsonucualinanpuan , musabakayapilantakim):
        self.puan += macsonucualinanpuan
        print(self.takimadi , " - " , musabakayapilantakim ," arasındaki maçın kazananı : " , self.takimadi)

    def print(self):
        print("Takım adı : {} || Takım Gücü : {} ||  Moral : {} || Puan : {}".format(self.takimadi,self.takim_gucu,self.moral,self.puan))


takimlar = ["Fenerbahçe","Galatasaray","Beşiktaş","TrabzonSpor","ŞanlıUrfa Spor","Osmanlı Spor","TİGEM Spor","Demir Spor"]
takimlar2 = []
takimlar3 = []
i = 0
while (i<4):
    # takimlar[random.randrange(0,8)] = random.choice(takimlar)   => takimlar listesi içinden rastgele seç dedik
    takim1 = FutbolMaci(takimlar.pop(random.randrange(0,len(takimlar))),random.randrange(50,100),random.randrange(50,100))
    takim2 = FutbolMaci(takimlar.pop(random.randrange(0,len(takimlar))),random.randrange(50,100),random.randrange(50,100))
    # liste.pop  kullanımından listeden istenen değeri siliniyor ve silinen değer ekrana yazdırılıyor..
    takim1guc = takim1.musabaka()
    takim2guc = takim2.musabaka()
    if (takim1.takimadi == takim2.takimadi):
        continue
    if (takim1guc>takim2guc):
        takim1.sonuc(3,takim2.takimadi)
        takimlar2.append(takim1.takimadi)
    elif (takim2guc>takim1guc):
        takim2.sonuc(3,takim1.takimadi)
        takimlar2.append(takim2.takimadi)
    else:
        print(takim1.takimadi , " - " , takim2.takimadi , " arasındaki maçta takımlar Berabere kaldı...")

    i +=1


print("Yarı final Başlıyor ---------------------------")
i = 0
while (i<2):
    # takimlar[random.randrange(0,8)] = random.choice(takimlar)   => takimlar listesi içinden rastgele seç dedik
    takim1 = FutbolMaci(takimlar2.pop(random.randrange(0,len(takimlar2))),random.randrange(50,100),random.randrange(50,100))
    takim2 = FutbolMaci(takimlar2.pop(random.randrange(0,len(takimlar2))),random.randrange(50,100),random.randrange(50,100))
    # liste.pop  kullanımından listeden istenen değeri siliniyor ve silinen değer ekrana yazdırılıyor..
    takim1guc = takim1.musabaka()
    takim2guc = takim2.musabaka()
    if (takim1guc == takim2guc):
        continue # if ile takimgüçleri aynı gelirse continue ettirererk bu olasılığı aradan çıkardık
    if (takim1guc>takim2guc):
        takim1.sonuc(3,takim2.takimadi)
        takimlar3.append(takim1.takimadi)
    elif (takim2guc>takim1guc):
        takim2.sonuc(3,takim1.takimadi)
        takimlar3.append(takim2.takimadi)
    else:
        print(takim1.takimadi , " - " , takim2.takimadi , " arasındaki maçta takımlar Berabere kaldı...")

    i +=1


print("Final Başlıyor ---------------------------")
i = 0
while (i<1):
    # takimlar[random.randrange(0,8)] = random.choice(takimlar)   => takimlar listesi içinden rastgele seç dedik
    takim1 = FutbolMaci(takimlar3.pop(random.randrange(0,len(takimlar3))),random.randrange(50,100),random.randrange(50,100))
    takim2 = FutbolMaci(takimlar3.pop(random.randrange(0,len(takimlar3))),random.randrange(50,100),random.randrange(50,100))
    # liste.pop  kullanımından listeden istenen değeri siliniyor ve silinen değer ekrana yazdırılıyor..
    takim1guc = takim1.musabaka()
    takim2guc = takim2.musabaka()
    if (takim1.takimadi == takim2.takimadi):
        continue
    if (takim1guc>takim2guc):
        takim1.sonuc(3,takim2.takimadi)
        print("Bu fikstürün şampiyonu = " , takim1.takimadi)
    elif (takim2guc>takim1guc):
        takim2.sonuc(3,takim1.takimadi)
        print("Bu fikstürün şampiyonu = ", takim2.takimadi)
    else:
        print(takim1.takimadi , " - " , takim2.takimadi , " arasındaki maçta takımlar Berabere kaldı...")

    i +=1
