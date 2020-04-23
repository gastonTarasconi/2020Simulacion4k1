import math


class Exponencial:

    def __init__(self, _lambda):
        self._lambda = _lambda

    def generate(self, rnd):
        return (-1 / self._lambda) * math.log(1 - rnd)

    def calculate_lambda(self, media):
        self._lambda = 1 / media
