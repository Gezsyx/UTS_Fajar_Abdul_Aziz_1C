tahun = int(input("Masukan Tahun : "))

kabisat_1 = tahun % 400
kabisat_2 = tahun % 4
kabisat_3 = tahun % 100


if kabisat_1 == 0 or kabisat_2 == 0 and kabisat_3 >= 1 :
    hasil = "Tahun Kabisat"
else:
    hasil = "Bukan Tahun Kabisat"

print(f"TAHUN {tahun} merupakan {hasil}")