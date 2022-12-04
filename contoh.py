

# class anggrek:
#     def __init__(self, benih, tunas, tanaman_kecil, tanaman_dewasa, berbunga):
#         self.benih = benih 
#         self.tunas = tunas
#         self.tanaman_kecil = tanaman_kecil
#         self.tanaman_dewasa = tanaman_dewasa
#         self.berbunga = berbunga
    
   
# class tunas(anggrek):
#     def __init__(self,tumbuh,):
#         self.tumbuh = tumbuh 

# jumlah_air = input("masukan jumlah air : ")
# jumlah_pupuk = input("masukan jumlah pupuk : ")

# jumlah_air = int(jumlah_air)
# jumlah_pupuk = int(jumlah_pupuk)



# print(jumlah_air)

# if jumlah_air <= 3 and jumlah_air <= 5 :
#     print("Tumbuh")
# else:
#     print("Tidak Tumbuh")

# print(jumlah_pupuk)

# if jumlah_pupuk <= 3 and jumlah_pupuk <= 5 :
#     print("Tumbuh")
# else:
#     print("Tidak Tumbuh")


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
         print("na")

# creation of an object variable or an instance
test = Employee 
(" Anggrek "),
('Jumlah pupuk : 3')
('jumlah air : 2')
('Tumbuh')
 
# calling a function of the class Person using its instance
test.display(), 
test.empDisp()


 # def statusTumbuh(self, status_tumbuh):
    #     self.status_tumbuh = status_tumbuh

    # def beriAir(self, jumlah_air):
    #     self.beri_air = jumlah_air

    # def beriPupuk(self, jumlah_pupuk):
    #     self.beri_pupuk = jumlah_pupuk
    
    # def jenis_plant(self, jenis):
    #     self.jenis = jenis

        

        