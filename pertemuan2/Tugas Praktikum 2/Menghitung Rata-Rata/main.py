#menghitung rata-rata
print("PROGRAM PYTHON MENGHITUNG NILAI RATA-RATA")

n = int(input("\n Masukkan Banyaknya Angka: ")) #banyaknya data yang akan kita hitung

print() #Membuat baris baru
data = []
jum = 0

for i in range(0, n): #0 nilai awal, n nilai akhir
    temp = int(input("Masukkan angka ke-%d: " % (i+1))) #kita bebas memasukkan angka sesuai keinginan
    data.append(temp) #fungsi ini untuk menambahkan nilai dibagian akhir
    jum += data[i] #nilai yang akan ditambahkan
    rata2 = jum / n #rumus menghitung rata-rata

print("\nRata-rata  = %0.2f" % rata2)