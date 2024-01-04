from mahasiswa import *
A = Mahasiswa()


A.nim = "170511019"
A.nama = "Fitri Azahra "
A.jk = "P"   
A.kode_prodi = "PGSD"

A.updateByNIM("170511019")
B = A.getByNIM("170511019")
print(B)
