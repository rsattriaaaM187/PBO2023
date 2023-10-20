print("Aplikasi menghitung luas permukaan dan volume prisma segitiga")

# Atur nilai variabel
luas_segitiga_alas = 24  
keliling_segitiga_alas = 18  
tinggi_prisma = 10  

# Rumus
luas_permukaan = (2 * luas_segitiga_alas) + (keliling_segitiga_alas * tinggi_prisma)
volume = luas_segitiga_alas * tinggi_prisma

# Output
print("Luas Segitiga Alas =", luas_segitiga_alas)
print("Keliling Segitiga Alas =", keliling_segitiga_alas)
print("Tinggi Prisma =", tinggi_prisma)
print("Luas Permukaan =", luas_permukaan)
print("Volume =", volume)
