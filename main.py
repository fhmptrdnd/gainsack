import os
import platform
import time
import menu_display
import auth_utils
import proposal_utils
import algorithms

def clear_screen():
    command = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(command)

def menu_urutkan_proposal(proposals, title):
    while True:
        clear_screen()
        pilihan = menu_display.tampilkan_menu_urutkan()
        if pilihan is None:
            input("Tekan Enter untuk coba lagi...")
            continue
        if pilihan == 6:
            break
        
        key = None
        ascending = False
        if pilihan == 1:
            key = "ROI INVESTOR"
        elif pilihan == 2:
            key = "BIAYA AWAL"
            ascending = False
        elif pilihan == 3:
            key = "PAYBACK INVESTOR"
            ascending = True
        elif pilihan == 4:
            key = "PERSENTASE INVESTOR"
            ascending = False
        elif pilihan == 5:
            key = "TANGGAL INPUT"
            ascending = True
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
            continue
        
        clear_screen()
        sorted_proposals = algorithms.heap_sort_proposal(proposals, key, ascending=ascending)
        print(f"\n{title} (Urut berdasarkan {key.replace('_', ' ').title()}):")
        for proposal in sorted_proposals:
            proposal_utils.tampilkan_proposal(proposal)
            print("-" * 70)
        input("\nTekan Enter untuk kembali...")

def menu_pengusaha(username):
    while True:
        clear_screen()
        print(f"Selamat datang, Pengusaha {username}! ✨")
        pilihan = menu_display.tampilkan_menu_pengusaha()
        if pilihan is None:
            input("Tekan Enter untuk coba lagi...")
            continue
        if pilihan == 5:
            break
        
        proposals = proposal_utils.baca_dari_csv_proposal()
        my_proposals = [p for p in proposals if p["NAMA PERUSAHAAN"] == username]
        
        if pilihan == 1:
            clear_screen()
            proposal = proposal_utils.input_proposal(username)
            proposal_utils.simpan_ke_csv_proposal([proposal])
            print("\nProposal berhasil ditambahkan!")
            input("Tekan Enter untuk kembali ke menu...")
        # elif pilihan == 2:
        #     clear_screen()
        #     if not my_proposals:
        #         print("Belum ada proposal yang Anda masukkan.")
        #     else:
        #         print("\nDaftar Proposal Anda:")
        #         tampilkan = proposal_utils.baca_dari_csv_proposal()
        #         if tampilkan:
        #             my_proposals = tampilkan[:3]
        #             for proposal in my_proposals:
        #                 proposal_utils.tampilkan_proposal(proposal)
        #                 # menu_urutkan_proposal(my_proposals, "Daftar Proposal Anda")
        #                 print("-" * 70)
        #     input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == 2:
            clear_screen()
            if not my_proposals:
                print("Belum ada proposal yang Anda masukkan.")
            else:
                print("\nDaftar Proposal Anda:")
                for proposal in my_proposals[:3]:
                    proposal_utils.tampilkan_proposal(proposal)
                    # menu_urutkan_proposal(my_proposals, "Daftar Proposal Anda")
                    print("-" * 70)
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == 3:
            if not my_proposals:
                clear_screen()
                print("Belum ada proposal yang Anda masukkan untuk diurutkan.")
                input("\nTekan Enter untuk kembali ke menu...")
            else:
                menu_urutkan_proposal(my_proposals, "Daftar Proposal Anda")
        elif pilihan == 4:
            clear_screen()
            nama_cari = input("Masukkan nama perusahaan untuk pencarian: ")
            hasil_cari = algorithms.cari_proposal(proposals, nama_cari)
            clear_screen()
            if not hasil_cari:
                print("Tidak ada proposal yang cocok dengan nama perusahaan tersebut.")
            else:
                print("\nHasil Pencarian:")
                for proposal in hasil_cari:
                    proposal_utils.tampilkan_proposal(proposal)
                    print("-" * 70)
                
                urut = input("\nApakah Anda ingin mengurutkan hasil pencarian? (y/n): ")
                if urut.lower() == 'y':
                    menu_urutkan_proposal(hasil_cari, "Hasil Pencarian")
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali ke menu...")

def menu_investor(username):
    while True:
        clear_screen()
        print(f"Selamat datang, Investor {username}! 💸")
        pilihan = menu_display.tampilkan_menu_investor()
        if pilihan is None:
            input("Tekan Enter untuk coba lagi...")
            continue
        if pilihan == 5:
            break
        
        proposals = proposal_utils.baca_dari_csv_proposal()
        
        if pilihan == 1:
            clear_screen()
            if not proposals:
                print("Belum ada proposal yang tersedia.")
            else:
                print("\nDaftar Semua Proposal:")
                for proposal in proposals:
                    proposal_utils.tampilkan_proposal(proposal)
                    print("-" * 70)
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == 2:
            if not proposals:
                clear_screen()
                print("Belum ada proposal yang tersedia untuk diurutkan.")
                input("\nTekan Enter untuk kembali ke menu...")
            else:
                menu_urutkan_proposal(proposals, "Daftar Semua Proposal")
        elif pilihan == 3:
            clear_screen()
            nama_cari = input("Masukkan nama perusahaan untuk pencarian: ")
            hasil_cari = algorithms.cari_proposal(proposals, nama_cari)
            clear_screen()
            if not hasil_cari:
                print("Tidak ada proposal yang cocok dengan nama perusahaan tersebut.")
            else:
                print("\nHasil Pencarian:")
                for proposal in hasil_cari:
                    proposal_utils.tampilkan_proposal(proposal)
                    print("-" * 70)
                
                urut = input("\nApakah Anda ingin mengurutkan hasil pencarian? (y/n): ")
                if urut.lower() == 'y':
                    menu_urutkan_proposal(hasil_cari, "Hasil Pencarian")
        elif pilihan == 4:
            clear_screen()
            if not proposals:
                print("Belum ada proposal yang tersedia.")
            else:
                try:
                    modal_investor = float(input("Masukkan modal investor (Rp): "))
                    if modal_investor <= 0:
                        print("Modal harus lebih dari 0.")
                        input("\nTekan Enter untuk kembali...")
                        continue
                except ValueError:
                    print("Input harus berupa angka.")
                    input("\nTekan Enter untuk kembali...")
                    continue
                
                clear_screen()
                laba_maks, proposal_diambil = algorithms.knapsack_proposal(proposals, modal_investor)
                print(f"\nHasil Optimasi Investasi:")
                print(f"Total Laba Investor Maksimal: Rp {laba_maks:,.0f}")
                total_modal = sum(p["BIAYA AWAL"] for p in proposal_diambil)
                print(f"Total Modal Digunakan: Rp {total_modal:,.0f}")
                if not proposal_diambil:
                    print("\nTidak ada proposal yang dapat dipilih dengan modal tersebut.")
                else:
                    print("\nProposal yang Dipilih:")
                    for proposal in proposal_diambil:
                        print(f"- {proposal['JUDUL PROYEK']} ({proposal['NAMA PERUSAHAAN']}):")
                        print(f"  Biaya Awal: Rp {proposal['BIAYA AWAL']:,.0f}")
                        print(f"  Durasi Investasi: {proposal['DURASI INVESTASI']} tahun")
                        print(f"  Total Laba Investor: Rp {proposal['TOTAL LABA INVESTOR']:,.0f}")
                        print("-" * 70)
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali ke menu...")

def menu_utama(user):
    print(user["username"])
    if user["role"].lower() == "pengusaha":
        menu_pengusaha(user["username"])
    else:
        menu_investor(user["username"])

def main():
    while True:
        clear_screen()
        pilihan = menu_display.tampilkan_menu_awal()
        if pilihan is None:
            input("Tekan Enter untuk coba lagi...")
            continue
        
        if pilihan == 1:
            clear_screen()
            user = auth_utils.sign_up()
            if user:
                print("\nSign up berhasil! Selamat datang!")
                time.sleep(1)
                clear_screen()

                print("\nMemulai Aplikasi...")
                time.sleep(1)
                clear_screen()

                print("\nMenyiapkan Investasi Terbaik Untukmu")
                time.sleep(1)
                clear_screen()

                print("\nYuk Mulai...")
                time.sleep(1)
                menu_utama(user)
            else:
                input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == 2:
            clear_screen()
            user = auth_utils.log_in()
            if user:
                clear_screen()
                print("\nLog in berhasil! Menyiapkan menu")
                time.sleep(1)
                clear_screen()

                print("\nMemulai Aplikasi...")
                time.sleep(1)
                clear_screen()

                print("\nMenyiapkan Investasi Terbaik Untukmu")
                time.sleep(1)
                clear_screen()

                print("\nYuk Mulai...")
                time.sleep(1)
                menu_utama(user)
            else:
                input("\nUsername atau password salah. Tekan Enter untuk kembali...")
        elif pilihan == 3:
            print("\nKeluar dari program. Sampai jumpa lagi! 👋")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali ke menu utama...")

main()