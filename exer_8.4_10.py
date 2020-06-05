import math

class Coordinate:
    """좌표를 나타내는 클래스"""

    #
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def distance(self, point_2):
        """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
        return math.sqrt(square(self.x - point_2.x) +
                         square(self.y - point_2.y))

class shape:

    def describe(self):
        print("이 도형은", self.sides, "개의 변을 갖고 있습니다.")

class Triangle(shape):
    """"삼각형"""
    sides = 3

    def circumference(self):
        return self.point_a.distance(point_b)+ point_b.distance(point_c)+ point_c.distance(point_a)

class Rectangle( shape, Coordinate):
    """사각형"""
    sides = 4

    def circumference(self):
        return self.point_a.distance(point_b) + point_b.distance(point_c) + point_c.distance(point_d)+point_d.distance(point_a)

shapes = [
    Triangle(Coordinate(0, 0), Coordinate(3, 0), Coordinate(3, 4)),
    Rectangle(Coordinate(2, 2), Coordinate(6, 2), Coordinate(6, 6), Coordinate(2, 6)),
]
for shape in shapes:
    shape.describe()
    print('둘레:', shape.circumference())
