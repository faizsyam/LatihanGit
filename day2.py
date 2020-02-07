# if, elif, else ..

# n1 = int(input("Masukkan angka pertama : "))
# n2 = int(input("Masukkan angka kedua : "))
# op = input("Mau melakukan apa? (*,/,-,+,%) : ")

# hasil = 0
# if op == "+" :
#     hasil = n1 + n2
# elif op == "-" :
#     hasil = n1 - n2
# elif op == "*" :
#     hasil = n1 * n2
# elif op == "/" :
#     hasil = n1 / n2
# elif op == "%" :
#     hasil = n1 % n2

# print(f"Hasil {n1} {op} {n2} adalah {hasil}")

# a = int(input("Masukkan angka : "))
# if a % 2 == 0 :
#     print("Angka " + str(a) + " tergolong bilangan GENAP!")
# else :
#     print("Angka " + str(a) + " tergolong bilangan GANJIL!")

# massa = int(input("Masukkan Massa(kg) : "))
# tinggi = int(input("Masukkan Tinggi(cm) : "))

# print("Massa " + str(massa) + " kg & tinggi " + str(tinggi/100) + " m")

# imt = round(massa / (tinggi/100)**2, 2)

# if imt < 18.5 :
#     print("IMT = " + str(imt) + ", BERAT BADAN KURANG!")
# elif imt <= 24.9 :
#     print("IMT = " + str(imt) + ", BERAT BADAN IDEAL!")
# elif imt <= 29.9 :
#     print("IMT = " + str(imt) + ", BERAT BADAN BERLEBIH!")
# elif imt <= 39.9 :
#     print("IMT = " + str(imt) + ", BERAT BADAN SANGAT BERLEBIH!")
# else :
#     print("IMT = " + str(imt) + ", OBESITAS!")


########################################################################

# Loop

n = 5
z = ""

# for x in range(0, n) :
#     for y in range(0, n - x) :
#         z += " * "
#     z += "\n"
# print(z)

# for x in range(0, n) :
#     print(" * " * (n - x))

# for x in range(0, n - 1) :
#     print(" * " * (x + 2))
    
# n = int(input("Size? "))
# for x in range(0, n) :
#     print(" " * (n - x - 1) + "* " * (x))


n = int(input("Size? "))

for i in range(0, n - 1) :
    for j in range(0, n * 2 - 1) :
        if n - i <= j <= n + i - 2:
            print(end= "  ")
        else :
            print(end= "X ")
    print("")

for i in range(0, n) :
    for j in range(0, n * 2 - 1) :
        if i + 1 <= j <= 2 * n - i - 3:
            print(end= "  ")
        else :
            print(end= "X ")
    print("")

count = 1
for i in range(n) :
    for j in range(n - i) :
        print(end= str(count) + " ")
        if count < 10 :
            print(end= " ")
        count += 2
    print()


# for x in range(n, 0, -1) :
#     print("   " * (n - x) + " * " * (x * 2 - 1))



n = 5

# for x in range(0, n) :
#     print("   " * (n - x - 1) + " * " * (x * 2 + 1))
# for x in range(n, 0, -1) :
#     print("   " * (n - x) + " * " * (x * 2 - 1))

# print(z)

#########################################################################

x = [40, 100, 1, 5, 25, 10]

# def mySort(xList) :
#     for item1 in range(0, len(xList) - 1) :
#         for item2 in range(item1, len(xList)) :
#             if(xList[item2 - 1] > xList[item2]) :
#                 t = xList[item2 - 1]
#                 xList[item2 - 1] = xList[item2]
#                 xList[item2] = t
#     return xList

# def findHighestAndLowest(xList) :
#     highest = 0
#     lowest = 0
#     for item in x :
#         if item == x[0] :
#             highest = item
#             lowest = item
#         else :
#             if item > highest :
#                 highest = item
#             if item < lowest :
#                 lowest = item
#     return [highest, lowest]

# print(mySort(x))

# tList = findHighestAndLowest(x)
# highest = tList[0]
# lowest = tList[1]

# print(f"Highest = {highest}")
# print(f"Lowest = {lowest}")


######################################################################


# listKata = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
# print(listKata)

# cari = input("Search : ")
# listTemu = []
# for item in listKata :
#     n = item.lower().find(cari.lower())
#     if n != -1 :
#         listTemu.append(item)

# print(listTemu)

