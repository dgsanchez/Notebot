import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

def tocar(pulso):
    brazo.ChangeDutyCycle(pulso)
    print(pulso)
    time.sleep(1.25)#2.5

    dedo.ChangeDutyCycle(5.5)
    time.sleep(0.5)#0.75
    dedo.ChangeDutyCycle(7)
    time.sleep(0.5)#1

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
        print("Do:60")
        tocar(9.6)#check
        print("Re:62")
        tocar(9.2)#checkvuelta
        print("Mi:64")
        tocar(8.8)#checkvuelta
        print("Fa:65")
        tocar(8.5)
        print("Sol:67")
        tocar(8.2)
        print("La:69")
        tocar(7.9)
        print("Si:71")
        tocar(7.4)#checkvuelta
        print("Do:72")
        tocar(7.1)#checkida
        print("Re:74")
        tocar(6.6)#checkvuelta
        print("Mi:76")
        tocar(6.2)#checkvuelta
        print("Fa:77")
        tocar(5.8)#checkvuelta
        print("Sol:79")
        tocar(5.4)#checkvuelta
        print("La:81")
        tocar(4.9)#checkvuelta
        print("Si:83")
        tocar(4.55)#checkvuelta
        print("Do:84")
        tocar(4.1)#check
        t +=1 

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    dedo.stop()
    brazo.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script

print("Clean up")
dedo.stop()
brazo.stop()
GPIO.cleanup()
"""

# testservo.py
 
import time
 
import pigpio
 
pi = pigpio.pi() # Connect to local Pi.
     
# set gpio modes
pi.set_mode(2, pigpio.OUTPUT)
     
     
# start 1500 us servo pulses on gpio2
pi.set_servo_pulsewidth(3, 1500)
time.sleep(1)
for _i in range(3): #loop between -90 and 90 degrees
    #pi.set_servo_pulsewidth(3,600)
    #time.sleep(1)
    pi.set_servo_pulsewidth(3,1500)
    time.sleep(1)
    pi.set_servo_pulsewidth(3, 900)
    time.sleep(1)
 
pi.set_servo_pulsewidth(3, 0) # stop servo pulses
 
pi.stop() # terminate connection and release resources
"""
