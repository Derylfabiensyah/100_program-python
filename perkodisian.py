# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 27/10/2024
# program perkondisian

print('='*20)
print('PERKONDISIAN')
print('='*20)
# 1
kondisi = str(input('masukan kondisi air : '))

if kondisi == 'mendidih':
    print('matikan kompor')
elif kondisi == 'anget':
    print('tunggu sebentar lagi')
elif kondisi == 'dingin':
    print('nyalakan api kompor paling besar')



# 2
suhu = int(input('masukan suhu ruangan dalam bentuk celcius : '))

if suhu >= 50:
    print('nyalakan tanda bahaya')
elif suhu <= 20:
    print('matikan ac')
else:
    print('suhu ruangan nya berapa bang')


# 3
kondisim = input('masukan konidsi mobil : ')

if kondisim == 'rusak':
    print('jangan lupa service bang')
elif kondisim == 'bagus':
    print('mantap bang')
else:
    print('lanjut bang pake mobil nya')


# 4
x = int(input('masukan nilai x : '))
r = x % 2

if x == r:
    print('genap')
else:
    print('ganjil')