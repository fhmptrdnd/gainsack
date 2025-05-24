import csv

def input_proposal():
    print("Masukkan data untuk proposal investasi:")
    nama = input("Nama proposal: ")
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
        "NAMA": nama,
        "BIAYA AWAL": biaya_awal,
        "LABA BERSIH TAHUNAN": laba_bersih_tahunan,
        "TOTAL LABA BERSIH": total_laba_bersih,
        "UNTUNG BERSIH": untung_bersih,
        "ROI": roi,
        "PAYBACK PERIOD": payback_period,
        "PERSENTASE INVESTOR": persentase_investor,
        "LABA INVESTOR TAHUNAN": laba_investor_tahunan,
        "TOTAL LABA INVESTOR": total_laba_investor,
        "ROI INVESTOR": roi_investor,
        "PAYBACK INVESTOR": payback_investor
    }

def tampilkan_proposal(proposal):
    # Lebar kolom label disesuaikan agar tanda ":" rata
    label_width = 38  # Lebar maksimum untuk label agar ":" sejajar

    print(f"\n{'Nama Perusahaan/Proposal':<{label_width}}: {proposal['NAMA']}")
    print(f"{'Biaya Investasi Awal':<{label_width}}: Rp {proposal['BIAYA AWAL']:,.0f}")
    print(f"{'Laba Bersih Tahunan':<{label_width}}: Rp {proposal['LABA BERSIH TAHUNAN']:,.0f}")
    print(f"{'Total Laba Bersih':<{label_width}}: Rp {proposal['TOTAL LABA BERSIH']:,.0f}")
    print(f"{'Untung Bersih':<{label_width}}: Rp {proposal['UNTUNG BERSIH']:,.0f}")
    print(f"{'ROI Perusahaan':<{label_width}}: {proposal['ROI']:.2f}%")
    print(f"{'Payback Period':<{label_width}}: {proposal['PAYBACK PERIOD']:.2f} tahun")
    print(f"{'Persentase Keuntungan untuk Investor':<{label_width}}: {proposal['PERSENTASE INVESTOR']:.2f}%")
    print(f"{'Laba Investor Tahunan':<{label_width}}: Rp {proposal['LABA INVESTOR TAHUNAN']:,.0f}")
    print(f"{'Total Laba Investor':<{label_width}}: Rp {proposal['TOTAL LABA INVESTOR']:,.0f}")
    print(f"{'ROI Investor':<{label_width}}: {proposal['ROI INVESTOR']:.2f}%")
    print(f"{'Payback Period untuk Investor':<{label_width}}: {proposal['PAYBACK INVESTOR']:.2f} tahun")

def simpan_ke_csv(daftar_proposal, filename="training_proposal.csv"):
    headers = [
        "NAMA", "BIAYA AWAL", "LABA BERSIH TAHUNAN", "TOTAL LABA BERSIH",
        "UNTUNG BERSIH", "ROI", "PAYBACK PERIOD", "PERSENTASE INVESTOR",
        "LABA INVESTOR TAHUNAN", "TOTAL LABA INVESTOR", "ROI INVESTOR",
        "PAYBACK INVESTOR"
    ]
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        for proposal in daftar_proposal:
            writer.writerow(proposal)

def main():
    daftar_proposal = []
    while True:
        proposal = input_proposal()
        daftar_proposal.append(proposal)
        
        lagi = input("Apakah Anda ingin memasukkan proposal lain? (y/n): ")
        if lagi.lower() != 'y':
            break
    
    simpan_ke_csv(daftar_proposal)
    
    print("\nDaftar Proposal Investasi:")
    for proposal in daftar_proposal:
        tampilkan_proposal(proposal)
        print("-" * 70)

if __name__ == "__main__":
    main()