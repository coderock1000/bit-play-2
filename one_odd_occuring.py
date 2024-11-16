def odd_occuring(arr):
    """
    Finds the number that occurs an odd number of times in the array.
    Assumes that exactly one number occurs an odd number of times.
    """
    res = 0
    for element in arr:
        res ^= element  
    return res


arr = []

n = int(input('Enter array size: '))
print('Enter the array elements:')

for _ in range(n):
    num = int(input('Enter number: '))
    arr.append(num)

print('\nOdd occurring number is:', odd_occuring(arr))
