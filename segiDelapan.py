# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 07/10/2024
# program keliling segi delapan

def segiDelapan():
    print('===============================')
    print('==== KELILING SEGI DELAPAN ====')
    print('===============================')

    s = int(input('Masukan panjang sisi nya : '))
    l = lambda s : 8 * s

    print(f'keliling : {l(s)}')

segiDelapan()