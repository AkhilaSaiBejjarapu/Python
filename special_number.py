number=int(input())
conv_to_str=str(number)
first_digit=int(conv_to_str[0])
second_digit=int(conv_to_str[1])
cond1=(first_digit+second_digit ==7)
cond2=((first_digit==7)or(second_digit==7))
cond3=(number%7==0)
if ((cond1 and cond2)and cond3):
    print("Special Number")
else:
    print("Normal Number")