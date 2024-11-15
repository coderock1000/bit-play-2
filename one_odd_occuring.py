def odd_occuring(arr):
    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []

n = int(input('Enter array size : '))

while(n):
    num = int(input('enter number : '))
    arr.append(num)
    n -= 1

print('\n Odd occuring number is: ', odd_occuring(arr))