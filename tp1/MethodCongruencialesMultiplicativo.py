from utils.tools import truncate


class MethodCongrualesMultiplicativo:
    xo = 0

    def __init__(self, root_number, k, g, accuracy):
        self.set_xo(root_number)
        self.k = int(k)
        self.g = int(g)
        self.a = 3 + (8 * self.k)
        self.m = pow(2, self.g)
        self.ACCURACY = accuracy

    def get_random(self):
        #formula del calculo de x1 del metodo congruencial multiplicativo
        x1 = (self.a * self.xo) % self.m
        self.set_xo(x1)
        return truncate((x1 / (self.m - 1)), self.ACCURACY)

    @classmethod
    def set_xo(cls, xo):
        cls.xo = int(xo)
