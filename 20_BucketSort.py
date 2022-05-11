import math

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

    
def bucketSort(myList):
    numofbuckets = round(math.sqrt(len(myList)))
    maxValue = max(myList)
    arr = []

    for i in range(numofbuckets):
        arr.append([])

    for j in myList:
        index_b = math.ceil(j*numofbuckets/maxValue)
        arr[index_b - 1].append(j)
        
    for i in range(numofbuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numofbuckets):
        for j in range(len(arr[i])):
            myList[k] = arr[i][j]
            k += 1
    return myList