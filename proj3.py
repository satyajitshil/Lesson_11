num = int(input("Enter a number:"))

# initialize sum

sum = 0
# while loop
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# if statement to display whether variable num is an armstrong number

if num == sum:
    print(num," is an Armstrong number") 
else:
    print(num," is unfortunately not an Armstrong number")
