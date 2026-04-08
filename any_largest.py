#No sorting allowed
numbers = []
required_level = 2

while True:
    entered_num = input("Enter number: ")
    if entered_num =="":
        break
    numbers.append(int(entered_num))

numbers = list(set(numbers))
amount_highs = required_level - 1
amount_lows = len(numbers) - amount_highs

for i in numbers:
    lows = 0
    highs = 0
    for x in numbers:
        if i < x:
            highs += 1
        else:
            lows += 1
    if lows == amount_lows and highs == amount_highs:
        print(f"largest {required_level} number:",i)
        break