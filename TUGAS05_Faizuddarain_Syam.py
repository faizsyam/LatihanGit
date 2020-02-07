import os

produkList = [['Jeruk', 5000], ['Apel', 8000]]

def mainMenu() :
    os.system("cls")
    print("\nPilih Menu:")
    print("1) Show produk")
    print("2) Tambahkan produk")
    print("3) Update harga")
    print("4) Hapus produk")
    print("5) Exit")
    pilihan = input("> ")

    while (True) :
        if pilihan.isdigit() :
            if 1 <= int(pilihan) <= 5 :
                break
            else :
                print("Input di luar jangakauan. Coba lagi.")
        else :
            print("Input harus angka. Coba lagi.")
        pilihan = input("> ")
    return pilihan

def showProduk() :
    os.system("cls")
    print("\nList produk:")
    print("Nama \t\t Harga")
    print("---------------------------")
    if len(produkList) == 0 :
        print("List produk kosong.")
    else :
        for i in range(len(produkList)) :
            print(str(i+1) + ") " + produkList[i][0] + "  \t Rp." + str(produkList[i][1]))

def tambahProduk() :
    os.system("cls")
    print("\nMasukkan Nama produk.")
    namaProduk = input("> ")
    while (True) :
        if namaProduk != "" :
            break
        else :
            print("Nama produk tidak boleh kosong. Coba lagi.")
            namaProduk = input("> ")
    print("Masukkan Harga produk.")
    hargaProduk = input("> ")
    while (True) :
        if hargaProduk.isdigit() :
            break
        else :
            print("Input harus angka. Coba lagi.")
            hargaProduk = input("> ")
    produkList.append([namaProduk, int(hargaProduk)])
    print("Data berhasil ditambahkan.")

def updateHarga() :
    os.system("cls")
    print("\nMasukkan Nama produk yang ingin diupdate.")
    namaProduk = input("> ")
    itemFound = False
    while(not itemFound) :
        for i in range(len(produkList)) :
            if produkList[i][0].lower() == namaProduk.lower() :
                itemFound = True
                break
        if not itemFound :
            print(f"Data dengan nama '{namaProduk}' tidak ditemukan. Coba lagi.'")
            namaProduk = input("> ")
    print("Masukkan update Harga produk tersebut.")
    hargaProduk = input("> ")
    while (True) :
        if hargaProduk.isdigit() :
            break
        else :
            print("Input harus angka. Coba lagi.")
            hargaProduk = input("> ")
    produkList[i][1] = int(hargaProduk)
    print("Data berhasil diupdate.")

def hapusProduk() :
    os.system("cls")
    print("\nMasukkan Nama produk yang ingin dihapus.")
    namaProduk = input("> ")
    itemFound = False
    urutanItem = -1
    while(not itemFound) :
        for i in range(len(produkList)) :
            if produkList[i][0].lower() == namaProduk.lower() :
                itemFound = True
                urutanItem = i
                break
        if not itemFound :
            print(f"Data dengan nama '{namaProduk}' tidak ditemukan. Coba lagi.'")
            namaProduk = input("> ")
    del produkList[urutanItem]
    print("Data berhasil dihapus.")

while(True) :
    inputmain = mainMenu()
    
    if inputmain != '5' :
        if inputmain == '1' :
            showProduk()
        elif inputmain == '2' :
            tambahProduk()
        elif inputmain == '3' :
            updateHarga()
        elif inputmain == '4' :
            hapusProduk()

        tmp = input("\nTekan Enter..")

    else :
        pilihan1 = input("Yakin mau Exit? (Y/N) : ")
        while pilihan1 != "Y" and pilihan1 !="y" and pilihan1 != "N" and pilihan1 !="n":
            print("Input invalid. Coba lagi.")
            pilihan1 = input("> ")
        if pilihan1 == "Y" or  pilihan1 =="y" :
            break
