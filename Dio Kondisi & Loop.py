# Kerusakan yang di bisa di tangani beserta harga
kerusakan_laptop = {
    "Layar pecah": 200,
    "Baterai rusak": 50,
    "Keyboard bermasalah": 30,
    "Overheating": 40,
    "Masalah suara": 20,
}
# Loop dengan while true untuk mengulang pilihan

while True:
    # Menampilkan pilihan kerusakan dan harga perbaikan dengan loop (for in)
    print("\nPilihan Kerusakan dan Harga Perbaikan:")
    for kerusakan, harga in kerusakan_laptop.items():
        print(f"- {kerusakan}: Rp.{harga}000,00")

    kerusakan_terpilih = input("Pilih kerusakan laptop (tuliskan nama kerusakan): ")
    harga_perbaikan = kerusakan_laptop.get(kerusakan_terpilih, 0)

    # Menampilkan biaya perbaikan mamakai kondisi (if else)
    if harga_perbaikan > 0:
        print(f"Biaya perbaikan {kerusakan_terpilih}: Rp.{harga_perbaikan}000,00")
    else:
        print("Kerusakan yang Anda pilih tidak ada dalam daftar.")

# perintah mengulang meneruskan dari while true
    ulang = input("Apakah Anda ingin memeriksa kerusakan lain? (ya/tidak): ").lower()
    if ulang != "ya":
        break

# Pesan kesimpulan
print("\nTerima kasih telah menggunakan layanan pengecekan kondisi laptop.")