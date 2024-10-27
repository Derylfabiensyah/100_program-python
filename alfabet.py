# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 26/10/2024
# program huruf

print('*'*30)
print('\tPROGRAM HURUF')
print('*'*30)

huruf = input('masukan huruf alfabet (a-z): ')


if huruf in 'aiueo':
    print('huruf ini termasuk kedalam huruf vokal')
elif huruf.isdigit():
    print('ini bukan huruf')
else:
    print('huruf ini termasuk kedalam huruf konsonan')