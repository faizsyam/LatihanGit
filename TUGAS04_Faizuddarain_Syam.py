# # nomor 1

# def duplicate_string(parameter) :
#     newstr = ''
#     for i in range(len(parameter)) :
#         for j in range(i+1) :
#             newstr += parameter[i]
#     print(newstr)

# duplicate_string("anugrah")
# duplicate_string("grizly")

# # # nomor 2

# def dupliacte_string_strip(parameter) :
#     newstr = ''
#     for i in range(len(parameter)) :
#         newstr += '-'
#         for j in range(i+1) :
#             if j == 0 :
#                 newstr += parameter[i].upper()
#             else :
#                 newstr += parameter[i].lower()
#     print(newstr)

# dupliacte_string_strip("anya")
# dupliacte_string_strip("anugrah")

# nomor 3
import time


def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 

    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 

def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2

        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 

def fungsi_sort_ascending(parameter) :
    for item1 in range(0, len(parameter) - 1) :
        for item2 in range(item1 + 1, len(parameter)) :
            if(parameter[item1] > parameter[item2]) :
                #swap
                t = parameter[item1]
                parameter[item1] = parameter[item2]
                parameter[item2] = t
    return parameter

import xlsxwriter
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()


arr = [12, 11, 13, 5, 6, 7, 14, 8, 16, 1, 9, 10, 2, 4, 3, 15]
rata1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
rata2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

for j in range (20) :
    arr2 = []

    for i in range(20):
        arr2 = arr2 + arr
        arr3 = arr2

        start = time.perf_counter_ns()
        fungsi_sort_ascending(arr3)
        hasil = time.perf_counter_ns() - start
        print(hasil)
        #worksheet.write_number(0,i,hasil)
        rata1[i] += hasil

        arr3 = arr2
        n = len(arr3) 

        start = time.perf_counter_ns()
        mergeSort(arr3,0,n-1) 
        hasil = time.perf_counter_ns() - start
        print(hasil)
        #worksheet.write_number(1,i,hasil)
        rata2[i] += hasil


for i in range(20) :
    worksheet.write_number(0,i,rata1[i]/20)
    worksheet.write_number(1,i,rata2[i]/20)

workbook.close()





