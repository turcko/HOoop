"""
Define el similador del Radar
"""
import matplotlib.pyplot as plt

class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector

    #TODO agregar el metodo plotear_senal
    def plotear_senal(self, senal_reflejada):
        #Implementar el metodo del radar plotear_senal() para visualizar las senales antes y despues de impactar en un blanco
        muestras = self.generador.get_muestras()
        plt.plot(muestras, self.generador.get_senal(), label='Senal Emitida por el radar', color='red')
        print (len(muestras), len(self.generador.get_senal()))
        print (len(muestras), len(senal_reflejada))
        plt.plot(muestras, senal_reflejada, label='Senal reflejada por el medio', color='blue')
        plt.title('Comparacion de senales', fontsize=16)
        plt.legend() 
        plt.ylabel('Senales',fontsize=14)
        plt.xlabel('Muestras', fontsize=14)
        plt.xlim(min(muestras)-0.5, max(muestras)+0.5)
        plt.show()

    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """        
        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        tiempo_final) 
        
        boolBlanco = self.detector.detectar(una_senal, una_senal_reflejada) 
        self.plotear_senal(una_senal_reflejada)
        return boolBlanco
        #pass

    
