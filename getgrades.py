marks=float(input())
if marks > 85:
    print("A")
elif (marks > 70 or marks <= 85):
    print("B")
elif (marks >= 60 or marks <= 70):
    print("C")
else:
    print("F")