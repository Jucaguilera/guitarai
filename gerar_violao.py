from mido import Message, MidiFile, MidiTrack, bpm2tempo, MetaMessage

def note_to_int(n):
    notas = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
    if len(n)==2:
        nome, oit = n[0], int(n[1])
    else:
        nome, oit = n[:2], int(n[2])
    return 12*(oit+1) + notas[nome]

# Parâmetros
bpm = 90
acordes = [['C3','E3','G3'], ['G2','B2','D3'], ['A2','C3','E3'], ['F2','A2','C3']]
reps = 2
ticks = 480
# Swing timing: first colcheia longa (320), depois curta (160)
ritmo = [0, 320, 480, 800]

mid = MidiFile(ticks_per_beat=ticks)
track = MidiTrack()
mid.tracks.append(track)

track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm), time=0))
track.append(Message('program_change', program=24, time=0))

for _ in range(reps):
    for acorde in acordes:
        for i, tick in enumerate(ritmo):
            time = tick if i==0 else 0
            for n in acorde:
                track.append(Message('note_on', note=note_to_int(n), velocity=90, time=time))
                time = 0
            for n in acorde:
                track.append(Message('note_off', note=note_to_int(n), velocity=90, time=160))

mid.save("violao.mid")
print("✅ Gerei 'violao.mid'")
