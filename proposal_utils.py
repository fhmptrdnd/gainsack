import csv
from datetime import datetime

def validasi_input(prompt, tipe_data_tujuan, kondisi_valid=lambda x: True, error_message="Input tidak valid."):
    while True:
        try:
            value = tipe_data_tujuan(input(prompt))
            if kondisi_valid(value):
                return value
            else:
                print(error_message + " Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def input_proposal(nama_perusahaan):
    print("Masukkan data untuk proposal investasi:")
    
    judul_proyek = input("Judul proyek: ")
    pendapatan_tahunan = validasi_input(
        "Pendapatan tahunan (Rp): ", float, lambda x: x >= 0, "Pendapatan tidak boleh negatif."
    )
    # batas = validasi_input(
    #     "Biaya investasi awal (Rp): ", float, lambda x: x > 0, "Biaya investasi harus lebih dari 0."
    # )
    # if batas <= pendapatan_tahunan * 5:
    #     batas = pendapatan_tahunan * 5
    #     print("Biaya investasi harus lima kali lipat dari penghasilan.")
    #     print("Biaya investasi yang disesuaikan:", batas)
    # else:
    #     batas = batas
        
    batas = validasi_input(
        "Biaya investasi awal (Rp): ", float,  lambda x: x > 0, "Biaya investasi harus lebih dari 0.")
    pengeluaran_tahunan = validasi_input(
        "Pengeluaran tahunan (Rp): ", float, lambda x: x >= 0, "Pengeluaran tidak boleh negatif."
    )
    durasi_tahun = validasi_input(
        "Durasi investasi (tahun): ", int, lambda x: x > 0, "Durasi investasi harus lebih dari nol."
    )
    persentase_investor = validasi_input(
        "Persentase keuntungan untuk investor (%): ", float, lambda x: 0 < x <= 100, "Persentase harus di antara 0 dan 100."
    )
        

    laba_bersih_tahunan = pendapatan_tahunan - pengeluaran_tahunan
    total_laba_bersih = laba_bersih_tahunan * durasi_tahun
    untung_bersih = total_laba_bersih - batas
    roi = (untung_bersih / batas) * 100 if batas != 0 else 0
    payback_period = batas / laba_bersih_tahunan if laba_bersih_tahunan != 0 else float('inf')

    laba_investor_tahunan = laba_bersih_tahunan * (persentase_investor / 100)
    total_laba_investor = laba_investor_tahunan * durasi_tahun
    roi_investor = (total_laba_investor / batas) * 100 if batas != 0 else 0
    payback_investor = batas / laba_investor_tahunan if laba_investor_tahunan != 0 else float('inf')
    tanggal_input = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "JUDUL PROYEK": judul_proyek,
        "NAMA PERUSAHAAN": nama_perusahaan,
        "BIAYA AWAL": batas,
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
        "PAYBACK INVESTOR": payback_investor,
        "TANGGAL INPUT": tanggal_input
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
    print(f"{'Tanggal Input':<{label_width}}: {proposal['TANGGAL INPUT']}")

def simpan_ke_csv_proposal(daftar_proposal, filename="training_proposal.csv"):
    headers = [
        "JUDUL PROYEK", "NAMA PERUSAHAAN", "BIAYA AWAL", "LABA BERSIH TAHUNAN",
        "TOTAL LABA BERSIH", "UNTUNG BERSIH", "ROI PERUSAHAAN", "PAYBACK PERIOD",
        "DURASI INVESTASI", "PERSENTASE INVESTOR", "LABA INVESTOR TAHUNAN",
        "TOTAL LABA INVESTOR", "ROI INVESTOR", "PAYBACK INVESTOR", "TANGGAL INPUT"
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
            for i, row in enumerate(reader, 1):
                try:
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
                    row["TANGGAL INPUT"] = datetime.strptime(row["TANGGAL INPUT"], "%Y-%m-%d %H:%M:%S")
                    data.append(row)
                except (ValueError, TypeError, KeyError) as e:
                    print(f"\nPeringatan: Melewati baris ke-{i} di file '{filename}' karena ada data yang tidak valid atau hilang. ({e})")
                    continue
            return data
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga saat membaca file CSV: {e}")
        return []