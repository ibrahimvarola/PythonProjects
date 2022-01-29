kilo = int(input("Kiloyu giriniz: "))
boy = float(input("Boyu giriniz: "))

bki = kilo / (boy**2)

print("BKI: {}".format(bki))

if bki<18.5:
    print("Zayıf")
elif (bki >= 18.5 and bki<= 25):
    print("Normal")
elif (bki >= 25 and bki <= 30):
    print("Fazla kilolu")
else:
    print("Obez")