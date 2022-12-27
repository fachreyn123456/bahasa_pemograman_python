# Parameter Wajib

def perkenalan (nama,alamat):
    print(f"Saya {nama} tempat tinggal saya {alamat}")

perkenalan("Fachreyn Nurika", "Perum Purijaya Pasar Kemis")

# Parameter Opsional

def suhu_udara (daerah, derajat, satuan = 'celcius'):
    print(f"suhu di {daerah} adalah {derajat} {satuan}")

suhu_udara("Tangerang", 26, 'celcius')

# Function dengan lebih dari 1 return
def presentase (total,jumlah):
    if (total >= 0 and total <= jumlah):
        return total/jumlah * 100

    return False

print(presentase(20, 40))
print(presentase(100, 50))

