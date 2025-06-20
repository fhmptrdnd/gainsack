#==========================================|Training 4|==========================================
import csv
from my_heap import build_heap, heappop

def input_proposal(nama_perusahaan):
    print("Masukkan data untuk proposal investasi:")
    judul_proyek = input("Judul proyek: ")
    biaya_awal = float(input("Biaya investasi awal (Rp): "))
    pendapatan_tahunan = float(input("Pendapatan tahunan (Rp): "))
    pengeluaran_tahunan = float(input("Pengeluaran tahunan (Rp): "))
    durasi_tahun = int(input("Durasi investasi (tahun): "))
    persentase_investor = float(input("Persentase keuntungan untuk investor (%): "))

    laba_bersih_tahunan = pendapatan_tahunan - pengeluaran_tahunan
    total_laba_bersih = laba_bersih_tahunan * durasi_tahun
    untung_bersih = total_laba_bersih - biaya_awal
    roi = (untung_bersih / biaya_awal) * 100 if biaya_awal != 0 else 0
    payback_period = biaya_awal / laba_bersih_tahunan if laba_bersih_tahunan != 0 else float('inf')

    laba_investor_tahunan = laba_bersih_tahunan * (persentase_investor / 100)
    total_laba_investor = laba_investor_tahunan * durasi_tahun
    roi_investor = (total_laba_investor / biaya_awal) * 100 if biaya_awal != 0 else 0
    payback_investor = biaya_awal / laba_investor_tahunan if laba_investor_tahunan != 0 else float('inf')

    return {
        "JUDUL PROYEK": judul_proyek,
        "NAMA PERUSAHAAN": nama_perusahaan,
        "BIAYA AWAL": biaya_awal,
        "LABA BERSIH TAHUNAN": laba_bersih_tahunan,
        "TOTAL LABA BERSIH": total_laba_bersih,
        "UNTUNG BERSIH": untung_bersih,
        "ROI PERUSAHAAN": roi,
        "PAYBACK PERIOD": payback_period,
        "DURASI INVESTASI": durasi_tahun,
        "PERSENTASE INVESTOR": persentase_investor,
        "LABA INVESTOR TAHUNAN": laba_investor_tahunan,
        "TOTAL LABA INVESTOR": total_laba_investor,
        "ROI INVESTOR": roi_investor,
        "PAYBACK INVESTOR": payback_investor
    }

def tampilkan_proposal(proposal):
    label_width = 38
    print(f"\n{'Judul Proyek':<{label_width}}: {proposal['JUDUL PROYEK']}")
    print(f"{'Nama Perusahaan':<{label_width}}: {proposal['NAMA PERUSAHAAN']}")
    print(f"{'Biaya Investasi Awal':<{label_width}}: Rp {proposal['BIAYA AWAL']:,.0f}")
    print(f"{'Laba Bersih Tahunan':<{label_width}}: Rp {proposal['LABA BERSIH TAHUNAN']:,.0f}")
    print(f"{'Total Laba Bersih':<{label_width}}: Rp {proposal['TOTAL LABA BERSIH']:,.0f}")
    print(f"{'Untung Bersih':<{label_width}}: Rp {proposal['UNTUNG BERSIH']:,.0f}")
    print(f"{'ROI Perusahaan':<{label_width}}: {proposal['ROI PERUSAHAAN']:.2f}%")
    print(f"{'Payback Period Perusahaan':<{label_width}}: {proposal['PAYBACK PERIOD']:.2f} tahun")
    print(f"{'Durasi Investasi':<{label_width}}: {proposal['DURASI INVESTASI']} tahun")
    print(f"{'Persentase Keuntungan untuk Investor':<{label_width}}: {proposal['PERSENTASE INVESTOR']:.2f}%")
    print(f"{'Laba Investor Tahunan':<{label_width}}: Rp {proposal['LABA INVESTOR TAHUNAN']:,.0f}")
    print(f"{'Total Laba Investor':<{label_width}}: Rp {proposal['TOTAL LABA INVESTOR']:,.0f}")
    print(f"{'ROI Investor':<{label_width}}: {proposal['ROI INVESTOR']:.2f}%")
    print(f"{'Payback Period untuk Investor':<{label_width}}: {proposal['PAYBACK INVESTOR']:.2f} tahun")

def simpan_ke_csv_proposal(daftar_proposal, filename="training_proposal.csv"):
    headers = [
        "JUDUL PROYEK", "NAMA PERUSAHAAN", "BIAYA AWAL", "LABA BERSIH TAHUNAN",
        "TOTAL LABA BERSIH", "UNTUNG BERSIH", "ROI PERUSAHAAN", "PAYBACK PERIOD",
        "DURASI INVESTASI", "PERSENTASE INVESTOR", "LABA INVESTOR TAHUNAN",
        "TOTAL LABA INVESTOR", "ROI INVESTOR", "PAYBACK INVESTOR"
    ]
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        for proposal in daftar_proposal:
            writer.writerow(proposal)

def baca_dari_csv_proposal(filename="training_proposal.csv"):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                row["BIAYA AWAL"] = float(row["BIAYA AWAL"])
                row["LABA BERSIH TAHUNAN"] = float(row["LABA BERSIH TAHUNAN"])
                row["TOTAL LABA BERSIH"] = float(row["TOTAL LABA BERSIH"])
                row["UNTUNG BERSIH"] = float(row["UNTUNG BERSIH"])
                row["ROI PERUSAHAAN"] = float(row["ROI PERUSAHAAN"])
                row["PAYBACK PERIOD"] = float(row["PAYBACK PERIOD"])
                row["DURASI INVESTASI"] = int(row["DURASI INVESTASI"])
                row["PERSENTASE INVESTOR"] = float(row["PERSENTASE INVESTOR"])
                row["LABA INVESTOR TAHUNAN"] = float(row["LABA INVESTOR TAHUNAN"])
                row["TOTAL LABA INVESTOR"] = float(row["TOTAL LABA INVESTOR"])
                row["ROI INVESTOR"] = float(row["ROI INVESTOR"])
                row["PAYBACK INVESTOR"] = float(row["PAYBACK INVESTOR"])
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file CSV: {e}")
        return []

def simpan_ke_csv_user(username, password, role, filename="training_user.csv"):
    headers = ["USERNAME", "PASSWORD", "ROLE"]
    user_data = {"USERNAME": username, "PASSWORD": password, "ROLE": role}
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(user_data)

def baca_dari_csv_user(filename="training_user.csv"):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file CSV: {e}")
        return []

def sign_up():
    username = input("Masukkan username: ")
    users = baca_dari_csv_user()
    if any(user["USERNAME"] == username for user in users):
        print("Username sudah digunakan. Silakan coba lagi.")
        return None
    
    password = input("Masukkan password: ")
    print("Pilih role:")
    print("1. Pengusaha")
    print("2. Investor")
    role_choice = input("Masukkan pilihan (1/2): ")
    role = "Pengusaha" if role_choice == "1" else "Investor" if role_choice == "2" else None
    
    if not role:
        print("Pilihan role tidak valid.")
        return None
    
    simpan_ke_csv_user(username, password, role)
    print("Sign up berhasil!")
    return {"username": username, "role": role}

def log_in():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    users = baca_dari_csv_user()
    
    for user in users:
        if user["USERNAME"] == username and user["PASSWORD"] == password:
            print("Log in berhasil!")
            return {"username": username, "role": user["ROLE"]}
    
    print("Username atau password salah.")
    return None

def heap_sort_proposal(proposals, key, ascending):
    if ascending:
        heap = [(proposal[key], proposal["NAMA PERUSAHAAN"], i, proposal) for i, proposal in enumerate(proposals)]
    else:
        heap = [(-proposal[key], proposal["NAMA PERUSAHAAN"], i, proposal) for i, proposal in enumerate(proposals)]


    build_heap(heap)

    sorted_proposals = []
    while heap:
        _, _, _, proposal = heappop(heap)
        sorted_proposals.append(proposal)

    return sorted_proposals

def cari_proposal(proposals, nama_perusahaan):
    return [p for p in proposals if nama_perusahaan.lower() in p["NAMA PERUSAHAAN"].lower()]

def knapsack_proposal(proposals, modal_investor):
    proposal_rasio = []  # Buat daftar proposal dengan rasio laba/biaya
    for proposal in proposals:
        biaya_original = proposal["BIAYA AWAL"]
        laba_original = proposal["TOTAL LABA INVESTOR"]
        # Gunakan nilai yang dimodifikasi untuk rasio
        biaya = biaya_original / 1000000
        laba = laba_original / 1000000
        # Hindari pembagian dengan nol dan biaya negatif
        rasio = laba / biaya if biaya > 0 else float('-inf') 
        proposal_rasio.append((rasio, biaya_original, laba_original, proposal))
    
    # Urutkan berdasarkan rasio saja
    proposal_rasio.sort(key=lambda x: x[0], reverse=True)
    
    laba_maks = 0
    proposal_diambil = []
    sisa_modal = modal_investor

    # Pilih proposal berdasarkan rasio tertinggi, gunakan biaya_original
    for _, biaya, laba, proposal in proposal_rasio:
        if biaya <= sisa_modal:
            laba_maks += laba
            proposal_diambil.append(proposal)
            sisa_modal -= biaya
    
    return laba_maks, proposal_diambil

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

def menu_urutkan_proposal(proposals, title):
    while True:
        pilihan = tampilkan_menu_urutkan()
        if pilihan is None:
            continue
        if pilihan == 5:
            break
        
        key = None
        ascending = False
        if pilihan == 1:
            key = "ROI INVESTOR"
            ascending = True
        elif pilihan == 2:
            key = "BIAYA AWAL"
            ascending = False
        elif pilihan == 3:
            key = "PAYBACK INVESTOR"
            ascending = False
        elif pilihan == 4:
            key = "PERSENTASE INVESTOR"
            ascending = True
        else:
            print("Pilihan tidak valid.")
            continue
        
        sorted_proposals = heap_sort_proposal(proposals, key, ascending=ascending)
        print(f"\n{title} (Urut berdasarkan {key.replace('_', ' ').title()}):")
        for proposal in sorted_proposals:
            tampilkan_proposal(proposal)
            print("-" * 70)
        input()

def main():
    while True:
        print("\nMenu Awal:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan (1-3): "))
        except ValueError:
            print("Input harus berupa angka 1-3.")
            continue
        
        if pilihan == 1:
            user = sign_up()
            if user:
                menu_utama(user)
        elif pilihan == 2:
            user = log_in()
            if user:
                menu_utama(user)
        elif pilihan == 3:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

def menu_utama(user):
    if user["role"] == "Pengusaha":
        menu_pengusaha(user["username"])
    else:
        menu_investor(user["username"])

def menu_pengusaha(username):
    while True:
        pilihan = tampilkan_menu_pengusaha()
        if pilihan is None:
            continue
        if pilihan == 5:
            break
        
        proposals = baca_dari_csv_proposal()
        my_proposals = [p for p in proposals if p["NAMA PERUSAHAAN"] == username]
        
        if pilihan == 1:
            proposal = input_proposal(username)
            simpan_ke_csv_proposal([proposal])
            print("Proposal berhasil ditambahkan!")
            input()
        elif pilihan == 2:
            if not my_proposals:
                print("Belum ada proposal yang Anda masukkan.")
                input()
            else:
                print("\nDaftar Proposal Anda:")
                for proposal in my_proposals:
                    tampilkan_proposal(proposal)
                    print("-" * 70)
                input()
        elif pilihan == 3:
            if not my_proposals:
                print("Belum ada proposal yang Anda masukkan.")
                input()
            else:
                menu_urutkan_proposal(my_proposals, "Daftar Proposal Anda")
        elif pilihan == 4:
            nama_cari = input("Masukkan nama perusahaan untuk pencarian: ")
            hasil_cari = cari_proposal(proposals, nama_cari)
            if not hasil_cari:
                print("Tidak ada proposal yang cocok dengan nama perusahaan tersebut.")
            else:
                print("\nHasil Pencarian:")
                for proposal in hasil_cari:
                    tampilkan_proposal(proposal)
                    print("-" * 70)
                urut = input("Apakah Anda ingin mengurutkan hasil pencarian? (y/n): ")
                if urut.lower() == 'y':
                    menu_urutkan_proposal(hasil_cari, "Hasil Pencarian")
        else:
            print("Pilihan tidak valid.")

def menu_investor(username):
    while True:
        pilihan = tampilkan_menu_investor()
        if pilihan is None:
            continue
        if pilihan == 5:
            break
        
        proposals = baca_dari_csv_proposal()
        
        if pilihan == 1:
            if not proposals:
                print("Belum ada proposal yang tersedia.")
            else:
                print("\nDaftar Semua Proposal:")
                for proposal in proposals:
                    tampilkan_proposal(proposal)
                    print("-" * 70)
                input()
        elif pilihan == 2:
            if not proposals:
                print("Belum ada proposal yang tersedia.")
                input()
            else:
                menu_urutkan_proposal(proposals, "Daftar Semua Proposal")
        elif pilihan == 3:
            nama_cari = input("Masukkan nama perusahaan untuk pencarian: ")
            hasil_cari = cari_proposal(proposals, nama_cari)
            if not hasil_cari:
                print("Tidak ada proposal yang cocok dengan nama perusahaan tersebut.")
                input()
            else:
                print("\nHasil Pencarian:")
                for proposal in hasil_cari:
                    tampilkan_proposal(proposal)
                    print("-" * 70)
                input()
                urut = input("Apakah Anda ingin mengurutkan hasil pencarian? (y/n): ")
                if urut.lower() == 'y':
                    menu_urutkan_proposal(hasil_cari, "Hasil Pencarian")
        elif pilihan == 4:
            if not proposals:
                print("Belum ada proposal yang tersedia.")
            else:
                try:
                    modal_investor = float(input("Masukkan modal investor (Rp): "))
                    if modal_investor <= 0:
                        print("Modal harus lebih dari 0.")
                        continue
                except ValueError:
                    print("Input harus berupa angka.")
                    continue
                
                laba_maks, proposal_diambil = knapsack_proposal(proposals, modal_investor)
                print(f"\nHasil Optimasi Investasi:")
                print(f"Total Laba Investor Maksimal: Rp {laba_maks:,.0f}")
                total_modal = sum(p["BIAYA AWAL"] for p in proposal_diambil)
                print(f"Total Modal Digunakan: Rp {total_modal:,.0f}")
                if not proposal_diambil:
                    print("Tidak ada proposal yang dapat dipilih dengan modal tersebut.")
                else:
                    print("Proposal yang Dipilih:")
                    for proposal in proposal_diambil:
                        print(f"- {proposal['JUDUL PROYEK']} ({proposal['NAMA PERUSAHAAN']}):")
                        print(f"  Biaya Awal: Rp {proposal['BIAYA AWAL']:,.0f}")
                        print(f"  Durasi Investasi: {proposal['DURASI INVESTASI']} tahun")
                        print(f"  Total Laba Investor: Rp {proposal['TOTAL LABA INVESTOR']:,.0f}")
                        print("-" * 70)
                    input()
        else:
            print("Pilihan tidak valid.")

main()