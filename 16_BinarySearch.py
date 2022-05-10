# works only when data is sorted

arr = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(arr, value):
    n = len(arr)-1
    low = 0
    high = n
    mid = (low+high)//2
    
    while low <= high:
        if arr[mid] == value:
            return arr[mid], "value found"

        elif value < arr[mid]:
            high = mid - 1

        elif value > arr[mid]:
            low = mid + 1

        mid = (low+high)//2

    return "Not Found"

print(binarySearch(arr, 9))
print(binarySearch(arr, 8))
print(binarySearch(arr, 7))
print(binarySearch(arr, 6))
print(binarySearch(arr, 5))
print(binarySearch(arr, 4))
print(binarySearch(arr, 3))
print(binarySearch(arr, 2))
print(binarySearch(arr, 1))
print(binarySearch(arr, -1))

