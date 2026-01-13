from mido import MidiFile
from pathlib import Path
from datetime import datetime

midi_file = None
midi_file_path = Path(__file__).parent.parent / 'data'

#Access midifile from data folder
for n in midi_file_path.iterdir():
    if n.suffix.lower() == '.mid':
        midi_file = MidiFile(n)
        break
if midi_file is None:
    midi_file = 'cannot find midi file'




#create log file with timestamp
log_path = Path(__file__).parent.parent / 'output'
log = open(log_path / f'log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt', 'w')
log.write(str(midi_file))
log.close()