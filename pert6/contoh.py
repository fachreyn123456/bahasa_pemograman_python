class Jam :
    def _init_(self,jam,menit,detik):
        self.jm = jam
        self.mnt = menit
        self.dtk = detik 


def tampil():
    jam = int(input("Jam : "))
    menit = int(input("Menit : "))
    detik = int(input("Detik: "))

    if jam <=24 and menit <= 59 and detik <= 59:
        fJam = Jam(jam,menit,detik)
        print("Tugas Jam".center(30,"="))
        print("""
        Jam : {}
        Menit : {}
        Detik : {}
        """.format(fJam.jm,fJam.mnt,fJam.dtk))
        print("=".center(30,"="))
    else: 
        print("Format Input Salah")
    
tampil()