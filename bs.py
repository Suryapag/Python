arr = [1, 3, 5, 7, 9]
target = 7
if arr[-1]<target:
    arr.append(target)
low = 0
high = (len(arr)-1)
while low <= high:
    mid =(low + high) // 2
    if arr[mid]==target:
        re=mid
    elif arr[mid]<target:
        low = mid + 1
    elif arr[mid]>target:
        low = mid -1
