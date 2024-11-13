# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 10/11/2024
# program login 2

print ("-------------------------")
print ("Verifikasi Login Anda")
print ("-------------------------")

username = str(input("Masukkan Username Anda: "))
password = str(input("Masukkan Password Anda: "))

if username == "admin" and password == "nimda123":
    print ('''-------------------------
Verifikasi Berhasil
-------------------------''')

else:
    print ('''-------------------------
Verifikasi Gagal
-------------------------''')