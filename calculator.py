character=input()
a=int(input())
b=int(input())
optr_1="+"
optr_2="-"
optr_3="*"
optr_4="/"
optr_5="%"
if (character == optr_1):
    print(a+b)
elif (character == optr_2):
    print(a-b)
elif (character == optr_3):
    print(a*b)
elif (character == optr_4):
    print(a/b)
else:
    print(a % b)