number=int(input())
cond1=(number%9==0)
conv_to_str=str(number)
digit1=int(conv_to_str[0])
digit2=int(conv_to_str[1])
cond2=(digit1 or digit2)
if cond1 and cond2:
    print("Lucky Number")
else:
    print("Unlucky Number")