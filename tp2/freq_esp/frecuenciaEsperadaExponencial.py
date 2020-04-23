import math
from utils.tools import truncate


class FreqEspExponencial:

    def calcularMedia(self, serie):
        acumulador = 0
        media = 0
        for i in range(0,len(serie)):
            acumulador += float(serie[i])
            media = acumulador / len(serie)
        return media


    def get_frecuencia_esperada(self, serie, intervalos):
        listaFrecuenciaEsperada = []
        lambdaa =  truncate((1 / self.calcularMedia(serie)), 9)
        for i in range(0,len(intervalos)):
            marcaClase = truncate(((intervalos[i][0] + intervalos[i][1]) / 2),1)
            # probEsperadaConMarcaClase = truncate(lambdaa * math.exp(-lambdaa*marcaClase) * (intervalos[i][1] - intervalos[i][0]),4)
            probEsperadaConMarcaClaseAcum = truncate((1-math.exp(-lambdaa*intervalos[i][1]))-(1-math.exp(-lambdaa*intervalos[i][0])),4)
            frecuenciaEsperada = truncate((len(serie) * probEsperadaConMarcaClaseAcum),4)
            listaFrecuenciaEsperada.append(frecuenciaEsperada)
        return listaFrecuenciaEsperada
       


# serie=[0.10,0.25,1.53,2.83,3.50,4.14,5.65,6.96,7.19,8.25,1.20,5.24,4.75,3.96,2.21,3.15,2.53,1.16,0.32,0.90,0.87,1.34,1.87,2.91,0.71,1.69,0.69,0.55,0.43,0.26]
# intervalos = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)]
# print(frecuenciaEsperadaExponencial(serie,intervalos))
