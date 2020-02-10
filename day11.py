
def remove_outliner(list1) :

    list2 = sorted(list1)
    mid = len(list2)//2
    data1 = list2[:mid]
    data2 = list2[-mid:]
    q1 = data1[len(data1)//2] if len(data1) % 2 != 0 else (data1[len(data1)//2] + data1[len(data1)//2-1])/2
    q3 = data2[len(data2)//2] if len(data2) % 2 != 0 else (data2[len(data2)//2] + data2[len(data2)//2-1])/2

    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    list2 = list(filter(lambda a: a>=lower and a<=upper, list2))
    return list2


data =  [71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69]

print(remove_outliner(data))


def countVowel(kalimat) :
    return len(list(filter(lambda s: s.lower() in ['a', 'i', 'u', 'e', 'o'], kalimat)))

print(countVowel('budi pergI kE pasAr'))


def given(fList) :
    newlist = []
    for i in fList :
        for j in i:
            newlist.append(int(j))
    return sorted(newlist)

print(given([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))
print(given([[3,4,2,1] , [1,2,3] , [5,4,3,1]]))


def countWords(kalimat) :
    newDict = {}
    newlist = kalimat.lower().split(' ')
    for i in newlist :
        if(i in newDict):
            newDict[i] += 1
        else :
            newDict[i] = 1
    for i,j in newDict.items() :
        print(i.capitalize() + ' ' + str(j))

countWords('Jangan jangan kau menolak cintaku')