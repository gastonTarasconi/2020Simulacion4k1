from utils.tools import truncate


class TestChiCuadrado:

    def __init__(self, data, subintervals, accuracy):
        self.data = data
        self.subintervals = subintervals
        self.accuracy = accuracy
        self.freq_observ = {}
        self.freq_esperadas = {}
        self.chi_2 = []
        self.labels = []

    def do_test(self):
        percentil = 1 / self.subintervals
        freq_esperada = len(self.data) / self.subintervals

        for i in range(self.subintervals):
            key_interval = truncate(percentil * i, self.accuracy)
            label_interval = str(key_interval) + " - " + str(truncate(key_interval + percentil, self.accuracy))
            self.freq_esperadas[key_interval] = freq_esperada
            self.freq_observ[key_interval] = 0
            self.labels.append(label_interval)

        for i in self.data:
            self.freq_observ[truncate(percentil * int(i / percentil), self.accuracy)] += 1

        for i in self.freq_observ:
            self.chi_2.append(truncate(
                (pow(self.freq_observ[i] - self.freq_esperadas[i], 2)) / self.freq_esperadas[i],
                self.accuracy
            ))
