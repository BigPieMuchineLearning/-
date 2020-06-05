

def price():
    print("몇개의 상품을 구매할 것인가요?")
    num=int(input())
    if (num<10):
        price=100
    elif (num<30):
        price = 95
    elif (num < 100):
        price = 90
    elif (num >=100):
        price = 85

    total=num*price

    print("총가격은",total,"입니다.")

price()