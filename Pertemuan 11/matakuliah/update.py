from matakuliah import *

A = matakuliah()
A.kodemk = "2453"
A.namamk = "PEMOGRAMAN TERSTRUKTUR"
A.sks = "3"


A.update(5) 
B = A.getById(5)  
print(B)
