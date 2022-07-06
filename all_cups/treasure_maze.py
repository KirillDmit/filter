from enum import Enum


class Ceil(Enum):
    EMPTY = 0
    WALL = 1


class Action:
    def __init__(self):
        self.type = type


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Seeker:
    def __init__(self, position: Position, has_coin: bool):
        self.position = position
        self.has_coin = has_coin


class Coin:
    def __init__(self, position: Position, value: int):
        self.position = position
        self.value = value


class ActionType(Enum):
    MOVE = 0
    TAKE_COIN = 1
    CRASH_WALL = 2


def get_action(maze, coins, seeker: Seeker, opponent_seeker: Seeker):
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


print(Ceil.WALL.value)
