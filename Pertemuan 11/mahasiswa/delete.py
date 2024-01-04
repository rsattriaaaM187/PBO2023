from mahasiswa import *

A = Mahasiswa()
nim = "170511019"
A.deleteByNIM(nim)
B = A.getAllData()
print(B)
