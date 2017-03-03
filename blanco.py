class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """
    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        
        # control en caso de que el intervalo de tiempo pase alguno de los limites
        if(self.hayInterseccion(tiempo_inicial, tiempo_final)):
            if(self.tiempo_inicial.hour <= tiempo_inicial.hour):
                self.tiempo_inicial = tiempo_inicial
            elif (self.tiempo_final.hour >= tiempo_final.hour):
                self.tiempo_final <= tiempo_final

            # controlo q este en el intervalo de la senal
            # regla de 3 simple. Basada en tiempo de deteccion de blanco
            muestrasIntersectadas = (self.tiempo_final - self.tiempo_inicial).seconds * len(senal) / (tiempo_final - tiempo_inicial).seconds
            print("Cantidad de muestras intersectadas: ", muestrasIntersectadas)
            # otra regla de 3 simple :P . Basada en tiempo de muestreo
            tiempoDeUnaMuestra = float(float((tiempo_final - tiempo_inicial).seconds) / float(len(senal)))
            rangoIni = (self.tiempo_inicial - tiempo_inicial).seconds / tiempoDeUnaMuestra
            rangoDeMuestra = range(int(rangoIni), int(rangoIni+muestrasIntersectadas))
            print("Rango de senal alterada: ", rangoDeMuestra)
            # senal * amplitud
            ret = [senal[i] * self.amplitud for i in rangoDeMuestra]
            return ret

    def hayInterseccion(self, tiempo_inicial, tiempo_final):
        ultimoInicio = max(self.tiempo_inicial.hour, tiempo_inicial.hour)
        primerFin = min(self.tiempo_final.hour, tiempo_final.hour)
        interseccion = (primerFin - ultimoInicio)
        if interseccion > 0:
            return True
        else: 
            return False

