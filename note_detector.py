#! /usr/bin/env python

import sys
from aubio import source, notes
import numpy as np
import funcions

def delete_sustain(noteList):
    sustained = [1, 3, 6, 8, 10]

    if len(noteList) > 0:
        for idx in range(len(noteList)):
            if (noteList[idx][1] % 12) in sustained:
                noteList[idx][1] -= 1 # Transformamos la sostenida a la nota "padre"

            if noteList[idx][1] < 60:
                noteList[idx][1] = 60 + (noteList[idx][1] % 12)

            if noteList[idx][1] > 84:
                noteList[idx][1] =  72 + (noteList[idx][1] % 12)
        
        
    else:
        print("No hay notas en la lista.")

if len(sys.argv) < 2:
    print("Usage: %s <filename> [samplerate]" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]

downsample = 1
samplerate = 44100 // downsample
if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

win_s = 512 // downsample # fft size
hop_s = 256 // downsample # hop size

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8

notes_o = notes("default", win_s, hop_s, samplerate)

print("%8s" % "time","%11s" % "MIDI")

# total number of frames read
total_frames = 0
note_list = []
while True:
    samples, read = s()
    new_note = notes_o(samples)
    if (new_note[0] != 0):
        note_str = ' '.join(["%.2f" % i for i in new_note])
        #print("%.6f" % (total_frames/float(samplerate)), new_note)
        note_list.append([(total_frames/float(samplerate)), new_note[0]])
    total_frames += read
    if read < hop_s: break


final_list = np.copy(note_list)
final_list[-1][0] = 5.0 - note_list[-1][0]

for note in range(1, len(note_list)-1):
    final_list[note][0] = float(note_list[note][0] - note_list[note - 1][0])

np.set_printoptions(suppress=True)
delete_sustain(final_list)
final_list = final_list[final_list[:, 0] > 0.15]
print (final_list)

brac, dit = funcions.init()
funcions.tocarCanco(final_list, brac, dit)

