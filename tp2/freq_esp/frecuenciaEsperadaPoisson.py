import math
from utils.tools import truncate


class FreqEspPoisson:
    '''
    ordena la serie de menor a mayor y completa
    los numero que falten entre el min y el max de la serie '''

    def ordenarYcompletarSerie(self, serieSinRepeticiones):
        serieOrdenadaCompleta = []
        for i in range(0, len(serieSinRepeticiones) + 1):
            serieOrdenadaCompleta.append(int(min(serieSinRepeticiones)) + i)
        return serieOrdenadaCompleta

    def calcularLambda(self, serie):
        acumulador = 0
        for i in range(0, len(serie)):
            acumulador += int(serie[i])
            lambdaa = round(acumulador / len(serie))
        return lambdaa

    def get_frecuencia_esperada(self, serieEntera, intervalo):
        # eliminamos las repeticiones de la serie, pero sigue desordenada e incompleta
        serieSinRepeticiones = set(serieEntera)
        # la serie final es la que ya esta ordenada, completa y sin repeticiones
        serieFinal = self.ordenarYcompletarSerie(serieSinRepeticiones)
        lambdaa = self.calcularLambda(serieEntera)
        listaFrecuenciaEsperadaPoisson = []
        for i in range(0, len(serieFinal)):
            probabilidad = truncate(
                (((lambdaa ** (serieFinal[i])) * math.exp(-lambdaa)) / math.factorial(serieFinal[i])), 4)
            frecuenciaEsperadaPoission = round(len(serieEntera) * probabilidad)
            listaFrecuenciaEsperadaPoisson.append(frecuenciaEsperadaPoission)
        return listaFrecuenciaEsperadaPoisson

# serie=[14,7,13,16,16,13,14,17,15,16,13,15,10,15,16,14,12,17,14,12,13,20,8,17,19,11,12,17,9,18,20,10,18,15,13,16,24,18,16,18,12,14,20,15,10,13,21,23,15,18]
# print(frecuenciaEsperadaPoission(serie))
