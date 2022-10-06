print("PROGRAM MENGHITUNG NILAI MAHASISWA")

nama=input("Masukan Nama :")
nim=input("Masukan Nim :")
jk=input("Masukan Jenis Kelamin :")
tgl=input("Masukan Tanggal Input Nilai :")
matkul=input("Masukan Mata Kuliah :")
absensi=input("Masukan Absensi :")
tugas=float(input("Masukan Nilai Tugas :"))
uts=float(input("Masukan Nilai UTS :"))
uas=float(input("Masukan Nilai UAS :"))

na=(tugas * 0.2) + (uts * 0.4) + (uas * 0.4)

print("HASIL PERHITUNGAN")

print("Nama :" ,nama)
print("Nim :" ,nim)
print("Jenis Kelamin :" ,jk)
print("Tanggal Input Nilai :" ,tgl)
print("Mata Kuliah :" ,matkul)
print("Absensi :" ,absensi)
print("Nilai Tugas :" ,tugas)
print("Nilai Uts :" ,uts)
print("Nilai Uas :" ,uas)
print("Nilai Akhir :" ,na)

if na >= 90:
    print("Grade : A")
elif na >= 80:
    print("Grade : B")
elif na >= 75:
    print("Grade : C")
elif na >= 50:
    print("Grade : D")

if na >= 60:
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")