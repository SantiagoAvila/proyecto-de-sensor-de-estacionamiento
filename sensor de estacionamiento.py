#### proyecto de penguin bootcamp
"""
ESTO DEBE CORRER EN LA RASPBERRY PARA QUE FUNCIONE

Tutores Claves: Willi Bobadilla @WilliBobadilla y Lorena Zalazar @Lorelulen
Objetivo:
        en el presente archivo se intentara realizar una pagina web para el monitoreo de vacancias 
        de estacionamientos funcional en un local determinado utilizando raspberry, que responda en
        una web basica diseñada por nosotros
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
import time #se necesita para usar las funciones de tiempo
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD) #definimos la configuracion de la raspberry para utilizar la numeracion de los pines
disparador1 = 3
Eco1 = 5
disparador2 = 38
Eco2 = 40
 
#Hay que configurar ambos pines del HC-SR04 para ambos sensores
GPIO.setup(disparador1, GPIO.OUT)
GPIO.setup(Eco1, GPIO.IN)
GPIO.setup(disparador2,GPIO.OUT)
GPIO.setup(Eco2,GPIO.IN)
#definimos la funcion para el sensor numero 1 
def detectar_lugar1():
 
   GPIO.output(disparador1, False) #apagamos el pin disparador1
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(disparador1, True)#encendemos el pin 
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(disparador1, False)#y lo volvemos a apagar
 
  #empezaremos a contar el tiempo cuando el pin Eco1 se encienda
   while GPIO.input(Eco1) == 0:
      start_1 = time.time()
 
   while GPIO.input(Eco1) == 1:
      end_1 = time.time()
      
   #La duracion del pulso del pin Eco sera la diferencia entre
   #el tiempo de inicio y el final
   duracion_1 = end_1-start_1
 
   #Este tiempo viene dado en  segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   #encontradas en los ejemplos extraidos
   duracion1 = duracion_1*10**6
   medida1 = duracion1/58 #hay que dividir por la constante que pone en la documentacion, 
   #nos dara la distancia en cm
   return medida1
#definimos la funcion para el lugar2
def detectar_lugar2():
   GPIO.output(disparador2, False) #apagamos el pin dispardor y seguimos los mismos pasos del lugar 1
   time.sleep(2*10**-6)
   GPIO.output(disparador2, True)
   time.sleep(10*10**-6) 
   GPIO.output(disparador2, False)
  #empezaremos a contar el tiempo cuando el pin Eco2 se encienda
   while GPIO.input(Eco2) == 0:
      start_2 = time.time()
 
   while GPIO.input(Eco2) == 1:
      end_2 = time.time()
      
   #La duracion del pulso del pin Eco2 sera la diferencia entre
   #el tiempo de inicio2 y el final2
   duracion_2 = end_2-start_2
 
   #Este tiempo viene dado en segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   #de la documentacion
   duracion2 = duracion_2*10**6
   medida2 = duracion2/58   #hay que dividir por la constante que pone en la documentacion, 
                            #nos dara la distancia en cm
   return medida2
#Bucle principal del programa, lee el sensor. Se sale con CTRL+C
while True:
   try:
      d1=detectar_lugar1()              #ahora guardamos los valores retornados al llamar las funciones
      d2=detectar_lugar2()              # para luego con los if relacionar para definir si esta o no libre 
      if d1>=14.5:                        #para esta maqueta se hara en miniatura por lo cual los valores son
         print("libre espacio 1")       #realmente muy pequeños pero si es para un estacionamiento estandar
      else:                             #se deben usar los valores de la descripcion 
         print("ocupado espacio 1")
      if 14.5<=d2:
         print("libre espacio 2")
      else:
         print("ocupado espacio 2")
      time.sleep(0.7)                   #por ultimo le damos un sleep para reiniciar la funcion 
   except KeyboardInterrupt:
      break                             #ponemos un break para detener el programa