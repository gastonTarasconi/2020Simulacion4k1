from utils.tools import truncate


class MethodCongrualesMixto:
    xo = 0

    def __init__(self, root_number, k, g, c, accuracy):
        self.set_xo(root_number)
        self.k = k
        self.g = g
        self.c = c
        self.ACCURACY = accuracy

    def get_random(self):
        a = 1 + (4 * self.k)
        m = pow(2, self.g)

        x1 = ((a * self.xo) + self.c) % m
        self.set_xo(x1)
        return truncate((x1 / (m - 1)), self.ACCURACY)

    @classmethod
    def set_xo(cls, xo):
        cls.xo = xo
