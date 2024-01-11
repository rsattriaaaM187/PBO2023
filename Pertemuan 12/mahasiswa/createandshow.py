from mahasiswa import *


A = Mahasiswa()
A.nim = "100511019"
A.nama = "WPP KaliFHA"
A.jk = "L"
A.kode_prodi = "TIF"


A.simpan()
B = A.getAllData()

print(B)
