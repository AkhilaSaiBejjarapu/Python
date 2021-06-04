a=int(input())
b=int(input())
a_power=a**b
b_power=b**a
if a_power > b_power:
    print(a_power)
else:
    print(b_power)