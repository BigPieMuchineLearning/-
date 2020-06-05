import random

class Dice(sides):
                   #면의 수
    _show=_number[sides]           #나온 면

    def __init__(self, sides):
        self._sides=sides

    def number(self):
        self._sides=[]


random.randint(1,6)


dice_4 = Dice(4)      # 사면체 주사위 생성
print('사면체 주사위 테스트 ----')
print('처음 나온 면:', dice_4.top())
print('다시 굴리기:', dice_4.roll())
print('다시 굴리기:', dice_4.roll())

dice_100 = Dice(100)  # 백면체 주사위 생성
print('백면체 주사위 테스트 ----')
print('처음 나온 면:', dice_100.top())
print('다시 굴리기:', dice_100.roll())
print('다시 굴리기:', dice_100.roll())