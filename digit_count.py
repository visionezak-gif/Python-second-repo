numbers = int(input("Enter the number: "))

if numbers == 0:
    count = 1
else:
    count = 0
    while numbers > 0:
        numbers //= 10
        count = count + 1

print(f"The number of digits is: {count}")
