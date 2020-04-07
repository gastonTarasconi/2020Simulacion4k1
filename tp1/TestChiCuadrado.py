from utils.tools import truncate
import csv

class TestChiCuadrado:

    def __init__(self, data, n, s, accuracy):
        self.data = data
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

        # creo archivo si no existe, borro lo que ya estaba
        csv_filename = 'exports/data.csv'
        f = open(csv_filename, 'w+')
        f.close()

        for i in range(self.subintervals):
            key_interval = truncate(percentil * i, self.accuracy)
            label_interval = str(key_interval) + ' - ' + str(truncate(key_interval + percentil, self.accuracy))

            self.labels.append((key_interval, label_interval))

            self.freq_esperadas[key_interval] = freq_esperada
            self.freq_observ[key_interval] = 0

        write_csv = []
        for i in self.data:
            key = truncate(percentil * int(i[1] / percentil), self.accuracy)
            if int(key) == 1:
                self.freq_observ[truncate(1 - percentil, self.accuracy)] += 1
            else:
                self.freq_observ[key] += 1

            # guardo la serie en un csv cada 1000 registros
            write_csv.append(i[1])
            if len(write_csv) == 1000:
                with open(csv_filename, 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(map(lambda x: [x], write_csv))
                    write_csv.clear()

        # agrego los que faltaron, si no llego a 1000 registros
        if len(write_csv) > 0:
            with open(csv_filename, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(map(lambda x: [x], write_csv))
                write_csv.clear()

        ac = 0.0
        for i in self.freq_observ:
            chi_2 = truncate(
                (pow(self.freq_observ[i] - self.freq_esperadas[i], 2)) / self.freq_esperadas[i],
                self.accuracy
            )
            self.chi_2.append(chi_2)

            ac += chi_2
            self.chi_2_ac.append(ac)
