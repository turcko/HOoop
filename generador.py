"""
Un generador de senal es el responsable de generar una senal portadora.

"""

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):
        import math
        import numpy as np

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo
        muestras = range(int(cantidad_muestras))

        #TODO agregar un ruido blanco a la senal
        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]

        noise = np.random.normal(0, 1, int(cantidad_muestras))
        ret = [sum(x) for x in zip(ret, noise.tolist())]      

        return ret