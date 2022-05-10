arr = [1,2,3,4,5,6,7,8,9,10]

# works even if the data is not sorted.

def linerSearch(arr, value):
    for i in range(len(arr)):
        if value == arr[i]:
            return arr[i]
    return "Not Found"

print(linerSearch(arr, 11))
