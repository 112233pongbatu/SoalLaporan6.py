def hitung_ips():
    print("Program Penghitung IPS Mahasiswa")
    
    # jumlah mata kuliaH
    jumlah_matkul = int(input("Berapa jumlah mata kuliah? "))

    # total bobot x SKS
    total_bobot_sks = 0
    total_sks = jumlah_matkul * 3 

    # Perulangan untuk setiap mata kuliah
    for i in range(1, jumlah_matkul + 1):
        while True:  
            nilai = input(f"Nilai MK {i}: ").upper()
            if nilai in ['A', 'B', 'C', 'D']:  
                break
            print("Input tidak valid! Masukkan nilai A, B, C, atau D.")

        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        else:
            bobot = 1  # D

        # Hitung total bobot x SKS
        total_bobot_sks += bobot * 3  # SKS = 3

    # Menghitung IPS
    ips = total_bobot_sks / total_sks

    # Menampilkan hasil IPS
    print(f"\nNilai IPS anda semester ini {ips:.2f}")

hitung_ips()
