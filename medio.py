class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos #listas de blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
        listaDeBlancos = []
        for oBlanco in self.blancos:
            #lista de senales de cada uno de los bancos q tiene el medio
            listaDeBlancos.append(oBlanco.reflejar(una_senal, tiempo_inicial, tiempo_final)) 
        print(listaDeBlancos)
        return listaDeBlancos
        
