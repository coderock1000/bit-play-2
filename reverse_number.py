def reverse_bits(num):
    reversed_binary = bin(num)[2:][::-1]
    return int(reversed_binary, 2)

number = int(input("Enter your original number: "))
reversed_number = reverse_bits(number)
print("Reversed Number: ",reversed_number)
