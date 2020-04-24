import math
from utils.truncate import truncate


class ExpNeg:

    @classmethod
    def get_media(cls, data):
        ac = 0
        media = 0
        tam = len(data)
        for i in range(0, tam):
            ac += float(data[i])
            media = ac / tam
        return media

    @classmethod
    def get_expected_frequencies(cls, data, intervals):
        n_intervals = len(intervals)
        expected_frequencies = []
        _lambda = truncate((1 / cls.get_media(data)), 9)
        for i in range(n_intervals):
            class_ac = truncate(
                (1 - math.exp(-_lambda * intervals[i][1])) - (1 - math.exp(-_lambda * intervals[i][0])), 4)
            expected_frequency = truncate((len(data) * class_ac), 4)
            expected_frequencies.append(expected_frequency)
        return expected_frequencies
