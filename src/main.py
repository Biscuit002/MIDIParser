from mido import MidiFile
from pathlib import Path

midi_file = None
midi_file_path = Path(__file__).parent.parent / 'data'

#Access midifile from data folder
for n in midi_file_path.iterdir():
    if n.suffix.lower() == '.mid':
        midi_file = MidiFile(n)
        break

if midi_file is None:
    midi_file = 'cannot find midi file'
log = open(midi_file_path)