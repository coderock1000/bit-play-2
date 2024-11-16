def print2odd(arr, size):
    xorf2 = 0
    for i in range(size):
        xorf2 ^= arr[i]

    set_bit = xorf2 & ~(xorf2 - 1)

    x = 0
    y = 0
    for i in range(size):
        if arr[i] & set_bit:
            x ^= arr[i]
        else:
            y ^= arr[i]

    print('The two odd elements are', x, 'and', y)


arr = []

arr_size = int(input('Enter size of the array: '))
for i in range(arr_size):
    z = int(input(f'Enter element {i + 1}: '))
    arr.append(z)

if arr_size < 2:
    print("Array must contain at least 2 elements.")
else:
    print2odd(arr, arr_size)
