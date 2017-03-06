import radar
import medio
import blanco
import blancoCluter
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo genrador de senales
    oGenerador = generador.Generador(amplitud, fase, frecuencia)

    #TODO construir un detector
    oDetector = detector.Detector()

    #TODO construir un nuevo radar
    oRadar = radar.Radar(oGenerador, oDetector)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100

    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)

    tiempo_inicial_del_blanco_clutter = datetime.datetime(2016, 3, 5, 8)
    tiempo_final_del_blanco_clutter = datetime.datetime(2016, 3, 5, 9)

    #TODO contruir un nuevo blanco
    oBlanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco,tiempo_inicial_del_blanco, tiempo_final_del_blanco)
    oBlancoCluter = blancoCluter.Blancocluter(amplitud_de_frecuencia_del_blanco,tiempo_inicial_del_blanco_clutter, tiempo_final_del_blanco_clutter)
    lista_blancos = [oBlanco, oBlancoCluter]
    #TODO contruir un medio
    oMedio = medio.Medio(lista_blancos)

    #TODO utilizar un radar
    if oRadar.detectar(oMedio, tiempo_inicial, tiempo_final): 
        print ('DETECTO AL MENOS UN BLANCO')


if __name__ == "__main__":
    main()