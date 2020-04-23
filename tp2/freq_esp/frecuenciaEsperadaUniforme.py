
class FreqEspUniforme:

    def get_frecuencia_esperada(self, serie, intervalos):
        freq_esperada = []
        for i in range(len(intervalos)):
            freq_esperada.append(len(serie) / len(intervalos))
        return freq_esperada