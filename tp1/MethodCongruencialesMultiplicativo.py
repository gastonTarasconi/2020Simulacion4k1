from utils.tools import truncate


class MethodCongrualesMultiplicativo:
    xo = 0

    def __init__(self, root_number, accuracy):
        self.set_xo(root_number)
        self.k = int(input('Ingrese k: '))
        self.g = int(input('Ingrese g: '))
        self.ACCURACY = accuracy

    def get_random(self):
        a = 1 + (4 * self.k)
        m = pow(2, self.g)

        x1 = (a * self.xo) % m
        self.set_xo(x1)
        return truncate((x1 / (m - 1)), self.ACCURACY)

    @classmethod
    def set_xo(cls, xo):
        cls.xo = xo
