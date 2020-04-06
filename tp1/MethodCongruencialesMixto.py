from utils.tools import truncate


class MethodCongrualesMixto:
    xo = 0

    #inicializador de la clase
    def __init__(self, root_number, k, g, c, accuracy):
        self.set_xo(int(root_number))
        self.k = int(k)
        self.g = int(g)
        self.c = int(c)
        self.a = 1 + (4 * int(k))
        self.m = pow(2, int(g))
        self.ACCURACY = accuracy

    def get_random(self):
        #calculo del x1 (ver formula del metodo congruencial mixto)
        x1 = ((self.a * self.xo) + self.c) % self.m
        #hacemos esto porque para el calculo del nuevo x1 se utiliza el ultimo x1
        self.set_xo(x1)
        return truncate((x1 / (self.m - 1)), self.ACCURACY)

    @classmethod
    def set_xo(cls, xo):
        cls.xo = int(xo)
