from mahasiswa import *

A = Mahasiswa()
nim = "100511019"
A.deleteByNIM(nim)
B = A.getAllData()
print(B)
