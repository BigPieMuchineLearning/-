
def is_leap_year():
    print("년도를 입력하세요:")
    year=int(input())

    year_4=year%4
    year_100=year%100
    year_400=year%400

    if (year_4==0):
        if (year_400==0):
            print("윤년이다.")
        elif (year_100==0):
            print("윤년이 아니다.")
        else:
            print("윤년이다.")

is_leap_year()