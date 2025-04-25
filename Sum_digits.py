#define function sum digits
def sum_digits(num):
    return sum(int(digit) for digit in str(num))

# prompt to input a number
num=int(input("Enter a number: "))
result=sum_digits(num)

# displays sum of digits
print("sum of digits:", result)