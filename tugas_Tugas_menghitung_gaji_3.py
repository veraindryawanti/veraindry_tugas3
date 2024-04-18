def hitung_tunjangan_jabatan(golongan):
    if golongan == 1:
        return 0.05 * 300000
    elif golongan == 2:
        return 0.10 * 300000
    elif golongan == 3:
        return 0.15 * 300000
    else:
        return 0

def hitung_tunjangan_pendidikan(pendidikan):
    if pendidikan == "SMA":
        return 0.025 * 300000
    elif pendidikan == "D1":
        return 0.05 * 300000
    elif pendidikan == "D3":
        return 0.20 * 300000
    elif pendidikan == "S1":
        return 0.30 * 300000
    else:
        return 0

def hitung_honor_lembur(jam_kerja):
    jam_normal = 8
    if jam_kerja > jam_normal:
        lembur = jam_kerja - jam_normal
        return lembur * 3500
    else:
        return 0

print("PROGRAM HITUNG NILAI AKHIR")
nama_karyawan = input("Nama Karyawan: ")
golongan_jabatan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Jumlah jam kerja (Jam): "))

tunjangan_jabatan = hitung_tunjangan_jabatan(golongan_jabatan)
tunjangan_pendidikan = hitung_tunjangan_pendidikan(pendidikan)
honor_lembur = hitung_honor_lembur(jam_kerja)

print("\nKaryawan yang bernama", nama_karyawan)
print("Honor yang diterima:")
print("Tunjangan Jabatan Rp", tunjangan_jabatan)
print("Tunjangan Pendidikan Rp", tunjangan_pendidikan)
print("Honor Lembur Rp", honor_lembur)
print("+")
print("Honor Lembur Rp", honor_lembur)

total_honor = tunjangan_jabatan + tunjangan_pendidikan + honor_lembur * 2
print("Total Honor:", total_honor)
