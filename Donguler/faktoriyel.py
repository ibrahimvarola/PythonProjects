print("""
*****************************************
Faktöriyel Bulma Yazılımına Hoşgeldiniz.

Çıkmak için q' ya basınız.
*****************************************
""")

while True:
    sayi = input("Sayıyı giriniz: ")
    if (sayi == "q"):
        print("Program Sonlandırılıyor...")
        break

    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2, sayi+1):
            print("Faktöriyel:",faktoriyel,"i:",i)
            faktoriyel *= i
        print("Faktöriyel:", faktoriyel)