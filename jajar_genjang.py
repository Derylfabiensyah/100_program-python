# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 24/09/2024
# program jajar genjang

def jajarGenjang():
    print('===============================')
    print('======== JAJAR GENJANG ========')
    print('===============================')

    a = float(input('Masukan alasnya : '))
    t = float(input('Masukan tingginya : '))
    l = lambda a,t : a * t

    print(f'Luas\t: {l(a,t)}')

jajarGenjang()