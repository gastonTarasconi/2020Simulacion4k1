
class Uniform:

    @staticmethod
    def get_expected_frequencies(data, intervals):
        n_intervals = len(intervals)
        expected_frequency = len(data) / n_intervals
        expected_frequencies = []
        for i in range(n_intervals):
            expected_frequencies.append(expected_frequency)
        return expected_frequencies
