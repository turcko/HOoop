class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos #listas de blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
        if self.blancos:
            for oBlanco in self.blancos:
                una_senal = oBlanco.reflejar(una_senal, tiempo_inicial, tiempo_final)
        return una_senal
        