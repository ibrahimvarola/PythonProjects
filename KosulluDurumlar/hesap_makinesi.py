print("""*************************************
Hesap Makinesi Programı

İşlemler;

1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
************************************* 
""")

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

işlem = input("İşlemi giriniz: ")

if işlem == "1":
    print("{} ile {} in toplamı: {}".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} in farkı: {}".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} in çarpımı: {}".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} in bölümü: {}".format(a,b,a/b))
else:
    print("Geçersiz İşlem!!!!")