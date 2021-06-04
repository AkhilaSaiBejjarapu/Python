a = input()

num1 = int(a) > 25

digit1 = a[0]
digit2 = a[1]

digit1 = int(digit1)
digit2 = int(digit2)

comp = digit1 > digit2

result = num1 and comp
print(result)
