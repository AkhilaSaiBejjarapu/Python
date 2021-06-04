num1=int(input())
num2=int(input())
cond1=((num1==6)or(num2==6))
cond2=((num1+num2)==6)
cond3=((num1-num2)==6)or((num2-num1)==6)
final_cond=cond2 or cond3
if cond1 or final_cond:
    print("Lucky")
else:
    print("Not Lucky")