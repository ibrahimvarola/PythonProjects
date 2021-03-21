def mukemmel_bulma(sayi):
    tam_bolenler = []
    toplama = 0
    for i in range(1, sayi):
        if (sayi % i == 0):
            tam_bolenler.append(i)
    for j in tam_bolenler:
        toplama = toplama + j
    if (toplama == sayi):
        return True

while True:
    sayi = input("Sayı: ")
    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)
        if (mukemmel_bulma(sayi)):
            print("Mukemmel Sayi")
        else:
            print("Mukemmel degil!")