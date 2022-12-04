# class Plant:
#     def __init__(self, nama, jenis, warna):
#         self.nama = nama
#         self.jenis = jenis
#         self.warna = warna
#     def display(self):
#         print(self.nama,"-", self.jenis,"-", self.warna)
        
# child class
class Plant:
    def __init__(self):
        self.jumlah_air = 0
        self.jumlah_pupuk = 0
        self.tumbuh = 0
        
    def beriAir(self):
        self.jumlah_air = str.jumlah_air + 1
    
    def beriPupuk(self):
        self.jumlah_pupuk = str.jumlah_pupuk + 1
    
    def status(self):
        self.tumbuh = str.tumbuh + 1
    
    def jenis_plant(self, jenis):
        self.jenis = jenis
    

str = Plant()
# print(str.__dict__)

def tumbuh(self, jumlah_air,jumlah_pupuk,tumbuh):
    self.jumlah_air = jumlah_air
    self.jumlah_pupuk = jumlah_pupuk
    self.tumbuh = tumbuh
print (tumbuh)    


         

# # creation of an object variable or an instance
# test = Employee('Anggrek','Tebu', 'kuning', 2 ,3, 'Tumbuh')
 
# # calling a function of the class Person using its instance
# test.display(), 
# test.empDisp()