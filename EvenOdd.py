#prompt for person to input a number
num=int(input("Enter a number: "))
#if...else loop will help in setting a condition where if the number input is divisible by 2 it will display that the number is even else odd''
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

