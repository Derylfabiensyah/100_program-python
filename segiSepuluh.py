# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 07/10/2024
# program keliling segi sepuluh

def segiSepuluh():
    print('===============================')
    print('==== KELILING SEGI SEPULUH ====')
    print('===============================')

    s = int(input('Masukan panjang sisi nya : '))
    l = lambda s : 10 * s

    print(f'keliling : {l(s)}')

segiSepuluh()