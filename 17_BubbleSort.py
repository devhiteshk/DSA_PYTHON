def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
    return arr

arr = [10,2,4,6,2,1,8,7]

print(bubbleSort(arr))