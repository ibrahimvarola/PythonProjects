print("""
***************************************
ATM Makinesine Hoşgediniz.
İşlemler;

1- Bakiye Sorgulama

2- Para Yatırma

3- Para Çekme

Programdan Çıkmak için 'q' ya basın.
***************************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi Giriniz :")

    if (islem == "q"):
        print("Programdan başarıyla çıkış işlemi gerçekleşmiştir.")
        break

    elif (islem == "1"):
        print("Bakiyeniz {} TL' dir.".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar

    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz: "))
        if (bakiye - miktar <0):
            print("Böyle bir miktar çekemezsiniz!")
            continue
        bakiye -= miktar
        print("Hesabınızdan {} TL tutarında para çekme işlemi gerçekleşmiştir.".format(miktar))

    else:
        print("Geçersiz işlem!")