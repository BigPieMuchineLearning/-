# 이곳에 체스말 데이터 유형 정의하기
체스말1 = {'type' : '체스',
        'x': 'A', 'y': '8', 'color': 'black', 'role': '룩'}
체스말2 = {'type' : '체스',
        'x': 'E', 'y': '1', 'color': 'white', 'role': '킹'}

# 이곳에 바둑돌 데이터 유형 정의하기
바둑돌1 = {'type' : '바둑',
        'x': 8, 'y': 14, 'order': 83, 'color': '흑'}
바둑돌2 = {'type' : '바둑',
        'x': 12, 'y': 3, 'order': 84, 'color': '백'}

def print_piece(hores):
#이렇게 하는게 맞나?
    if hores['type'] == '체스':  # type() 함수 대신 인덱싱 연산 사용
        return print(hores['color'], hores['role'],'이', hores['x'],hores['y'],'위치에 놓여있어요.')


    elif hores['type'] == '바둑':  # type() 함수 대신 인덱싱 연산 사용
        return print('제',hores['order'],'수', hores['color'], '이','(', hores['x'],',', hores['y'],')','위치에 놓여있어요.')


    else:
        return None


print(print_piece(체스말1))
print(print_piece(바둑돌2))