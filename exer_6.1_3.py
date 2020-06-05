def length(year, month):
    year_4 = year % 4
    year_100 = year % 100
    year_400 = year % 400

    month_l=month%2

    if (month_l==0):
        if (year_4 == 0):
            if (year_400 == 0):
                print("이 달은 29입니다.")
            elif (year_100 == 0):
                print("이 달은 28입니다.")
            else:
                print("이 달은 29입니다.")
    else:
        print("이 달은 31일입니다.")


length(2000,2)