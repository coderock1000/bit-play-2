def print2odd(arr, size):
    xorf2 = arr[0]
    x=0
    y=0
    set_bit = 0

    for i in range(1, size):
        xorf2 = xorf2 ^ arr[i]

    set_bit = xorf2 & ~(xorf2 - 1)

    for i in range(size):
        if(arr[i] & set_bit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print('the 2 odd elements are', x, '&', y)

arr = []

arr_size = int(input('enter size of the array : '))
for i in range(0, arr_size):
    z = int(input('enter element : '))
    arr.append(z)

print2odd(arr, arr_size)