# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 24/09/2024
# program kerucut

def kerucut():
    print('===============================')
    print('=========== KERUCUT ===========')
    print('===============================')

    PHI = 3 / 14
    r = int(input('masukan jari jari : '))
    s = int(input('masukan sisi kerucut : '))
    t = int(input('masukan tinggi kerucut : '))
    ls = lambda PHI,r,s : PHI * r * s
    lp = lambda PHI,r,s : (PHI * r * s) + (PHI * r * r)
    v = lambda PHI,r,t : 1/3 * PHI * r * r * t

    print(f'Luas Selimut : {ls(PHI,r,s)}')
    print(f'Luas Permukaan : {lp(PHI,r,s)}')
    print(f'Volume : {v(PHI,r,t)}')

kerucut()