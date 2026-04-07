factorial_n = int(input("Enter needed factorial: "))
factorial = 1
for i in range(factorial_n):
    factorial *= i + 1
print(f"Factorial of {factorial_n}: ",factorial)