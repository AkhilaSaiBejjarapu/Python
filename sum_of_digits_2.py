number=input()




if (len(number)==1):
    print(number)
elif (len(number)==2):
    first_digit=int(number[0])
    second_digit=int(number[1])
    print(first_digit+second_digit)
elif (len(number)==3):
    first_digit=int(number[0])
    second_digit=int(number[1])
    third_digit=int(number[2])
    print(first_digit+second_digit+third_digit)
else:
    first_digit=int(number[0])
    second_digit=int(number[1])
    third_digit=int(number[2])
    fourth_digit=int(number[3])
    print(first_digit+second_digit+third_digit+fourth_digit)
    