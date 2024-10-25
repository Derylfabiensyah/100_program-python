# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 24/10/2024
# program Ganjil henap

user = int(input('masukan nilai angka : '))
rumus = user % 2

if user == rumus:
    print('genap')
else:
    print('ganjil')