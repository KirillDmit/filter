from enum import Enum
from numpy import copy
from typing import List, Set


class Ceil(Enum):
    EMPTY = 0
    WALL = 1


class ActionType(Enum):
    MOVE = 0
    TAKE_COIN = 1
    CRASH_WALL = 2


class Action:
    def __init__(self):
        self.type = type


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Seeker:
    def __init__(self, position: Position, has_coin: bool):
        self.position = position
        self.has_coin = has_coin


class Coin:
    def __init__(self, position: Position):
        self.position = position


def take_coin_condition(coins, seeker):
    for coin in coins:
        if coin.position.__eq__(seeker.position):
            if not seeker.has_coin:
                return True
    return False


def go_to_coin_condition(coins, seeker):
    for coin in coins:
        if coin.position.__eq__(seeker.position):
            return False
    return True


def get_action(maze, coins, seeker, opponent_seeker):
    if take_coin_condition(coins, seeker):
        return "Take_coin"
    if go_to_coin_condition(coins, seeker):
        return "Go_to_coin"
    return "Go_to_base"


number_of_queries = int(input())
for i in range(number_of_queries):
    number_of_coins = int(input())
    coins = []
    for j in range(number_of_coins):
        x, y = [int(x) for x in input().split()]
        coins.append(Coin(Position(x, y)))
    x, y = [int(x) for x in input().split()]
    has_coin = bool(int(input()))
    seeker = Seeker(Position(x, y), has_coin)
    print(get_action(None, coins, seeker, None))


def get_action1(maze, coins, seeker: Seeker, opponent_seeker: Seeker):
    action = Action()
    action.type = ActionType.MOVE
    target_coin = coins[0]
    shift_x = target_coin.position.x - seeker.position.x
    shift_y = target_coin.position.y - seeker.position.y
    if shift_x != 0:
        if shift_x > 0:
            action.position = Position(seeker.position.x + 1, seeker.position.y)
        else:
            action.position = Position(seeker.position.x - 1, seeker.position.y)
    if shift_x == 0 and shift_y != 0:
        if shift_y > 0:
            action.position = Position(seeker.position.x, seeker.position.y + 1)
        else:
            action.position = Position(seeker.position.x, seeker.position.y - 1)
    if shift_x == 0 and shift_y == 0:
        action.position = Position(seeker.position.x, seeker.position.y)

    if maze[action.position.x][action.position.y] == Ceil.WALL:
        action.type = ActionType.CRASH_WALL
    return action


def bfs(maze):
    queue = []
    marked = set()
    shifts = [Position(0, 1), Position(0, -1), Position(1, 0), Position(-1, 0)]

    start_vertex = Position(0, 0)
    queue.append(start_vertex)
    marked.add(start_vertex)
    while len(queue) != 0:
        current_vertex = queue.pop(0)
        for shift in shifts:
            next_vertex = copy(current_vertex)
            next_vertex.x += shift.x
            next_vertex.y += shift.y
            in_maze = 0 <= next_vertex.x < 20 and 0 <= next_vertex.y < 20
            if in_maze and maze[next_vertex.x][next_vertex.y] == Ceil.EMPTY and next_vertex not in marked:
                marked.add(next_vertex)
                queue.append(next_vertex)

