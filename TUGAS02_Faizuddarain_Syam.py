import os

while(True) :
    os.system("cls")
    print("\nPilih Menu:")
    print("1) Belajar")
    print("2) Belanja")
    print("3) Exit")
    pilihan = input("> ")

    while (True) :
        if pilihan.isdigit() :
            if 1 <= int(pilihan) <= 3 :
                break
        print("Input invalid. Coba lagi.")
        pilihan = input("> ")

    if pilihan == "1" :
        os.system("cls")
        print("\nPilih Perhitungan Luas:")
        print("1) Segitiga")
        print("2) Trapesium")
        print("3) Kembali")
        pilihan1 = input("> ")

        while (True) :
            if pilihan1.isdigit() :
                if 1 <= int(pilihan1) <= 3 :
                    break
            print("Input invalid. Coba lagi.")
            pilihan1 = input("> ")
        
        if pilihan1 == "1" :
            alas = input("Input panjang ALAS : ")
            while (not alas.isdigit()) :
                print("Input invalid. Coba lagi.")
                alas = input("> ")

            tinggi = input("Input panjang TINGGI : ")
            while (not tinggi.isdigit()) :
                print("Input invalid. Coba lagi.")
                tinggi = input("> ")

            print(f"Luas segitiga adalah {float(alas)*float(tinggi)/2}")
        elif pilihan1 == "2" :
            alas1 = input("Input panjang ALAS 1 : ")
            while (not alas1.isdigit()) :
                print("Input invalid. Coba lagi.")
                alas1 = input("> ")

            alas2 = input("Input panjang ALAS 2 : ")
            while (not alas2.isdigit()) :
                print("Input invalid. Coba lagi.")
                alas2 = input("> ")

            tinggi = input("Input panjang TINGGI : ")
            while (not tinggi.isdigit()) :
                print("Input invalid. Coba lagi.")
                tinggi = input("> ")

            print(f"Luas trapesium adalah {(float(alas1) + float(alas2))*float(tinggi)/2}")

        if pilihan1 != "3" :
            pilihan1 = input("\nPress enter..")

    elif pilihan == "2" :
        os.system("cls")
        print("\nMenu makan siang:")
        print("1) Ayam Bakar \t Rp.15.000")
        print("2) Ayam Geprek \t Rp.18.000")
        print("3) Ikan Bakar \t Rp.25.000")
        print("4) Kembali")
        pilihan1 = input("> ")

        while (True) :
            if pilihan1.isdigit() :
                if 1 <= int(pilihan1) <= 4 :
                    break
            print("Input invalid. Coba lagi.")
            pilihan1 = input("> ")
        
        if pilihan1 != "4" :
            kuantitas = input("Berapa kuantitas? : ")

            while (not kuantitas.isdigit()) :
                print("Input invalid. Coba lagi.")
                kuantitas = input("> ")

            totalHarga = 0
            if pilihan1 == "1":
                totalHarga = int(kuantitas) * 15000
            elif pilihan1 == "2" :
                totalHarga = int(kuantitas) * 18000
            elif pilihan1 == "3" :
                totalHarga = int(kuantitas) * 25000
            print(f"Total Harga : Rp.{totalHarga}")
            pilihan1 = input("\nPress enter..")

    elif pilihan == "3" :
        pilihan1 = input("Yakin mau Exit? (Y/N) : ")
        while pilihan1 != "Y" and pilihan1 !="y" and pilihan1 != "N" and pilihan1 !="n":
            print("Input invalid. Coba lagi.")
            pilihan1 = input("> ")
        if pilihan1 == "Y" or  pilihan1 =="y" :
            break
