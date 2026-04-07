number = int(input("Enter number: "))
if number == 1 or number == 2:
    print("Not Prime")
    exit()
for i in range(2,number):
    if number % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")