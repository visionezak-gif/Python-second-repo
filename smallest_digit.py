number = int(input("Enter the number: "))
smallest_digit = 9

if number == 0:
    smallest_digit = 0
    
while number > 0:
    digit = number % 10
    
    if digit < smallest_digit:
        smallest_digit = digit
        
    number //= 10

print(f"The smallest digit is: {smallest_digit}")
