# looping python with range
for i in range(15):
    for j in range(i, 15):
        print(j, end=" ")
    print()

#looping python with break
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)

# looping python with continue
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        continue
    print(n)

# nested loop
def l_for():
    print ("For_2". center(0, "="))
    listCity = ['Kalimantan', 'Sumatra', 'Sulawesi']
    listPlace = ['West', 'North', 'South']
    for city in listCity:
        for place in listPlace:
            print(f"Provinsi: {city} {place}")

l_for()
print("selesai")

