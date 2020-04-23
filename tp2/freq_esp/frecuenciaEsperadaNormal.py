import math
from utils.tools import truncate

# serie =[1.56,2.21,3.15,4.61,4.18,5.20,6.94,7.71,5.15,6.76,7.28,4.23,3.21,2.75,4.69,5.86,6.25,4.27,4.91,4.78,2.46,3.97,5.71,6.19,4.20,3.48,5.83,6.36,5.90,5.43]
# intervalos = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)]


class FreqEspNormal:

    def calcularMedia(self, serie):
        acumulador = 0
        for i in range(0,len(serie)):
            acumulador += float(serie[i])
            media = acumulador / len(serie)
        return media

    def calcularDevEstandar(self, serie):
        acumulador = 0
        media = self.calcularMedia(serie)
        for i in range(0,len(serie)):
            acumulador +=  (float(serie[i]) - media) ** 2
        desviacionEstandar = math.sqrt( acumulador / (len(serie) - 1) )
        return desviacionEstandar


    def get_frecuencia_esperada(self, serie,intervalos):
        listaFrecuenciaEsperadaNormal = []
        media = self.calcularMedia(serie)
        desviacionEstandar = self.calcularDevEstandar(serie)
        for i in range(0,len(intervalos)):
            marcaClase = truncate(((intervalos[i][0] + intervalos[i][1]) / 2),1)
            probabilidad=((math.exp(-0.5 * ((marcaClase-media)/ desviacionEstandar)**2))/ (desviacionEstandar*math.sqrt(2*math.pi)))* (intervalos[i][1] - intervalos[i][0])
            frecuenciaEsperadaNormal = len(serie) * probabilidad
            listaFrecuenciaEsperadaNormal.append(frecuenciaEsperadaNormal)
        return listaFrecuenciaEsperadaNormal

# print(frecuenciaEsperadaNormal(serie,intervalos))