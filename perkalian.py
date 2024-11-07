# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 05/11/2024
# program inputan perkalian

print('='*20)
print('Inputan Perkalian')
print('='*20)

jumlah_perkalian = int(input("Masukkan jumlah perkalian: "))

for i in range(1, jumlah_perkalian+1):
  for j in range(1, 3):
    hasil = i * j
    print(f"{j} x {i} = {hasil}", end="  ")
  print()