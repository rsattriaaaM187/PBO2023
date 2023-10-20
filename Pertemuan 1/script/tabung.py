import math

print("Aplikasi menghitung luas permukaan dan volume tabung")

# Atur nilai variabel
jari_jari = 5.0  
tinggi = 10.0  

# Rumus
luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
volume = math.pi * jari_jari**2 * tinggi

# Output
print("Jari-Jari Tabung =", jari_jari)
print("Tinggi Tabung =", tinggi)
print("Luas Permukaan =", luas_permukaan)
print("Volume =", volume)
