#prompt person to input a number
num = int(input("Enter a number: "))
#I set factorial to start from one
factorial= 1
#factorials of negative numbers are not defined hence limit to positive numbers
if num < 0:
    print("The number cannot be negative")
else:
    #use of for loop to multiply from one to the number entered
    for i in range (1,num+1):
        factorial = factorial * i
#dispays the output
print(f"The factorial of {i} is {factorial}")