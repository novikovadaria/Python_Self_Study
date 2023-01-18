# -------------------------------------------------------------------------------------------
# ------------------------------- Дата класс ------------------------------------------------
# -------------------------------------------------------------------------------------------

"""
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

robot1 = Robot(1, 2)
robot2 = Robot(1, 2)

print(robot1 == robot2)
"""

from collections import namedtuple

Robot = namedtuple('Robot', ['x', 'y'])

robot1 = Robot(x=1, y=2)
robot2 = Robot(x=1, y=2)

print(robot1 == robot2)