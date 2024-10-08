# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 07/10/2024
# program keliling segi sepuluh

def segiTujuh():
    print('===============================')
    print('===== KELILING SEGI TUJUH =====')
    print('===============================')

    s = int(input('Masukan panjang sisi nya : '))
    l = lambda s : 7 * s

    print(f'keliling : {l(s)}')

segiTujuh()