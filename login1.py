# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 10/11/2024
# program login 1

pin = "nimda123"

print ("-------------------------")
print ("Verifikasi Login Anda")
print ("-------------------------")

username = input ("Masukkan Username Anda: ")
password = input("Masukkan Password Anda: ")

if password == pin:
    print (f'''-------------------------
Login berhasil
-------------------------''')
else:
    print (f'''-------------------------
Maaf, Password Salah
-------------------------''')