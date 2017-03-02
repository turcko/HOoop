"""
Define el similador del Radar
"""


class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector


    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        #
        # una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        #
        # una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        # tiempo_final) #una lista de senales emitidas x los blancos
        #
        #      boolBlanco = self.detector.detectar(una_senal, una_senal_reflejada)  #lista booleana de blancos
 	#return boolBlanco
        pass

    #TODO agregar el metodo plotear_senal
