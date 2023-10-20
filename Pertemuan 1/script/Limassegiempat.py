print("Aplikasi menghitung luas permukaan dan volume limas segi empat")

# Atur nilai variabel
luas_alas = 16  
panjang_sisi = 4  
tinggi = 8  

# Rumus
luas_permukaan = luas_alas + 4 * (0.5 * panjang_sisi * tinggi)
volume = (1/3) * luas_alas * tinggi

# Output
print("Luas Alas =", luas_alas)
print("Panjang Sisi Dasar =", panjang_sisi)
print("Tinggi Limas =", tinggi)
print("Luas Permukaan =", luas_permukaan)
print("Volume =", volume)