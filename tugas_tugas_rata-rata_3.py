print("Menghitung Nilai Rata-Rata")
def hitung_rata_rata(nama, nilai1, nilai2, nilai3):
    rata_rata = (nilai1 + nilai2 + nilai3) / 3
    return rata_rata

def tentukan_juara(rata_rata):
    if rata_rata > 80:
        return "Juara I"
    elif rata_rata > 75:
        return "Juara II"
    elif rata_rata > 65:
        return "Juara III"
    else:
        return "Tidak Juara"

print("PROGRAM HITUNG NILAI RATA-RATA")
nama_siswa = input("Nama Siswa: ")
nilai_pertandingan1 = float(input("Nilai Pertandingan I: "))
nilai_pertandingan2 = float(input("Nilai Pertandingan II: "))
nilai_pertandingan3 = float(input("Nilai Pertandingan III: "))

rata_rata_nilai = hitung_rata_rata(nama_siswa, nilai_pertandingan1, nilai_pertandingan2, nilai_pertandingan3)
peringkat = tentukan_juara(rata_rata_nilai)

print("\nSiswa yang bernama", nama_siswa)
print("Memperoleh nilai rata-rata", rata_rata_nilai, "dan menjadi", peringkat, "dari hasil perlombaan yang diikutinya")
