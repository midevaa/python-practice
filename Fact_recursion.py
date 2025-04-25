# I define a recursive function for factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
#You prompt the user to enter a number
num = int(input("Enter a number: "))
#I will limit the input numbers to only positive  numbers because negatives are undefined
if num < 0:
    print(num, "is not a factorial.")
else: #printing the factorial
    print(f"The factorial of {num} is {factorial(num)}")