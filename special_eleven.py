number=int(input())
cond1=(number%11==0)
cond2=(number%11==1)
if cond1 or cond2:
    print("Special Eleven")
else:
    print("Normal Number")