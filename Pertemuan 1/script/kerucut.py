
import math
print("Aplikasi menghitung luas permukaan dan volume kerucut")

# Atur nilai variabel
jari_jari = 4.0  
tinggi = 7.0  

# Hitung panjang sisi kerucut
sisi = math.sqrt(jari_jari**2 + tinggi**2)

# Rumus
luas_permukaan = math.pi * jari_jari * (jari_jari + sisi)
volume = (1/3) * math.pi * jari_jari**2 * tinggi

# Output
print("Jari-Jari Kerucut =", jari_jari)
print("Tinggi Kerucut =", tinggi)
print("Panjang Sisi Kerucut (s) =", sisi)
print("Luas Permukaan =", luas_permukaan)
print("Volume =", volume)
