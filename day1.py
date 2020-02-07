import math

print("Hello World!")

def my_function():
    # x = 4
    # y = 3
    # z = 2
    # w = pow((x + y * z)/(x * y),z)

    # print(w)

    # a = int(input("Silahkan masukkan angka berapapun : "))
    # print(f"Kuadrat dari {a} = {a**2}")

    # hari = int(input("Berapa hari? : "))

    # tahun = hari//360
    # hari %= 360

    # bulan = hari//30
    # hari %= 30

    # minggu  = hari//7
    # hari %= 7

    # print("Tahun: " + str(tahun))
    # print("Bulan: " + str(bulan))
    # print("Minggu: " + str(minggu))
    # print("Hari: " + str(hari))

    # AndiPlusBudi = 49
    # # 4 : 10
    # rasioAndi = 4
    # rasioBudi = 10

    # AndiDuaTahunLagi = rasioAndi/(rasioAndi+rasioBudi) * AndiPlusBudi + 2
    # BudiDuaTahunLagi = rasioBudi/(rasioAndi+rasioBudi) * AndiPlusBudi + 2

    # print(f'Usia Andi 2 tahun lagi {int(AndiDuaTahunLagi)}')
    # print("Usia Budi 2 tahun lagi " + str(int(BudiDuaTahunLagi)))

    # kalimat = input("Masukkan sebuah kalimat : ")
    # huruf = input("Masukkan huruf yang ingin dicari : ")

    # print(kalimat.count(huruf))

    # word = 'aa'
    # cari = 'a'

    # word_split = word.split(cari)
    # length_word = len(word_split)
    # print(length_word-1)


    jarakAB = 120
    vA = 60
    vB = 40
    startTime = 9

    t = jarakAB/(vA + vB)
    dec = t-int(t)

    print("A dan B tabrakan pada jam " + str(startTime + int(t)) + ":" + str(math.ceil(dec*60)))


    # a = 5
    # b = 6
    
    # a,b = b,a
    # t = a
    # a = b
    # b = t

    #print(f"{a}\n{b}")
    # print(a)
    # print(b)
    


my_function()