def is_array_sorted(arr):
    if len(arr) <= 1:
        return True
    return False if arr[0] > arr[1] else is_array_sorted(arr[1:])


print(is_array_sorted([1,2,3,4]))
print(is_array_sorted([1,2,4,4]))
print(is_array_sorted([1,2,5,4]))