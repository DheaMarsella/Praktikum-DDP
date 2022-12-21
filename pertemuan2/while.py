# angka = 1

# while angka > 0 and angka < 11:
#     angka = int(input("masukkan bilangan bulat: "))
#     if angka >= 1:
#         print("Bilangan Positif")
#     elif angka < 0:
#         print("Bilangan Negatif")
#     else:
#         print("Biangan Nol")

while True:
    nama = input("masukkan nama anda: ")

    if nama == "x":
        break
    elif nama == "Adi":
        continue

    print("selamat datang ", nama)