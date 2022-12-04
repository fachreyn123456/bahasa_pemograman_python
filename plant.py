# class Person(object):
#     def __init__(self, id, nama):
#         self.id = id
#         self.nama = nama
#     def display(self):
#         print(self.id,"-", self.nama)
        
# # child class
# class Employee(Person):
#     def __init__(self, id, nama, gaji, posisi):
#         self.gaji = gaji
#         self.posisi = posisi
#         Person.__init__(self, id, nama)
#     def empDisp(self):
#         print(self.id,"-", self.nama,"-", self.gaji,"-", self.posisi)

# # creation of an object variable or an instance
# test = Employee(1,'John',4000000, 'Magang')
 
# test.display(), 
# test.empDisp()

# parent class
class Person(object):
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
    def display(self):
        print(self.nama,"-", self.jenis,"-", self.warna)
        
# child class
class Employee(Person):
    def __init__(self, nama, jenis, warna, jumlah_air, jumlah_pupuk, tumbuh):
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
        self.tumbuh = tumbuh
        Person.__init__(self, nama, jenis, warna)
    def empDisp(self):
         print(self.nama,"-", self.jumlah_pupuk,"-", self.jumlah_air,"-", self.tumbuh)

# creation of an object variable or an instance
test = Employee('Anggrek','Tebu', 'kuning', 2 ,3, 'Tumbuh')
 
# calling a function of the class Person using its instance
test.display(), 
test.empDisp()

        

    
