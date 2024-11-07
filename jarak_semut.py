# dibuat oleh : m.deryl fabiensyah
# tanggal di buat : 05/11/2024
# program jarak semut

print('='*20)
print('JARAK SEMUT')
print('='*20)

KILOMETER = 100000
METER = 100

cm = int(input("masukan berapa cm perjalanan semut: "))
km = int(cm / KILOMETER)
cm = cm % KILOMETER
m = int(cm / METER)
cm = cm % METER

print (f"{km}km {m}m {cm}cm")