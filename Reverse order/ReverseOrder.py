num = int(input("Enter the number : "))
revNum = 0
while num > 0:
    digit = num % 10
    revNum = revNum * 10 + digit
    num //= 10
print("Reversed Number: ", revNum)