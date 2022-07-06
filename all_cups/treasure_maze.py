from enum import Enum


class Ceil(Enum):
    EMPTY = 0
    WALL = 1


class Action:
    pass


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Seeker:
    def __init__(self, position: Position, has_coin: bool):
        self.position = position
        self.has_coin = has_coin


class ActionType(Enum):
    MOVE = 0
    TAKE_COIN = 1
    CRASH_WALL = 2


def get_action(maze, coins, seeker: Seeker, opponent_seeker: Seeker):
    action = Action()
    action.position = Position(seeker.position.x + 1, seeker.position.y)
    action.type = ActionType.MOVE
    return action


print(Ceil.WALL.value)
