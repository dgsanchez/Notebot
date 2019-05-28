# Notebot

Pianist robot capable of playing simple melodies provided through a microphone in a music keyboard of 2 octaves.

## Keypad.py

Controlsontrols all the information from the switch matrix, allowing the human-machine interaction. Autostart after powering up the Raspberry Pi, waiting for petitions.

## ServosIda.py | ServosVuelta.py

These two scripts are tools coded for the servos' calibration, assigning a pulse for the servo for each key in the piano.

## ServosOrigen.py

It positions the servo at the origin point.

## CodiTocar.py

Contains various arrays of midi notes, along with the duration of each, which are later transformed in pulses or servo position for playing the different pre-programmed songs.

## Note_Detector.py

Detection of musical notes in a .WAV file, previously recorded by a person through the microphone.

## Funcions.py

Contains the basic functions for playing a note and a song, these functions are called from other scripts in the project, like CodiTocar.py

Project for the RLP subject at Universitat Autònoma de Barcelona.

Copyright © 2019 Ferran Rodríguez Mir, Josep Douton Martín, Gerard Aceves Soley, David Sánchez González