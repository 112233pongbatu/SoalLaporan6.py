def ganjil(bawah, atas):
    # Bilangan ganjil
    if bawah % 2 == 0:
        bawah += 1
    elif atas % 2 == 0:
        atas -= 1
    # urutan ke atas
    if bawah < atas:
        for i in range(bawah, atas + 1, 2):
            print(i, end=", ")
    # urutan ke bawah
    else:
        for i in range(bawah, atas - 1, -2):
            print(i, end=", ")

    print() 

# Contoh penggunaan fungsi
ganjil(10, 30) 
ganjil(97, 83)  
