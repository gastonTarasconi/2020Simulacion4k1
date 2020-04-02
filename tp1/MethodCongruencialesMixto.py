from utils.tools import truncate


class MethodCongrualesMixto:
    xo = 0

    def __init__(self, root_number, k, g, c, accuracy):
        self.set_xo(int(root_number))
        self.k = int(k)
        self.g = int(g)
        self.c = int(c)
        self.a = 1 + (4 * int(k))
        self.m = pow(2, int(g))
        self.ACCURACY = accuracy

    def get_random(self):
        x1 = ((self.a * self.xo) + self.c) % self.m
        self.set_xo(x1)
        return truncate((x1 / (self.m - 1)), self.ACCURACY)

    @classmethod
    def set_xo(cls, xo):
        cls.xo = int(xo)
