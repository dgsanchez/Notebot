import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep
import sys

def tocar(pulso):
    brazo.ChangeDutyCycle(pulso)
    print(pulso)
    time.sleep(1.25)

    dedo.ChangeDutyCycle(5.5)
    time.sleep(0.5)
    dedo.ChangeDutyCycle(7)
    time.sleep(0.5)

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(5,GPIO.OUT)    #Ponemos el pin 5 como salida para el brazo
brazo = GPIO.PWM(5,50)        #Ponemos el pin 5 en modo PWM y enviamos 50 pulsos por segundo
brazo.start(7)               #Enviamos un pulso del 7% para centrar el servo

GPIO.setup(3,GPIO.OUT)    #Ponemos el pin 3 como salida para el dedo
dedo = GPIO.PWM(3,50)        #Ponemos el pin 3 en modo PWM y enviamos 50 pulsos por segundo
dedo.start(7)               #Enviamos un pulso del 7% para centrar el servo

t = 0

try:
    while t!=1:      #iniciamos un loop finit
#        pulse = float(input("Introduce un pulso: "))
        print("Do:84")
        tocar(4.1)#checkIda
        print("Si:83")
        tocar(4.55)#checkIda
        print("La:81")
        tocar(4.9)#checkIda
        print("Sol:79")
        tocar(5.4)#checkIda
        print("Fa:77")
        tocar(5.8)#checkIda
        print("Mi:76")
        tocar(6.25)#checkIda
        print("Re:74")
        tocar(6.6)#checkIda
        print("Do:72")
        tocar(7.1)#checkIda
        print("Si:71")
        tocar(7.4)#checkIda
        print("La:69")
        tocar(7.8)
        print("Sol:67")
        tocar(8.3)
        print("Fa:65")
        tocar(8.6)
        print("Mi:64")
        tocar(8.9)#checkIda
        print("Re:62")
        tocar(9.2)#checkIda
        print("Do:60")
        tocar(9.6)#check
        
        t +=1 

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    dedo.stop()
    brazo.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script

print("Clean up")
dedo.stop()
brazo.stop()
GPIO.cleanup()

