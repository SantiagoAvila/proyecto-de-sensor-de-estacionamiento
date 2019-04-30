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
import RPi.GPIO as GPIO
import time 
### para cada sensor tendremos que usar dos conexiones una de entrada y otra de salida
#para el sensor numero 1 definimos los pines en las rapberry
disparador= 11
receptor=13
##para el sensor numero 2 definimos los pines en la raspberry
#disparador2=16
#receptor2=18
GPIO.setmode(GPIO.BOARD)                #configuramos los pines del sensor en la raspebrry para  
GPIO.setup(disparador, GPIO.OUT)        # para ambos sensores
GPIO.setup(receptor,GPIO.IN)			#
#GPIO.setup(disparador2,GPIO.OUT)		#
#GPIO.setup(receptor2,GPIO.IN)			#
#### Definimos una funcion para la lectura del espacio de estacionamiento
def detec_espacio():
 
   GPIO.output(disparador, False) #apagamos el pin Trig
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(disparador, True) #encendemos el pin Trig
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(disparador, False) #y lo volvemos a apagar
 
  #empezaremos a contar el tiempo cuando el pin Echo se encienda
   while GPIO.input(receptor) == 0:
      comienzo = time.time()
 
   while GPIO.input(receptor) == 1:
      final = time.time()
 
   #La duracion del pulso del pin Echo sera la diferencia entre
   #el tiempo de inicio y el final
   duracion = final-comienzo
 
   #como la duracion del tiempo esta en mili segundos 
   #debemosa pasar a segundos
   duracion = duracion*10**6
   distancia = duracion/58 #hay que dividir por la constante que pone en la documentacion, nos dara la distancia en cm
 
   print "%.1f" %distancia #por ultimo
    ## en el bucle principal 
while True:
	try:
		detec_espacio()
		time.sleep(0.5)
	except KeyboardInterrupt:
		break