import mido
from pathlib import Path

midi_file = None
midi_file_path = Path(__file__).parent.parent / 'data'
for n in midi_file_path.iterdir():
    if n.suffix.lower() == '.mid':
        midi_file = n
        break

if midi_file is None:
    midi_file = 'cannot find midi file'
print(midi_file)