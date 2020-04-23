import math

from tp2.freq_esp.frecuenciaEsperadaExponencial import FreqEspExponencial
from tp2.freq_esp.frecuenciaEsperadaNormal import FreqEspNormal
from tp2.freq_esp.frecuenciaEsperadaPoisson import FreqEspPoisson
from tp2.freq_esp.frecuenciaEsperadaUniforme import FreqEspUniforme
from utils.tools import truncate


class TestChiCuadradoTp2:

    def __init__(self, data, accuracy):
        self.data = data
        self.accuracy = accuracy

        self.freq_observ = {}
        self.freq_esperadas = {}
        self.chi_2 = []
        self.chi_2_ac = []

        self.labels = []

    def do_test(self,  lim_inf, lim_sup, _type, intervals):

        interval_size = truncate((lim_sup - lim_inf) / intervals, self.accuracy)

        ac = 0.0


        for i in range(intervals):
            self.freq_observ[i] = 0

            k = truncate(lim_inf + interval_size * i, self.accuracy)
            k_prox = truncate(k + interval_size, self.accuracy)
            self.labels.append((k, k_prox))

        for i in self.data:
            k = int((i - lim_inf) // interval_size)

            if k == intervals:
                self.freq_observ[k-1] += 1
            else:
                self.freq_observ[k] += 1

        self.freq_esperadas = self.get_frecuencia_esperada(_type, self.labels)

        for i in self.freq_observ:
            chi_2 = truncate(
                (pow(self.freq_observ[i] - self.freq_esperadas[i], 2)) / self.freq_esperadas[i],
                self.accuracy
            )
            self.chi_2.append(chi_2)

            ac += chi_2
            self.chi_2_ac.append(ac)

    def get_frecuencia_esperada(self, _type, intervalos):
        types = {0: FreqEspUniforme,
                 1: FreqEspExponencial,
                 2: FreqEspNormal,
                 3: FreqEspPoisson}

        calculador = types[_type]()
        freq_esperadas = calculador.get_frecuencia_esperada(self.data, intervalos)

        return freq_esperadas
