# nomor 1

def check_name(nama, alphabet):
    print(alphabet.lower() in nama.lower())

check_name('Anugrah Nurhamid','A')
check_name('Arya Stark','A')

# nomor 2

def add_even(number):
    if number % 2 == 0 :
        print("genap")
    else :
        print("ganjil")

add_even(9)
add_even(256)
add_even(911)

# nomor 3
def max_number(num1, num2, num3, num4):
    print(max(num1, num2, num3, num4))

max_number(911,711,811,611)
max_number(1289,1981,1995,1375)
max_number(1890,1891,1888,1900)

# nomor 4

def string_filter(text):
    newstr = ''.join(i for i in text if i.isdigit())
    # newText = ""
    # for i in text :
    #     if i.isdigit() :
    #         newText += i
    print(newstr)

string_filter('9Anya11')
string_filter('11Pevita875')
string_filter('W34AREM4NU')

# nomor 5

import datetime

def check_plat(platnomor):
    d = datetime.datetime.today().day
    nomor = int(platnomor.split(' ')[1])
    if nomor % 2 == d % 2 :
        print(f"Kendaraan anda dengan plat nomor {platnomor} boleh lewat")
    else :
        print(f"Kendaraan anda dengan plat nomor {platnomor} tidak boleh lewat")

check_plat('D 4444 CBR')
check_plat('D 1576 ADT')
check_plat('D 5959 RF')

