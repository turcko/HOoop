class Detector(object):

    def __init__(self):
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def detectar(self, senal_original, senal_reflejada):

        #TODO: Completar
        equalSignal = False
        different = [i for i, j in zip(senal_original, senal_reflejada) if i != j]
        if different:
            equalSignal = True
        return equalSignal
        #pass
