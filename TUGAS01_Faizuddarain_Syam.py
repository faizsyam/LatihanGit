#soal 1

n1 = int(input("Input: "))
n2 = n1//1000*10 + (n1%1000//100) + (n1%100//10*1000) + (n1%10*100)

print(f"Output: {n2}")

#soal 2
import math

radius = float(input("Input radius: "))
area = math.pi*radius**2
print(f"Output area: {area}")

#soal 3

n1 = int(input("Input 1: "))
n2 = int(input("Input 2: "))
n3 = n1%10*10 + n1//10*1000 + n2%10 + n2//10*100

print(f"Output: {n3}")

#soal 4

s1 = input("Input string: ")
c1 = input("Input character to remove: ")
s2 = s1.replace(c1,"")
# kalau huruf besarnya juga dihapus
# s2 = s2.replace(c1.upper(),"")  

print("Output: " + s2)

#soal 5

s1 = input("Input: ")
slist = s1.split(" ")
s2 = slist[1] + " " + slist[0]

print("Output: " + s2)