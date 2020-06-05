
#def almost_equal():
#    print('첫번째 실수를 입력해주세요', end='')
#    first=float(input())
#    print('두번째 실수를 입력해주세요', end='')
#    second = float(input())
#    print(abs(first-second)<0.0001)
#almost_equal()

def almost_equal(x,y):
     print(abs(x-y)<0.0001)

almost_equal(1,0.999)
