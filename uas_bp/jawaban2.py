def get_age():
    try:
        age = int(input('Berapa Umur Anda?: '))
    except:
        print('Jawaban Anda Tidak Terdeteksi, Silahkan Input dengan Angka!')
        age = 0
    return age

age = get_age()
print(f'Umur Anda {age} tahun')