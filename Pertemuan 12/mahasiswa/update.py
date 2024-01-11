from mahasiswa import *
A = Mahasiswa()


A.nim = "100511019"
A.nama = "WPP KaliFHA "
A.jk = "L"   
A.kode_prodi = "PGSD"

A.updateByNIM("100511019")
B = A.getByNIM("100511019")
print(B)
