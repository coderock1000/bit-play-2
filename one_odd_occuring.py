def odd_occuring(arr):
    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []