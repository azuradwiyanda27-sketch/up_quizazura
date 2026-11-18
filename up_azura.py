print("================================")
print("       KASIR KANTIN KAMPUS")
print("================================")

nama = input("Masukkan nama mahasiswa: ")

total_belanja = 0

while True:
    print("\n--- Input Data Makanan ---")
    makanan = input("Nama makanan: ")
    harga = int(input("Harga makanan: Rp"))
    jumlah = int(input("Jumlah pembelian: "))

    subtotal = harga * jumlah
    total_belanja += subtotal

    print("Subtotal: Rp", subtotal)

    ulang = input("\nTambah makanan lagi? (ya/tidak): ")

    if ulang.lower() != "ya":
        break

# Menentukan diskon
if total_belanja > 100000:
    diskon = total_belanja * 10 / 100
    print("Selamat! Kamu mendapatkan diskon 10%")
else:
    diskon = 10
    print("Maaf, kamu belum mendapatkan diskon")

# Menghitung total pembayaran
total_bayar = total_belanja - diskon

# Menampilkan hasil
print("\n================================")
print("         STRUK PEMBAYARAN")
print("================================")
print("Nama Mahasiswa :", nama)
print("Total Belanja  : Rp", total_belanja)
print("Diskon 10%     : Rp", int(diskon))
print("--------------------------------")
print("Total Bayar    : Rp", int(total_bayar))
print("================================")
print("      TERIMA KASIH!")