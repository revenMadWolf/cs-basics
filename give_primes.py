range_of_primes = int(input("Enter last number (positive): "))

if range_of_primes < 2:
    print("Invalid Input!")

for i in range(2,range_of_primes+1):
    for x in range(2,i):
        if i % x == 0:
            break
    else:
        print(i)