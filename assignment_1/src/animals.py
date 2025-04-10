import random
import math

class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = 0.5
        self.status = 'alive'

    def move(self):
        direction = random.randint(1, 4)
        if direction == 1:
            self.y += self.distance  # north
        elif direction == 2:
            self.x += self.distance  # east
        elif direction == 3:
            self.y -= self.distance  # south
        else:
            self.x -= self.distance  # west

class Wolf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = 1.0

    def nearest_sheep(self, herd):
        alive_sheep = [sheep for sheep in herd if sheep.status == 'alive']
        if not alive_sheep:
            return None
        nearest = min(alive_sheep, key=lambda sheep: (sheep.x - self.x) ** 2 + (sheep.y - self.y) ** 2)
        return nearest

    def move_towards(self, sheep):
        if sheep:
            dist = math.sqrt((sheep.x - self.x) ** 2 +
                             (sheep.y - self.y) ** 2)  # distance vector
            if dist <= self.distance:  # wolf replaces sheep
                sheep.status = 'dead'
                self.x, self.y = sheep.x, sheep.y
                print(f"The wolf ate sheep at position ({sheep.x:.2f}, {sheep.y:.2f}).")
            else:  # wolf is moving towards nearest sheep
                dx = (sheep.x - self.x) / dist  # normalization x
                dy = (sheep.y - self.y) / dist
                self.x += dx * self.distance  # multiplication x by wolf steps
                self.y += dy * self.distance
                print(f"The wolf's position: ({self.x:.3f}, {self.y:.3f})")
