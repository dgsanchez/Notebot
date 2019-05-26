import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time

t = 1

pulsos={
#Ida#Vuelta
    60:[9.6,9.6], #C4
    62:[9.2,9.2], #D4
    64:[8.9,8.8], #E4
    65:[8.6,8.5], #F4
    67:[8.3,8.2], #G4
    69:[7.8,7.9], #A4
    71:[7.4,7.4], #B4
    72:[7.1,7.1], #C5
    74:[6.6,6.6], #D5
    76:[6.25,6.25], #E5
    77:[5.8,5.8], #F5
    79:[5.4,5.4], #G5
    81:[4.9,4.9], #A5
    83:[4.55,4.55], #B5
    84:[4.3,4.3] #C6
}

def init():
    GPIO.setmode(GPIO.BOARD)  # Ponemos la Raspberry en modo BOARD
    GPIO.setup(5, GPIO.OUT)  # Ponemos el pin 5 como salida
    p = GPIO.PWM(5, 50)  # Ponemos el pin 5 en modo PWM y enviamos 50 pulsos por segundo
    p.start(7)  # Enviamos un pulso del 7% para centrar el servo

    time.sleep(1)

    GPIO.setup(3, GPIO.OUT)  # Ponemos el pin 3 como salida
    d = GPIO.PWM(3, 50)  # Ponemos el pin 3 en modo PWM y enviamos 50 pulsos por segundo
    d.start(7)  # Enviamos un pulso del 7% para centrar el servo

    time.sleep(1)
    return p,d

def tocarNota(durada, nota,brac,dit,anar):
    try:
        if (anar==0):
            print("tornar",nota)
        else:
            print("anar",nota)
        brac.ChangeDutyCycle(pulsos[nota][anar])
        time.sleep(1.25)

        dit.ChangeDutyCycle(5.3)#5.5
        time.sleep(0.5)#0.75

        dit.ChangeDutyCycle(7)
        time.sleep(durada)#0.5

    except KeyboardInterrupt:  # Si el usuario pulsa CONTROL+C entonces...
        dit.stop()
        brac.stop()  # Detenemos el servo
        GPIO.cleanup()  # Limpiamos los pines GPIO

def tocarCanco(arrayNotes,brac,dit):
    try:
        tocarNota(arrayNotes[0][0],arrayNotes[0][1],brac,dit,0)
        #print(arrayNotes,len(arrayNotes))
        for i in range(1,len(arrayNotes)):
            if (arrayNotes[i][1]-arrayNotes[i-1][1])<0:
                tocarNota(arrayNotes[i][0],arrayNotes[i][1],brac,dit,0)
            else:
                tocarNota(arrayNotes[i][0],arrayNotes[i][1],brac,dit,1)
        dit.stop()
        brac.stop()  # Detenemos el servo
        GPIO.cleanup()  # Limpiamos los pines GPIO

    except KeyboardInterrupt:  # Si el usuario pulsa CONTROL+C entonces...
        dit.stop()
        brac.stop()  # Detenemos el servo
        GPIO.cleanup()  # Limpiamos los pines GPIO