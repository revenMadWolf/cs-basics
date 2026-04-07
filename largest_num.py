numbers = []
while True:
    input_number = input("Enter Number: ")
    if input_number == "":
        break
    numbers.append(int(input_number))

numbers.sort(reverse=True)
print("Largest number: ",numbers[0])