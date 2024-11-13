print("SELAMAT DATANG DI KALKULATOR BMI")

nama = str(input("Masukan Nama : "))
bb = float(input("Masukan Berat Badan (Kg) : "))
tb = float(input("Masukan Tinggi Badan (M) : "))

BMI = bb/tb**2

if BMI < 18.5:
    hasil = "BERAT BADAN KURANG"

elif 18.5 <= BMI <24.9:
    hasil = "berat badan normal"

elif 25 <= BMI <29.9 :
    hasil = "kelebihan berat badan"

elif BMI >=30 :
    hasil = "obesitas"

print("="*100)
print(f"Nama : {nama}".title())
print(f"Berat Badan : {bb}".title())
print(f"Tinggi Badan : {tb}".title())
print(f"NILAI BMI : {BMI}".title())
print(f"Kategori bmi : {hasil}".title())
