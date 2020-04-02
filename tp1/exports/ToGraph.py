import matplotlib.pyplot as plt
import numpy as np


class ToGraph:

    @staticmethod
    def get_graph(intervalos, freq_observadas, freq_esperadas):
        x_indexes = np.arange(len(intervalos))
        bars_width = 0.25

        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_title('Prueba Chi Cudadrado')
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frecuencias')
        ax.set_xticks(ticks=x_indexes, minor=False)

        ax.set_xticklabels(labels=intervalos, fontdict=None, minor=False)
        ax.bar(x_indexes - bars_width, freq_observadas, label='Frecuencias Obtenidas',
               color='#3b5998', width=bars_width)
        ax.bar(x_indexes, freq_esperadas, label='Frecuencias Esperadas', color='#ffa500',
               width=bars_width)

        ax.legend(loc='upper right')

        return fig
