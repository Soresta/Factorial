# Factorial
# Bir sayının faktöriyelini hesaplayan program.
# Program to calculate factorial of a number.

num = int(input("Enter a number: "))
i = 1

for j in range(num - 1):
    num = num * i
    i += 1
    j += 1

print(num)
