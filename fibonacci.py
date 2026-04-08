amount_of_terms = int(input("Enter amount of terms required: "))

fibonacci_list = [1]
add_term = 0
for x in range(amount_of_terms - 1):
    fibonacci_list.append(fibonacci_list[-1] + add_term)
    add_term = fibonacci_list[-2]

print(fibonacci_list)


