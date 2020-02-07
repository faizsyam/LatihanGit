import os

while(True) :
    os.system("cls")
    print("\nPilih Menu:")
    print("1) Segitiga Siku-siku")
    print("2) Segitiga Sama Kaki")
    print("3) Persegi")
    print("4) Exit")
    pilihan = input("> ")

    while (True) :
        if pilihan.isdigit() :
            if 1 <= int(pilihan) <= 4 :
                break
            else :
                print("Input di luar rentang 1-4. Coba lagi.")
        else :
            print("Input harus Angka. Coba lagi.")
        pilihan = input("> ")

    if pilihan != "4" :
        while(True) :
            os.system("cls")
            nBaris  = input("\nBerapa baris? (1 - 10): ")
            while (True) :
                if nBaris.isdigit() :
                    if 1 <= int(nBaris) <= 10 :
                        break
                    else :
                        print("Input di luar rentang 1-10. Coba lagi.")
                else :
                    print("Input harus Angka. Coba lagi.")
                nBaris = input("> ")

            nBaris = int(nBaris)
            
            for x in range(nBaris) :
                if pilihan == "1" :
                    print("  " * (nBaris - x - 1) + "* " * (x + 1))
                elif pilihan == "2" :
                    print(" " * (nBaris - x - 1) + "* " * (x + 1))
                else :
                    print("* " * (nBaris))

            kembali = input("\nApakah akan ke menu awal? (Y/N) : ")

            while kembali != "Y" and kembali !="y" and kembali != "N" and kembali !="n":
                print("Input invalid. Coba lagi.")
                kembali = input("> ")
            if kembali == "Y" or  kembali == "y" :
                break

    else :
        pilihan1 = input("Yakin mau Exit? (Y/N) : ")
        while pilihan1 != "Y" and pilihan1 !="y" and pilihan1 != "N" and pilihan1 !="n":
            print("Input invalid. Coba lagi.")
            pilihan1 = input("> ")
        if pilihan1 == "Y" or  pilihan1 == "y" :
            break
