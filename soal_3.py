jumlah = int(input('Masukan Jumlah Barang : '))
total = 0
barang_ke = 1

for i in range (jumlah):
    harga = int(input(f'Masukan Harga Barang Ke {barang_ke} : '))
    total += harga
    barang_ke += 1

print("="*100)

print(f'Total Harga Belanjaan : Rp.{total:,.2f}')