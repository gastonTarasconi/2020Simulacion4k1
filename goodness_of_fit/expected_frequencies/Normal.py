import math
from utils.truncate import truncate


class Normal:

    @classmethod
    def get_media(cls, data):
        n_data = len(data)
        ac = 0
        media = 0
        for i in range(n_data):
            ac += float(data[i])
            media = ac / n_data
        return media

    @classmethod
    def get_standard_deviation(cls, data, media):
        ac = 0
        n_data = len(data)
        for i in range(n_data):
            ac += (float(data[i]) - media) ** 2
        standard_deviation = math.sqrt(ac / (n_data - 1))
        return standard_deviation

    @classmethod
    def get_expected_frequencies(cls, data, intervals):
        n_data = len(data)
        expected_frequencies = []
        media = cls.get_media(data)
        standard_deviation = cls.get_standard_deviation(data, media)
        for i in range(0, len(intervals)):
            class_mark = truncate(((intervals[i][0] + intervals[i][1]) / 2), 1)
            probability = ((math.exp(-0.5 * ((class_mark-media) / standard_deviation)**2)) /
                           (standard_deviation*math.sqrt(2*math.pi))) * (intervals[i][1]
                                                                         - intervals[i][0])
            expected_frequency = n_data * probability
            expected_frequencies.append(expected_frequency)
        return expected_frequencies
