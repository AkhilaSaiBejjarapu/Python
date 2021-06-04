attendance_str=input()
medical_reason=input()

length=len(attendance_str)
attendance=attendance_str[0:(length-1)]
attendance=int(attendance)


if attendance >= 75:
    print("Allowed to write exam ")
elif attendance < 75 and medical_reason == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")