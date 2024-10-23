def deret_aritmatika(n):
    a = 2  # nilai awal
    d = 3  # beda (selisih antar bilangan)
    
    deret = [a + i * d for i in range(n)]
    return deret

# Meminta input dari pengguna
n = int(input("Masukkan jumlah elemen (N): "))
hasil = deret_aritmatika(n)

print("Output: ", ', '.join(map(str, hasil)))