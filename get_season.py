month=int(input())

season_winter=(((month==1)or(month==11))or(month==12))
season_spring=((month==2)or(month==3))
season_summer=(((month==4)or(month==5))or(month==6))
season_rainy=((month==7)or(month==8))
if season_winter:
    print("winter")
elif season_spring:
    print("Spring")
elif season_summer:
    print("Summer")
elif season_rainy:
    print("Rainy")
else:
    print("Autumn")
