def perkalian(x, y):
    # Menghitung hasil perkalian
    hasil_perkalian = x*y

    # Menampilkan hasil
    print(f"(x) x (y) = ", end="")
    print(" + ".join([str(y)] * x), end=" = ")
    print(hasil_perkalian)

perkalian(6,5)
perkalian(7,10)
