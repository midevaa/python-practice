#define function sum digits
def sum_digits(num):
    #each int in the digit str(num) converts digits into string to get each number in the digit
    return sum(int(digit) for digit in str(num))
# prompt to input a number
num=int(input("Enter a number: "))
result=sum_digits(num)
# displays sum of digits
print("sum of digits:", result)