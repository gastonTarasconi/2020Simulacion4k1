import math
from collections import Counter

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

        if _type != 3:
            for i in range(intervals):
                self.freq_observ[i] = 0

                k = truncate(lim_inf + interval_size * i, self.accuracy)
                k_prox = truncate(k + interval_size, self.accuracy)
                if _type != 3:
                    self.labels.append((k, k_prox))
                else:
                    self.labels.append((i, i))

            for i in self.data:
                k = int((i - lim_inf) // interval_size)

                if k == intervals:
                    self.freq_observ[k-1] += 1
                else:
                    self.freq_observ[k] += 1
        else:
            self.freq_observ = Counter(self.data)
            self.freq_observ.most_common()
            self.freq_observ = sorted(self.freq_observ.items())
            for i in self.freq_observ:
                self.labels.append((i, i))

        self.freq_esperadas = self.get_frecuencia_esperada(_type, self.labels)

        # self.agrupar_freq_esperadas()

        for i in self.freq_observ:
            if _type != 3:
                freq_esp = self.freq_esperadas[i]
                freq_obs = self.freq_observ[i]
            else:
                freq_esp = self.freq_esperadas[int(i[0])]
                freq_obs = self.freq_observ[int(i[0])][1]
            if freq_esp == 0:
                freq_esp = 1

            chi_2 = truncate(
                (pow(freq_obs - freq_esp, 2)) / freq_esp,
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

    def agrupar_freq_esperadas(self):

        freq_esperadas = []
        freq_observadas = []
        labels = []



        tamano = len(self.freq_esperadas)
        for i in range(len(self.freq_esperadas)):
            temp_esp = 0
            temp_obs = 0
            temp_lab = []

            if self.freq_esperadas[i] < 5:
                temp_index = i + 1

                if temp_index < tamano:
                    temp_esp = self.freq_esperadas[i] + self.freq_esperadas[temp_index]
                    temp_obs = self.freq_observ[i] + self.freq_observ[temp_index]
                    temp_lab = [self.labels[i][0], self.labels[temp_index][1]]

                    while temp_esp < 5:
                        if temp_index < tamano -1:
                            temp_index += 1
                            temp_esp += self.freq_esperadas[temp_index]
                            temp_obs += self.freq_observ[temp_index]
                            temp_lab = [temp_lab[0], self.labels[temp_index][1]]
                        else:
                            temp_esp += self.freq_esperadas[i-1]
                            temp_obs += self.freq_observ[i-1]
                            temp_lab = [self.labels[i-1][0], temp_lab[1]]

                    freq_esperadas.append(temp_esp)
                    freq_observadas.append(temp_obs)
                    labels.append(temp_lab)

                    i = temp_index + 1
            else:
                freq_esperadas.append(self.freq_esperadas[i])
                freq_observadas.append(self.freq_observ[i])
                labels.append(self.labels[i])
                # elif i+1 == tamano:
                #     # sumar al anterior
                #     break
        print(self.freq_esperadas)
        print(freq_esperadas)
        print()
        print(self.freq_observ)
        print(freq_observadas)
        print()
        print(self.labels)
        print(labels)
