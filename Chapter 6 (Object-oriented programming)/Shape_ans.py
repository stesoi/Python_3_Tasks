import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    # p = q + r
    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

    # p += q
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # p = q - r
    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)

    # p -= q
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    # p = q * n
    def __mul__(self, n):
        return Point(x=self.x * n, y=self.y * n)

    # p *= n
    def __imul__(self, n):
        self.x *= n
        self.y *= n
        return self

    # p = q / n
    def __truediv__(self, n):
        return Point(x=self.x / n, y=self.y / n)

    # p /= n
    def __itruediv__(self, n):
        self.x /= n
        self.y /= n
        return self

    # p = q // n
    def __floordiv__(self, n):
        return Point(x=self.x // n, y=self.y // n)

    # p //= n
    def __ifloordiv__(self, n):
        self.x //= n
        self.y //= n
        return self

