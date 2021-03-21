print("Hiptenüs Hesaplama Programına Hoşgeldiniz...\nLütfen dik olan iki kenarın uzunluğunu giriniz.")

kenar1 = int(input("Kenar 1: "))
kenar2 = int(input("Kenar 2: "))

hipotenus= (kenar1 ** 2 + kenar2 ** 2) ** 0.5

print("Hipotenüs değeri: {}".format(hipotenus))