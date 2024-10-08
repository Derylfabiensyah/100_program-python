# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 21/08/2024
# program suhu

def suhu():
    print('========================================')
    print('==== MENGUBAH CELCIUS KE FAHRENHEIT ====')
    print('========================================')

    c = float(input("Celcius: "))
    f = lambda c : c * 1.8 + 32


    print(f"Suhu {c} C sama dengan {f(c)} F")

suhu()