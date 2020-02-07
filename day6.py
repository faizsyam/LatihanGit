
# def bebas(kalimat, huruf) :
#     rmv = kalimat.replace(huruf.upper(), '')
#     rmv = rmv.replace(huruf.lower(), '')
#     print(rmv)

# bebas('Anugrah', 'a')


# def MainSuit(ply1, ply2) :
#     yang_boleh = ['batu', 'gunting', 'kertas']
#     if not any(ply2 in s for s in yang_boleh) and not any(ply2 in s for s in yang_boleh) :
#         print("invalid")
#         return
    
#     print(end= "Player 1 " + ply1 + " player 2 " + ply2)

#     if ply1 == ply2 :
#         print (", Draw. Semua menang!")
#     elif ply1 == 'batu' :
#         if ply2 == 'gunting' :
#             print(", Player 1 menang!")
#         else :
#             print (", Player 2 menang!")
#     elif ply1 == "gunting" :
#         if ply2 == 'batu' :
#             print (", Player 2 menang!")
#         else :
#             print(", Player 1 menang!")
#     else :
#         if ply2 == 'batu' :
#             print (", Player 1 menang!")
#         else :
#             print (", Player 2 menang!")


# MainSuit("kertas", "kertas")

# def perkalian (angka1 = 5, angka2 = 2) :
#     return angka1 * angka2

# print(perkalian(angka2= 4))

# def remove_vowel(kalimat) :
#     vowel = ('a', 'i', 'u', 'e', 'o')

#     for i in vowel :
#         kalimat = kalimat.replace(i, "")
#         kalimat = kalimat.replace(i.upper(), "")

#     return kalimat

# print(remove_vowel("Aku Anak Sehat Tubuhku KuAt"))

def bintang(n):
    if n > 0 :
        print("*" * n)
        bintang(n-1)

# def fibo(n) :
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else :
#         return fibo(n-1) + fibo(n-2)

# bintang(10)
# for i in range(10) :
#     print(fibo(i))

# xList= [bintang(10), 'apel', 'pisang']

# #print(xList[:])

# xList.remove(bintang(10))

# print(xList[:])

# def check_nama(nama, alphabet) :
#     print(alphabet.lower() in nama.lower())


# check_nama("Faiz", "o")

# a = (['faiz', 'syam'], 5)

# a[0][0] = 'ais'

# print (a)

# s ={1, 1, 2, 3, 3, 5, 5}

# print(s)
# s.remove(1)
# print(s)
# s.add(5)
# print(s)

#list comprehension
# def enam():
#     return 6

# def kalidua(x = 3) :
#     return x*2

# list_num = [1,2,3,4,5, kalidua()]
# list_num = [kalidua(item) for item in list_num]

# print(list_num )

# x = lambda a,b: a+b

# listNum = [1,2,3,4,5]
# listNum2 = [5,4,3,2,1]

# print(x(5,10))

# # print(listNum)

# def tambah(a) :
#     return a+2

# kali = lambda a : a*2
# number1 = [1,2,3]
# number2 = [2,3,4]

# def duplicateMAP(function,iteration):
#     newList = []
#     for item in iteration :
#         newList.append(function(item))
#     return newList


# print(duplicateMAP(kali,number1))

# list_nama  = ['uga','faiz', 'mantap']

# test = duplicateMAP(list, list_nama)

# print(list(test))


# def duplicateFilter(function, list_apapun) :
#     newlist = []
#     for item in list_apapun :
#         if function(item):
#             newlist.append(item)
#     return newlist

# tahun = [1990, 1998, 2000, 2010, 2015, 2018]
# test = duplicateFilter(lambda tahun: tahun < 2000, tahun)
# print(list(test))

# d = { 'a' : 'A', 'b' : 'B', 'c' : 'C' }

# list1 = list(d)
# list2 = list(d.values())

# print(list1)
# print(list2)

# print(d[list1[1]])
# print(list(d.values())[1])


# newD = dict(zip(list1, list2))

# print(newD)


Decision = {'testing' : ['a','b', ['c', ['d', { 'Ada apa' : ['e', [ 'HALO' ]]}]]]}

# print(Decision['testing'][2][1][1]['Ada apa'][1][0])

# def test(list1, a, s) :
#     list1.append(4)
#     a = 5
#     s = 'kamu'

# a = 1
# s = 'aku'
# list2 = [1,2,3]
# test(list2, a, s)

# print(a)
# print(s)
# print(list2)

# c = { 1: 2, 3:4}

# for k in c.values() :
#     print(k)

# import math

def mean(list) :
    return sum(list)/len(list)

def median(list2) :
    list3 = list(list2.sort())
    if len(list3) % 2 == 0 :
        return (list3[len(list3)//2 - 1] + list3[len(list3)//2])/2
    else :
        return list3[len(list3//2)]

def mode(list) :
    ind = set(list)
    counter = {}
    modus = []
    for i in ind :
        z = 0
        for j in list :
            if i==j :
                z += 1
        counter[i]=z
    max_count= max(counter.values())
    for k in counter:
        if counter[k] == max_count :
            modus.append(k)
    if len(modus) == len(ind) :
        modus = []
    return modus

def variance(list) :
    z = 0
    meanVal = mean(list)
    for i in list :
        z+= (i - meanVal) ** 2
    return z/(len(list)-1)

def stdev(list) :
    return variance(list) ** 0.5

def sample_statistic(list, type = 'mean'):
    if type == 'mean':
        return mean(list)
    elif type == 'stdev' :
        return stdev(list)
    elif type == 'median' :
        return median(list)
    elif type == 'mode' :
        return mode(list)
    elif type == 'variance' :
        return variance(list)
    else :
        return 'Input invalid'

a = [4,5,2,1,5,1,6,6,5,3,6,2,4,4,6,1,6,2,4,1,2,4,5,7,8,9,7,3,2,2,1,5,1]
b = [1,2,3,4,5]

print(sample_statistic(a,'mean'))
print(sample_statistic(a,'median'))
print(sample_statistic(a,'mode'))
print(sample_statistic(a,'variance'))
print(sample_statistic(a,'stdev'))