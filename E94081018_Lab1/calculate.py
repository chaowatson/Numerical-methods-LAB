print("Enter first integer:", end='')
first = input()
print("Enter second integer:", end='')
second = input()
quo = int(first) // int(second)
rem = int(first) % int(second)
print(f"Quotient: {quo}, Remainder: {rem}")