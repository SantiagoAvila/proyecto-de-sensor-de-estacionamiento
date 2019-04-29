#### proyecto de penguin bootcamp
"""
ESTO DEBE CORRER EN LA RASPBERRY PARA QUE FUNCIONE

Objetivo:
        en el presente archivo se intentara realizar una pagina web para el monitoreo de vacancias 
        de estacionamientos funcional en un local determinado utilizando raspberry, que responda en
        una web basicadiseñada por nosotros
Diseño:
        se necesitaran  por lugar de estacionamiento  1 sensor de ultrasonido, que estaran conectados
        a una misma raspberry pi, que correra una pagina web para el contacto con el cliente sobre
        la disponibilidad del estacionamiento
Consideraciones:
        1)Para la consideracion de lugares vacios con los sensores de ultrasonidos, se tomara la 
        distancia de 1.95 metros como vacion (teniendo la altura real de piso a techo en el estacionamiento
        de 2.10 metros). Otra medida recibida se tomara como espacio ocupado actualmente
        2)El dato sera enviado por la raspberry pi a la web que se correra en la misma
        3)El cliente recibira una pantalla que le indicara por lugar el estatus de cada estacionamiento de
        bateria dentro del local como ( texto libre+ mas color verde) o (texto ocupado + color rojo)
"""
import RPi.GPIO as gpio
import time 
### para cada sensor tendremos que usar dos conexiones una de entrada y otra de salida
#para el sensor numero 1 definimos los pines en las rapberry
disparador= 11
receptor=13
##para el sensor numero 2 definimos los pines en la raspberry
disparador2=16
receptor2=18
GPIO.setmode(GPIO.BOARD)                #configuramos los pines del sensor en la raspebrry para  
GPIO.setup(disparador, GPIO.OUT)        # para ambos sensores
GPIO.setup(receptor,GPIO.IN)			#
GPIO.setup(disparador2,GPIO.OUT)		#
GPIO.setup(receptor2,GPIO.IN)			#
#### Definimos una funcion para la lectura del espacio de estacionamiento
GPIO.input(receptor)=lugar1
GPIO.input(receptor2)=lugar2
def det_espacio():
    while True:
        GPIO.output(disparador,True)
        GPIO.output(disparador2,True)
        time.sleep(0.00001)
        GPIO.output(disparador,False)
        GPIO.output(disparador2,False)
        while 0==GPIO.input(receptor):
            empieza1=time.time()
        while 1==GPIO.input(receptor):
           terminar1=time.time()
        while 0==GPIO.input(receptor2):
            empieza2=time.time()
        while 1==GPIO.input(receptor2):
            termina2=time.time()
        tiempo1=terminar1-empieza1
        tiempo2=termina2-empieza2
        distancia1=(tiempo1*34300)/2
        distancia2=(tiempo2*34300)/2
        if distancia1==195:                     ##para lugar1
            return "Libre espacio 1"            ##
        elif distancia!=195:                    ##
            return "Ocupado espacio 2"            ##
        elif distancia2==195:
            return "Libre espacio 2"
        elif distancia!=195:
            return "Ocupado espacio 2"



	

