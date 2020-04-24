from collections import Counter

from goodness_of_fit.expected_frequencies.ExpNeg import ExpNeg
from goodness_of_fit.expected_frequencies.Normal import Normal
from goodness_of_fit.expected_frequencies.Poisson import Poisson
from goodness_of_fit.expected_frequencies.Uniform import Uniform
from utils.truncate import truncate


class ChiSquareTest:
    def __init__(self, data, accuracy):
        self.data = data
        self.accuracy = accuracy

        self.labels = []
        self.observed_frequency = {}
        self.expected_frequency = {}
        self.chi_2 = []
        self.chi_2_ac = []

    def do_test_poisson(self):
        self.observed_frequency = Counter(self.data)
        self.observed_frequency.most_common()
        self.observed_frequency = sorted(self.observed_frequency.items())

        temp = {}
        for i in self.observed_frequency:
            temp[int(i[0])] = i[1]
            self.labels.append(int(i[0]))
        self.observed_frequency = temp

        calculator = Poisson()
        self.expected_frequency = calculator.get_frecuencia_esperada(self.data)

        self._do_formula()

    def do_test(self, intervals, _type):
        lim_sup = max(self.data)
        lim_inf = min(self.data)

        interval_size = truncate((lim_sup - lim_inf) / intervals, self.accuracy)

        for i in range(intervals):
            self.observed_frequency[i] = 0

            k = truncate(lim_inf + (interval_size * i), self.accuracy)
            k_next = truncate(k + interval_size, self.accuracy)
            self.labels.append((k, k_next))

        for i in self.data:
            k = int((i - lim_inf) // interval_size)

            if k == intervals:
                self.observed_frequency[k - 1] += 1
            else:
                self.observed_frequency[k] += 1

        if _type == 0:
            self.expected_frequency = Uniform.get_expected_frequencies(self.data, self.labels)
        elif _type == 1:
            self.expected_frequency = ExpNeg.get_expected_frequencies(self.data, self.labels)
        elif _type == 2:
            self.expected_frequency = Normal.get_expected_frequencies(self.data, self.labels)

        self._do_formula()

    def join_expected_frequencies(self):
        pass

    def join_expected_frequencies_poisson(self):
        pass

    def _do_formula(self):
        ac = 0.0
        for i in self.observed_frequency:
            freq_esp = self.expected_frequency[int(i)]
            freq_obs = self.observed_frequency[int(i)]
            chi_2 = truncate(
                (pow(freq_obs - freq_esp, 2)) / freq_esp,
                self.accuracy
            )
            self.chi_2.append(chi_2)

            ac += chi_2
            self.chi_2_ac.append(ac)
        print(ac)
