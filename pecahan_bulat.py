# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 11/11/2024
# program pecahan ke bulat

pembilang = int(input("Masukkan pembilang : "))
penyebut = int(input("Masukkan penyebut : "))

if penyebut == 0:
    print("Tidak dapat membagi dengan nol")
else:
    rumus =  pembilang / penyebut

print(f"Hasil konversi : {rumus}")

