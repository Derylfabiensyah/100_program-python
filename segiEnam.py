# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 07/10/2024
# program keliling segi enam

def segiEnam():
    print('================================')
    print('====== KELILING SEGI ENAM ======')
    print('================================')

    s = int(input('Masukan panjang sisi nya : '))
    l = lambda s : 6 * s

    print(f'keliling : {l(s)}')

segiEnam()