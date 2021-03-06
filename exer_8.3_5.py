import math

class Coordinate:
    """좌표를 나타내는 클래스"""

    #
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def distance(self, point_b):
        """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
        return math.sqrt(square(self.x - point_b.x) +
                         square(self.y - point_b.y))

point_1 = Coordinate(-1,2)
point_2 = Coordinate(y=3, x=2)
point_3=Coordinate()
point_4=Coordinate(10)


def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x

print(point_1.x, point_1.y)
print(point_2.x, point_2.y)
print(point_3.x, point_3.y)
print(point_4.x, point_4.y)
print(point_1.distance(point_2))