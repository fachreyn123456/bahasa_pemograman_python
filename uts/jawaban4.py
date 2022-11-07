class Belanja :

    def _init_(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampil():
        nim = int(input(" Masukana NIM : "))
        nama = input("Masukan Nama : ")

    tampil()

    print('\nSilahkan pilih menu yang tersedia : ')
    print ("1. capucino.")
    print ("2. teh.")
    print ("3. Exit.")
    pilihan = int(input('Masukkan Pilihanmu : '))


def hitung():
    harga_barang = int(input("Masukan Harga : "))
    ppn = 0.1 #10%
    total_ppn = harga_barang * ppn
    grand_total = float(harga_barang + total_ppn)
    return harga_barang,ppn,grand_total,total_ppn

sub_total,ppn,grand_total,total_ppn = hitung()

def printDat():
    print("Total PPN : ",total_ppn)
    print("Grand Total : ",grand_total)

printDat()




    

    
    
       





    



