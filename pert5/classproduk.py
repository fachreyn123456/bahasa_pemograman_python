# Atribut/Field

class Barang:
    idproduk = None
    namaproduk = None
    harga = None
    jumlah = None

    def jual(self):
        print(f'jual {self.idproduk} {self.namaproduk} {self.harga} {self.jumlah}')
    
# Konstruktor

rinso = Barang()
rinso.idproduk = "123"
rinso.namaproduk = "rinso"
rinso.harga = "27000"
rinso.jumlah = "1"

rinso.jual()

    