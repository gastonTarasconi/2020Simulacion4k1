
class Uniforme:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def generate(self, rnd):
        return self.a + rnd * (self.b - self.a)
