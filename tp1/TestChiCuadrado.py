from utils.tools import truncate


class TestChiCuadrado:

    def __init__(self, data, n, s, accuracy):
        self.data = data
        self.serie = []
        self.n = n
        self.subintervals = s
        self.accuracy = accuracy

        self.freq_observ = {}
        self.freq_esperadas = {}
        self.chi_2 = []
        self.chi_2_ac = []

        self.labels = []

    def do_test(self):
        percentil = 1 / self.subintervals
        freq_esperada = self.n / self.subintervals

        for i in range(self.subintervals):
            key_interval = truncate(percentil * i, self.accuracy)
            label_interval = str(key_interval) + ' - ' + str(truncate(key_interval + percentil, self.accuracy))

            self.labels.append((key_interval, label_interval))

            self.freq_esperadas[key_interval] = freq_esperada
            self.freq_observ[key_interval] = 0
            # self.chi_2[key_interval] = 0

        for i in self.data:
            key = truncate(percentil * int(i[1] / percentil), self.accuracy)
            if int(key) == 1:
                self.freq_observ[truncate(1 - percentil, self.accuracy)] += 1
            else:
                self.freq_observ[key] += 1
            self.serie.append(i[1])

        for i in self.freq_observ:
            self.chi_2.append(truncate(
                (pow(self.freq_observ[i] - self.freq_esperadas[i], 2)) / self.freq_esperadas[i],
                self.accuracy
            ))

        self.chi_2_ac.append(self.chi_2[0])
        for i in range(1, len(self.chi_2)):
            self.chi_2_ac.append(self.chi_2_ac[i - 1] + self.chi_2[i])
