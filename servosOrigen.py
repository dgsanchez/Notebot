import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

def origen():
     dedo.ChangeDutyCycle(7)
     time.sleep(0.75)
     brazo.ChangeDutyCycle(4.3)
     time.sleep(0.75)
     dedo.stop()
     brazo.stop()
     GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(5,GPIO.OUT)    #Ponemos el pin 5 como salida para el brazo
brazo = GPIO.PWM(5,50)        #Ponemos el pin 5 en modo PWM y enviamos 50 pulsos por segundo
brazo.start(7)               #Enviamos un pulso del 7% para centrar el servo


GPIO.setup(3,GPIO.OUT)    #Ponemos el pin 3 como salida para el dedo
dedo = GPIO.PWM(3,50)        #Ponemos el pin 3 en modo PWM y enviamos 50 pulsos por segundo
dedo.start(7)               #Enviamos un pulso del 7% para centrar el servo


try:
    origen()


except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    dedo.stop()
    brazo.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script

