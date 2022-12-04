class Plant :
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
    
class Anggrek(Plant):
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        super().__init__(nama, status_tumbuh, jumlah_air, jumlah_pupuk)
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
    def tumbuh():
        nama = input("Anggrek")
        status_tumbuh = input("Status Tumbuh : ")
        jumlah_air = int(input("Jumlah Air : "))
        beri_Air = str(jumlah_air + 1)
        if jumlah_air <= 3 and jumlah_air <= 5 :
            print("Kurang")
        else:
            print("Cukup")
        jumlah_pupuk = int(input("Jumlah Pupuk : "))
        beri_Pupuk = str(jumlah_pupuk + 1)
        if jumlah_pupuk <= 3 and jumlah_pupuk <= 5 :
            print("Kurang")
        else:
            print("Cukup")
        return nama, status_tumbuh,jumlah_air,jumlah_pupuk,beri_Air,beri_Pupuk

    nama,status_tumbuh, jumlah_air,jumlah_pupuk,beri_Air,beri_Pupuk= tumbuh()

class Mawar(Plant):
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        super().__init__(nama, status_tumbuh, jumlah_air, jumlah_pupuk)
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
    def tumbuh():
        nama = input("Mawar")
        status_tumbuh = input("Status Tumbuh : ")
        jumlah_air = int(input("Jumlah Air : "))
        beri_Air = str(jumlah_air + 1)
        if jumlah_air <= 3 and jumlah_air <= 5 :
            print("Kurang")
        else:
            print("Cukup")
        jumlah_pupuk = int(input("Jumlah Pupuk : "))
        beri_Pupuk = str(jumlah_pupuk + 1)
        if jumlah_pupuk <= 3 and jumlah_pupuk <= 5 :
            print("Kurang")
        else:
            print("Cukup")
        return nama, status_tumbuh,jumlah_air,jumlah_pupuk,beri_Air,beri_Pupuk

    nama,status_tumbuh, jumlah_air,jumlah_pupuk,beri_Air,beri_Pupuk= tumbuh()

class Melari(Plant):
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        super().__init__(nama, status_tumbuh, jumlah_air, jumlah_pupuk)
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
    def tumbuh():
        nama = input("Melati")
        status_tumbuh = input("Status Tumbuh : ")
        jumlah_air = int(input("Jumlah Air : "))
        beri_Air = str(jumlah_air + 1)
        if jumlah_air <= 3 and jumlah_air <= 5 :
            print("Kurang")
        else:
            print("Cukup")
        jumlah_pupuk = int(input("Jumlah Pupuk : "))
        beri_Pupuk = str(jumlah_pupuk + 1)
        if jumlah_pupuk <= 3 and jumlah_pupuk <= 5 :
            print("Kurang")
        else:
            print("Cukup")
        return nama, status_tumbuh,jumlah_air,jumlah_pupuk,beri_Air,beri_Pupuk

    nama,status_tumbuh, jumlah_air,jumlah_pupuk,beri_Air,beri_Pupuk= tumbuh()