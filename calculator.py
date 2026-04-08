#two numbers no empty spaces
formula = input("Enter formula: ")
count = 0
for char in formula:
    if char.isdigit():
        count += 1
    else:
        break

first_number = int(formula[0:count])
last_number = int(formula[count+1:len(formula)])

if formula.__contains__("+"):
    print(first_number+last_number)
if formula.__contains__("-"):
    print(first_number-last_number)
if formula.__contains__("x"):
    print(first_number*last_number)
if formula.__contains__("/"):
    print(first_number/last_number)
