# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 11/11/2024
# program menghitung panjang nama

print('='*25)
print("MENGHITUNG PANJANG NAMA")
print('='*25)

try:
    input_nama = str(input("masukan nama anda = "))
    panjang_nama = len(input_nama)
    print(f"panjang nama anda adalah = {panjang_nama}")

except ValueError:
    print("inputan anda tidak valid")
    print("masukan inputan bertipe string saja")