# class Anggrek :
#     def _init_(self, nama, warna, jenis):
#         self.nama = nama
#         self.warna = warna
#         self.jenis = jenis
    
#     def cek_anggrek(self):
#         print('nama: ',self.nama, '\nWarna: ',self.warna, '\njenis: ',self.jenis)

# print('Anggrek','putih','Anggrek bulan')


# class Mawar :
#     def _init_(self, nama, warna, jenis) :
#         self.nama = nama
#         self.warna = warna
#         self.jenis = jenis
    
#     def cek_mawar(self):
#         print('nama: ',self.nama, '\nWarna: ',self.warna, '\njenis: ',self.jenis)

# class Melati :
#     def _init_(self, nama, warna, jenis) :
#         self.nama = nama
#         self.warna = warna
#         self.jenis = jenis
    
#     def cek_melati(self):
#         print('nama: ',self.nama, '\nWarna: ',self.warna, '\njenis: ',self.jenis)


# bunga1 = Anggrek('Anggrek','putih', 'Anggrek Bulan')
# bunga2 = Mawar('Mawar','pink','Galica')
# bunga3 = Melati('Melati','kuning', 'Primrose')

# bunga1.cek_anggrek()
# bunga2.cek_mawar()
# bunga3.cek_melati()

    

































# class Plant :
#     def _init_(self, nama, jenis, warna):
#         self.nama = nama
#         self.jenis = jenis
#         self.warna = warna
    
#     def _set(self, nama, jenis, warna):
#         self.nama = nama
#         self.jenis = jenis
#         self.warna = warna
    
#     def _get(self):
#         print("Nama         : " + self.nama)
#         print("Jenis        : " + self.jenis)

        
# class Kembang :
#     def _init_(self, nama, anggrek, mawar, melati, jenis, warna):
#         super()._init_(nama, jenis, warna)
#         self.__anggrek = anggrek
#         self.mawar = mawar
#         self.melati = melati
    
#     def __setattr__(self, __name: str, __value: Any) -> None:
#         pass

    
#     def _get_kembang(self):
#         print("Nama          : " + self.anggrek)
#         print("Nama          : " + self.mawar)
#         print("Nama          : " + self.melati)

# nama    = input("Nama Bunga        : ")
# jenis   = input("Jenis Bunga       : ")
# warna   = input("Warna Bunga       : ")
# print("------------------------------------")


# Bunga = (nama, jenis, warna)




