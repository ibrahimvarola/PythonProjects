sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))

print("Sayı 1: {}, Sayı 2: {}".format(sayi1,sayi2))

sayi1,sayi2 = sayi2,sayi1

print("Değişen sonuçlar= Sayı 1: {}, Sayı 2: {}".format(sayi1,sayi2))