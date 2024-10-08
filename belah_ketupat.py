# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 24/09/2024
# program belah ketupat

def belahKetupat():
    print('===============================')
    print('======== BELAH KETUPAT ========')
    print('===============================')

    d1 = float(input('Masukan panjang sisi diagonal pertama : '))
    d2 = float(input('Masukan panjang sisi diagonal kedua : '))

    l = lambda d1,d2 : 1/2 * d1 * d2

    print(f'Luas\t: {l(d1,d2)}')

belahKetupat()