def tampilkan_menu_awal():
    print("\nMenu Awal:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan (1-3): "))
        return pilihan
    except ValueError:
        print("Input harus berupa angka 1-3.")
        return None

def tampilkan_menu_pengusaha():
    print("\nMenu Pengusaha:")
    print("1. Tambah Proposal")
    print("2. Lihat Proposal Saya")
    print("3. Urutkan Proposal Saya")
    print("4. Cari Proposal Berdasarkan Nama Perusahaan")
    print("5. Log Out")
    try:
        pilihan = int(input("Masukkan pilihan (1-5): "))
        return pilihan
    except ValueError:
        print("Input harus berupa angka 1-5.")
        return None

def tampilkan_menu_investor():
    print("\nMenu Investor:")
    print("1. Lihat Semua Proposal")
    print("2. Urutkan Semua Proposal")
    print("3. Cari Proposal Berdasarkan Nama Perusahaan")
    print("4. Optimalkan Investasi (Knapsack)")
    print("5. Log Out")
    try:
        pilihan = int(input("Masukkan pilihan (1-5): "))
        return pilihan
    except ValueError:
        print("Input harus berupa angka 1-5.")
        return None

def tampilkan_menu_urutkan():
    print("\nPilih kriteria pengurutan:")
    print("1. ROI Investor (besar ke kecil)")
    print("2. Biaya Investasi (kecil ke besar)")
    print("3. Payback Period Investor (kecil ke besar)")
    print("4. Persentase Keuntungan untuk Investor (besar ke kecil)")
    print("5. Kembali")
    try:
        pilihan = int(input("Masukkan pilihan (1-5): "))
        return pilihan
    except ValueError:
        print("Input harus berupa angka 1-5.")
        return None