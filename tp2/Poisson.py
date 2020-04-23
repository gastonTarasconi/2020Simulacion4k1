import math


class Poisson:

    def __init__(self, _lambda):
        self._lambda = _lambda

    # TODO: ver si este metodo esta bien planteado
    def generate(self, rnd):
        a = math.exp(-self._lambda)
        p = rnd
        x = 0
        while p >= a:
            p *= rnd
            x += 1
        return x

