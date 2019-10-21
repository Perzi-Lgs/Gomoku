#!/usr/bin/python3  

# 점수를 세는데에는 뭐가 필요한가
# score 라는 점수가 필요하다?
# 판을 두는 알고리즘도 필요로 한다 그런데 굳이 여기에서 해야하나?
# 점수가 적힌 리스트를 반환해 다음 점수판을 만드는데에 시간을 아낄수 있다
# 그럼 이곳에는 크게 3가지 함수로 구성이 되어야 한다
# 1. initialisation 의 역할을 가지는 함수, 즉 처음 보드판의 점수를 제주고 그 보드판을 리턴하는 함수가 필여하다
# 2. 타겟 판과 그의 맞는 coordinate를 입력 받을시 그 값을 업데이트해서 판을 리턴하는 함수를 만든다
# 3. 굳이 만들자면 스코어를 리턴하는 함수를 구우우욷이 만들자면 만든다 (다음 알고리즘에 유용할수도 있으니 만들어놔라 걍)
# 4. 공격면이 조금 약하다는 약점을 보안하기 위해 조금 더 적극적인 공격 알고리즘을 짤 필요가 있다

import copy
import time

def change_value(table, x, y, type):
    try:
        if (not (table[y][x] == 'A') and not(table[y][x] == 'B')):
            if (x >= 0 and y >= 0) and (x <= 19 and y <= 19):
                table[y][x] += type
                return (True)
    except IndexError:
        pass
    return (False)

def update_score(table, x, y, type):
    change_value(table, x + 1, y, type)
    change_value(table, x - 1, y, type)
    change_value(table, x, y + 1, type)
    change_value(table, x, y - 1, type)
    change_value(table, x + 1, y - 1, type)
    change_value(table, x - 1, y + 1, type)
    change_value(table, x - 1, y - 1, type)
    change_value(table, x + 1, y + 1, type)
    return (table)

def check_his_diagonal(table, type):
    if (type == 1):
        target = 'A'
    else:
        target = 'B'
    for y in range(2, 17):
        for x in range(2, 17):
            if (table[y][x] == target and table[y][x-1] == target and table[y][x+1] == target):
                change_value(table, x+2, y, type * 50)
                change_value(table, x-2, y, type * 50)
            if (table[y][x] == target and table[y+1][x] == target and table[y-1][x] == target):
                change_value(table, x, y+2, type * 50)
                change_value(table, x, y-2, type * 50)
            if (table[y][x] == target and table[y+1][x+1] == target and table[y-1][x-1] == target):
                change_value(table, x+2, y+2, type * 50)
                change_value(table, x-2, y-2, type * 50)
            if (table[y][x] == target and table[y+1][x-1] == target and table[y-1][x+1] == target):
                change_value(table, x+2, y-2, type * 50)
                change_value(table, x-2, y+2, type * 50)

def check_my_diagonal(table, type):
    # 대각선을 체크할시에 방어는 잘 되지만 공격성은 잃게된다는 문제점이 발견되어
    # 그것을 보안하기 위해 4줄일경우의 룰을 만든다
    if (type == 1):
        target = 'B'
    else:
        target = 'A'
    for y in range(2, 17):
        for x in range(2, 17):
            if (table[y][x] == target and table[y][x-1] == target and table[y][x+1] == target):
                change_value(table, x+2, y, type * 50)
                change_value(table, x-2, y, type * 50)
            if (table[y][x] == target and table[y+1][x] == target and table[y-1][x] == target):
                change_value(table, x, y+2, type * 50)
                change_value(table, x, y-2, type * 50)
            if (table[y][x] == target and table[y+1][x+1] == target and table[y-1][x-1] == target):
                change_value(table, x+2, y+2, type * 50)
                change_value(table, x-2, y-2, type * 50)
            if (table[y][x] == target and table[y+1][x-1] == target and table[y-1][x+1] == target):
                change_value(table, x+2, y-2, type * 50)
                change_value(table, x-2, y+2, type * 50)

def generate_table(dup_list, x, y):
    if (dup_list[y][x] == 'A'):
        type = 1
    elif (dup_list[y][x] == 'B'):
        type = -1
    update_score(dup_list, x, y, type)
    return (dup_list)

# first function that allows us to make a scoreboard

def init_scoreboard(table):
    dup_list = copy.deepcopy(table)
    for y in range(19):
        for x in range(19):
            if (dup_list[y][x] == 'A' or dup_list[y][x] == 'B'):
                dup_list = generate_table(dup_list, x, y)
    check_his_diagonal(dup_list, 1)
    check_his_diagonal(dup_list, -1)
    return (dup_list)

# second function that takes the board, coordinate, type and returns an updated scoreboard

def update_scoreboard(target_table, coordinate, type):
    table = copy.deepcopy(target_table)
    if (type == 1):
        target = 'A'
    else:
        target = 'B'
    if (table[coordinate[1]][coordinate[0]] != 'A' and table[coordinate[1]][coordinate[0]] != 'B'):
        table[coordinate[1]][coordinate[0]] = target
    else:
        return (table)
    table = generate_table(table, coordinate[0], coordinate[1])
    return (table)

# third function that takes a scored table and it s coordinate, and returns the score

def get_score(table, coordinate):
    if (table[coordinate[1]][coordinate[0]] == 'A' or table[coordinate[1]][coordinate[0]] == 'B'):
        return (0)
    return (table[coordinate[1]][coordinate[0]])

def static_evaluation(table, position, type, score=False): # table is a 19 * 19 list and position is a tuple of x, y and returns the static point
    # if score is True, returns only the score of the table
    # else, generate a table that contains 
    if (type == 1):
        target = 'A'
    else:
        target = 'B'
    if (table[position[0]][position[1]] == 'A' or
        table[position[0]][position[1]] == 'B'):
        return (table, 0)
    dup_list = copy.deepcopy(table)
    for y in range(19):
        for x in range(19):
            if (dup_list[y][x] == 'A' or dup_list[y][x] == 'B'):
                dup_list = generate_table(dup_list, x, y)
    check_his_diagonal(dup_list, 1)
    check_his_diagonal(dup_list, -1)
    score = dup_list[position[0]][position[1]]
    dup_list[position[0]][position[1]] = target
    return (dup_list, score)