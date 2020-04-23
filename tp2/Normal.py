import math


class Normal:

    def __init__(self, desviacion, media):
        self.desviacion = desviacion
        self.media = media

    # Box Muller
    def generate(self, rnd1, rnd2):
        return self.get_n1(rnd1), self.get_n2(rnd2)

    def get_n1(self, rnd):
        return (math.sqrt(-2 * math.log(rnd)) * math.cos(2 * math.pi)) * self.desviacion + self.media

    def get_n2(self, rnd):
        return (math.sqrt(-2 * math.log(rnd)) * math.sin(2 * math.pi)) * self.desviacion + self.media
