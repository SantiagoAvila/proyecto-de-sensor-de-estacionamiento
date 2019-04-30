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
import time #se necesita para usar las funciones de tiempo

GPIO.setmode(GPIO.BOARD) #Queremos usar la numeracion de la placa raspberry
#Definimos los dos pines del sensor que hemos conectado: disparador y Eco
disparador = 11
Eco = 13
#Hay que configurar ambos pines del HC-SR04
GPIO.setup(disparador, GPIO.OUT)
GPIO.setup(Eco, GPIO.IN)
#Para leer la distancia del sensor al lugar del estacionamiento, creamos una funcion
def detectar_lugar():
 
   GPIO.output(disparador, False) #apagamos el pin disparador
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(disparador, True) #encendemos el pin disparador
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(disparador, False) #y lo volvemos a apagar
  #empezaremos a contar el tiempo cuando el pin Eco se encienda
   while GPIO.input(Eco) == 0:
      start = time.time()

   while GPIO.input(Eco) == 1:
      end = time.time()
 
   #La duracion del pulso del pin Eco sera la diferencia entre
   #el tiempo de inicio y el final
   duracion = end-start
 
   #Este tiempo viene dado en segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   duracion = duracion*10**6
   medida = duracion/58 #hay que dividir por la constante que pone en la documentacion, nos dara la distancia en cm
   return medida
    #por ultimo, vamos a mostrar el resultado por pantalla
 
#Bucle principal del programa, lee el sensor. Se sale con CTRL+C
while True:
   try:
      d=detectar_lugar()
      if 73<=d<=75:
         print("libre")
      else:
         print("ocupado")
      time.sleep(0.7)
   except KeyboardInterrupt:
      break