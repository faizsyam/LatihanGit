# def getSquare(a) :
#     hasil = 0
#     count = 0
#     while a>0 :
#         pangkat = (a % 10)**2 
#         hasil += pangkat * (10**count)
#         count += len(str(pangkat))
#         a = a//10 
#     return hasil

# print(getSquare(242))

def domainName(s) :
    a = s.split('.')
    if len(a) == 3:
        return a[1]
    elif len(a)== 2:
        return a[0].split('//')[1]

print(domainName("http://github.com/anugrahnrhmd/apapun"))
print(domainName("http://www.zombie-bites.com"))
print(domainName("http://facebook.com"))