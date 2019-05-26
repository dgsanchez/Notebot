import funcions
import sys

brac,dit=funcions.init()


frereJaques=[[1,72],[1,74],[1,76],[1,72],[1,72],[1,74],[1,76],[1,72],[1,76],[1,77],[2,79],[1,76],[1,77],[2,79],
             [0.75,79],[0.75,81],[0.75,79],[0.75,77],[1,76],[1,72],[0.75,79],[0.75,81],[0.75,79],[0.75,77],[1,76],
             [1,72],[1,74],[1,71],[2,72],[1,74],[1,71],[2,72]]

gegantPi=[[0.5,76],[0.5,77],[0.75,79],[0.75,76],[0.75,72],[0.5,77],[0.5,76],[0.5,74],[0.5,72],[0.5,74],[0.5,74],[0.75,76],[0.75,72],
          [0.5,76],[0.5,77],[0.75,79],[0.75,76],[0.75,72],[0.5,77],[0.5,76],[0.5,74],[0.5,72],[0.75,74],[0.75,76],[0.75,72]]

imperialMarch=[[0.75,69],[0.75,69],[0.75,69],[0.5,65],[0.5,72],[0.75,69],[0.5,65],[0.5,72],[0.75,69],[0.75,76],[0.75,76],[0.75,76],
               [0.5,77],[0.5,72],[0.75,69],[0.5,65],[0.5,72],[0.75,69]]

try:
    if sys.argv[1] == "1":
      funcions.tocarCanco(gegantPi,brac,dit)
    
    elif sys.argv[1] == "2":
      funcions.tocarCanco(frereJaques,brac,dit)

    elif sys.argv[1] == "3":
      funcions.tocarCanco(imperialMarch,brac,dit)

except KeyboardInterrupt:  # Si el usuario pulsa CONTROL+C entonces...
    dit.stop()
    brac.stop()  # Detenemos el servo
    GPIO.cleanup()  # Limpiamos los pines GPIO

    
    
