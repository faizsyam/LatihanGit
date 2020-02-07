import os

dictionary = { 'Nama' : 'Faiz', 'Usia' : 23}

def inputAngka(text, maxrange = 9999999999, minrange = 1) :
    i = input(text)
    while (True) :
        if i.isdigit() :
            if minrange <= int(i) <= maxrange :
                break
            else :
                print("Input di luar jangakauan. Coba lagi.")
        else :
            print("Input harus angka. Coba lagi.")
        i = input("> ")
    return i

def mainMenu() :
    os.system("cls")
    print("\nPilih Menu:")
    print("1) Menu Dictionary")
    print("2) Add Dictionary")
    print("3) Search Dictionary")
    print("4) Exit")

    return inputAngka("> ", 4)

def menuDictionary(newDict = dictionary) :
    os.system("cls")
    listDictKeys = list(newDict)
    print("\n|      Key     |     Value     |")
    for i in range(len(newDict)) :
        print(str(i+1) + "." + listDictKeys[i].center(13) + " " + str(dictionary[listDictKeys[i]]).center(15))

def addDictionary() :
    os.system("cls")
    print("\nBerapa kali masukan dictionary?")
    n = int(inputAngka("> "))
    for i in range(n) :
        print ("Pilih tipe Dictionary:\n 1) String\n 2) Number")
        pilihan = inputAngka("> ", 2)
        newKey = input("Key: ")
        if pilihan == "1" :
            newValue = input("Value: ")
        else :
            newValue = inputAngka("Value: ")
        dictionary[newKey] = newValue
        print("Data berhasil ditambahkan.\n")
    
def searchDictionary() :
    os.system("cls")
    kata = input("\nCari kata: ")
    listDictKeys = list(dictionary.keys())
    filteredDictionary = list(filter(lambda key: key.lower().find(kata.lower()) != -1, listDictKeys))
    menuDictionary(filteredDictionary)

while(True) :
    inputmain = mainMenu()
    
    if inputmain != '4' :
        menuList = [menuDictionary, addDictionary, searchDictionary]
        index = int(inputmain) - 1
        menuList[index]()

        tmp = input("\nKembali ke Menu Awal? (y/n) : ")
        while tmp != "y" and tmp != "n" :
            print("Input invalid. Coba lagi.")
            tmp = input("> ")
        if tmp == "n" :
            break
    else :
        pilihan1 = input("Yakin mau Exit? (y/n) : ")
        while pilihan1 !="y" and pilihan1 !="n":
            print("Input invalid. Coba lagi.")
            pilihan1 = input("> ")
        if pilihan1 =="y" :
            break

os.system("cls")
print("\nTerimakasih telah menggunakan aplikasi sederhana ini!")