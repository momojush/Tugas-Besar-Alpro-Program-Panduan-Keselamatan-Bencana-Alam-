print("===== Sistem Panduan Keselamatan Bencana Alam =====\n")

# database bencana alam
bencana_alam = [
    (
        "Gempa bumi",
        "Gempa bumi adalah getaran atau guncangan pada permukaan bumi akibat pelepasan energi secara tiba-tiba.",
        [
            "Lindungi kepala dan badan dari reruntuhan.",
            "Segera keluar jika memungkinkan.",
            "Cari tempat aman dari goncangan.",
            "Jauhi bangunan dan tiang listrik."
        ]
    ),
    (
        "Tsunami",
        "Tsunami adalah gelombang besar akibat gangguan di dasar laut seperti gempa atau longsor.",
        [
            "Evakuasi ke tempat tinggi.",
            "Jauhi pantai setelah goncangan.",
            "Hindari bangunan rapuh.",
            "Dengarkan informasi dari BMKG."
        ]
    ),
    (
        "Letusan vulkanik",
        "Letusan gunung berapi terjadi ketika magma terdorong keluar dari dalam bumi.",
        [
            "Gunakan masker dan kacamata.",
            "Pakai pakaian tertutup.",
            "Hindari aliran sungai (lahar).",
            "Ikuti jalur evakuasi."
        ]
    ),
    (
        "Badai topan",
        "Badai topan adalah angin kencang skala besar di wilayah tropis.",
        [
            "Tetap di rumah yang kokoh.",
            "Matikan listrik jika banjir.",
            "Pindah ke tempat evakuasi jika perlu.",
            "Jangan keluar sebelum aman."
        ]
    )
]


# menu utama
def tampil_menu_utama():
    print("\n===== MENU UTAMA =====")

    for i in range(len(bencana_alam)):
        print(f"{i+1}. {bencana_alam[i][0]}")

    print("Ketik nomor untuk melihat detail, 'menu' untuk CRUD, atau 'keluar' untuk berhenti.")

# menu CRUD
def menu_crud():
    while True:
        print("\n--- MENU CRUD ---")
        print("1. Tambah bencana (CREATE)")
        print("2. Ubah bencana (UPDATE)")
        print("3. Hapus bencana (DELETE)")
        print("4. Tampilkan daftar (READ)")
        print("5. Kembali")

        pilihan = input("Pilihan CRUD (1-5): ")

        # create
        if pilihan == "1":
            nama = input("Nama bencana: ")
            deskripsi = input("Deskripsi: ")
            tips = [input(f"Tips {i+1}: ") for i in range(4)]
            bencana_alam.append((nama, deskripsi, tips))
            print(f"'{nama}' berhasil ditambahkan.")

        # update
        elif pilihan == "2":
            try:
                nomor = int(input("Nomor bencana yang ingin diubah: ")) - 1
                if 0 <= nomor < len(bencana_alam):
                    nama = input("Nama baru: ")
                    deskripsi = input("Deskripsi baru: ")
                    tips_baru = []
                    for i in range(4):
                        tips_baru.append(input(f"Tips baru {i+1}: "))
                    bencana_alam[nomor] = (nama, deskripsi, tips_baru)
                    print("Data berhasil diubah.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid.")

        # delete
        elif pilihan == "3":
            try:
                nomor = int(input("Nomor yang ingin dihapus: ")) - 1
                if 0 <= nomor < len(bencana_alam):
                    nama = bencana_alam.pop(nomor)[0]
                    print(f"'{nama}' berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid.")

        # read
        elif pilihan == "4":
            print("\nDaftar bencana saat ini:")
            for i in range(len(bencana_alam)):
                print(f"{i+1}. {bencana_alam[i][0]}")

        elif pilihan == "5":
            return

        else:
            print("Pilihan CRUD tidak valid, coba lagi.")

# program perulangan
while True:
    tampil_menu_utama()
    pilihan_user = input("\nMasukkan pilihan: ")

    if pilihan_user == "keluar":
        print("Byee jawa")
        break

    if pilihan_user == "menu":
        menu_crud()
        continue

    if pilihan_user.isdigit():
        idx = int(pilihan_user) - 1

        if 0 <= idx < len(bencana_alam):

            while True:
                tanya = input("Tampilkan panduan keselamatan? (ya/tidak): ")

                if tanya == "ya":
                    nama, deskripsi, tips = bencana_alam[idx]
                    print(f"\n--- {nama} ---")
                    print("Deskripsi:", deskripsi)
                    print("Panduan keselamatan:")

                    no = 1
                    for tip in tips:
                        print(f"{no}. {tip}")
                        no += 1
                    break

                elif tanya == "tidak":
                    print("Baik, tidak menampilkan panduan.")
                    break

                else:
                    print(f"Input tidak dikenali: '{tanya}'. Ketik 'ya' atau 'tidak'.")

            input("\nTekan ENTER untuk kembali ke menu utama...")
            continue

        else:
            print("Nomor bencana tidak valid.")
            continue

    print("Pilihan tidak valid. Ketik nomor, 'menu', atau 'keluar'.")
