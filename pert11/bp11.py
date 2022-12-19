def welcome():
    print('Tugas Perkuliahan Sesi 11')
    print('Function')
welcome()

#Function dengan parameter
def cetak(a,b):
    print("Nama : ", a)
    print("NIM : ", b)
def tampil(a,b):
    print("Prodi : ", a)
    print("Fakultas : ", b)

cetak("Fachreyn", "20210801258")
tampil("Teknik Informatika", "Fakultas Komputer")

#Function dengan return
def penjumlahan(a,b):
    c = a + b
    print(a, "+", b, "=", c)

a = int(input("bilangan 1 : "))
b = int(input("bilangan 2 : "))
penjumlahan(a,b)