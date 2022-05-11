# helper function
from re import L
from turtle import left


def merge(Myarr, l, m, r):
    n1 = m - l + 1    # l -> first index m -> middle index  r -> last index
    n2 = r - m 

    Left = [0]*(n1)
    Right = [0]*(n2)

    for i in range(0, n1):
        Left[i] = Myarr[l + i]

    for j in range(0, n2):
        Right[j] = Myarr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i<n1 and j<n2:
        if Left[i]<=Right[j]:
            Myarr[k] = Left[i]
            i += 1
        else:
            Myarr[k] = Right[j]
            j += 1
        k += 1

    while i< n1:
        Myarr[k] = Left[i]
        i+=1
        k+=1

    while j<n2:
        Myarr[k] = Right[j]
        j+=1
        k+=1


def mergeSort(Myarr, L_Index, R_index):
    if L_Index<R_index:
        m = (L_Index + (R_index-1))//2
        mergeSort(Myarr, L_Index , m)
        mergeSort(Myarr, m+1, R_index)
        merge(Myarr, L_Index, m , R_index)   
    return Myarr


arr = [10,34,2,1,0,3,55,6]
print(mergeSort(arr, 0 , 7 ))

