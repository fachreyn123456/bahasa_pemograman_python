class Waktu:
    
    def _init_(self,jj,mm,dd):
        self.jam = jj
        self.menit = mm
        self.detik= dd
    

j = input("masukan jam: ")
m = input("masukan menit: ")
d = input("masukan detik: ")

jj = int(j)
mm = int(m)
dd = int(d)
print("jam:",jj,":", mm, ":", dd)

if jj <= 24 and mm <= 59  and dd <= 59:  
    print("Format Waktu Benar")
else:
    print("Format Waktu Salah")






        

