import blanco


class Blancocluter(blanco.Blanco):
    """
    Define un Blancocluter a ser detectado por un radar

    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
#	blanco.Blanco.__init__(amplitud*10, tiempo_inicial, tiempo_final)
        self.amplitud = amplitud*10
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        #TODO ver como se encajan los timepos del blanco y del intervalo de tiempo
        # senal.insert(self.instante, senal[instante]+self.amplitud)
        # modificar la senal conlos parametros del blanco
        if(self.hayInterseccion(tiempo_inicial, tiempo_final)):
            # regla de 3 simple. Basada en tiempo de deteccion de blanco
            muestrasIntersectadas = (self.tiempo_final - self.tiempo_inicial).seconds * len(senal) / (tiempo_final - tiempo_inicial).seconds
            print("muestras intersec", muestrasIntersectadas)
            # otra regla de 3 simple :P . Basada en tiempo de muestreo
            tiempoDeUnaMuestra = float(float((tiempo_final - tiempo_inicial).seconds) / float(len(senal)))
            rangoIni = (self.tiempo_inicial - tiempo_inicial).seconds / tiempoDeUnaMuestra
            rangoDeMuestra = range(int(rangoIni), int(rangoIni+muestrasIntersectadas))
            # y multipllico x amplitud ese pedazo de senal y retorno 
        #Primera parte de la senal sin cambios
        ret1 = [senal[i] for i in range(0, int(rangoIni))]
        #Porcion de senal reflejada
        ret = [senal[i] + self.amplitud*10 for i in rangoDeMuestra]
        #Resto de senal sin cambios
        ret2 = [senal[i] for i in range(int(rangoIni+muestrasIntersectadas), len(senal))]
        #Senal Reflejada
        retFinal = ret1 + ret + ret2
        
        #Amplifico toda la senal
        # ret = [x*self.amplitud for x in senal]      
        return retFinal
	#pass
