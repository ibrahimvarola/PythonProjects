import random
import time

class Kumanda():
    
    def __init__(self,tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["TRT"], kanal = "TRT"):

        self.tv_durum = tv_durum
        self.tv_ses =tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık!")
        else:
            print("Televizyon Açılıyor.")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı!")
        else:
            print("Televizyon Kapatılıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış = 'cikis'")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)

            elif (cevap == ">"):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)

            else:
                print("Ses güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")

        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi!")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def  __str__(self):
        return "TV Durumu {}\nTV Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print("""
Televizyon Uygulaması:

1 - TV Aç
2 - TV Kapat
3 - Ses Ayarları
4 - Kanal Ekle
5 - Kanal Sayısını Öğren
6 - Rastgele Kanal Geçme
7 - TV Bilgileri

Çıkmak için 'q' ya basınız.
""")

while True:

    işlem = input("İşlemi Seçiniz: ")

    if (işlem == "q"):
        print("Program Sonlandırıldı.")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()

    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarlari()

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif  (işlem == "5"):
        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()

    elif (işlem == "7"):
        print(kumanda)

    elif (işlem == "q"):
        break

    else:
        print("Geçersiz İşlem!")