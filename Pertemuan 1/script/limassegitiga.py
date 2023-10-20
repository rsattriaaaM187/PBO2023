print("Aplikasi menghitung luas permukaan dan volume limas segi tiga")

# Atur nilai variabel
keliling_segitiga_alas = 18 
tinggi_limas = 8 
luas_segitiga_alas = 36 

# Rumus
luas_permukaan = (0.5 * keliling_segitiga_alas * tinggi_limas) + luas_segitiga_alas
volume = (1/3) * luas_segitiga_alas * tinggi_limas

# Output
print("Keliling Segitiga Alas =", keliling_segitiga_alas)
print("Tinggi Limas =", tinggi_limas)
print("Luas Segitiga Alas =", luas_segitiga_alas)
print("Luas Permukaan =", luas_permukaan)
print("Volume =", volume)
