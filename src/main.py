from mido import MidiFile
from pathlib import Path
from datetime import datetime
import json

midi_file = None
midi_file_path = Path(__file__).parent.parent / 'data'

json_file = []

#Access midifile from data folder
for n in midi_file_path.iterdir():
    if n.suffix.lower() == '.mid':
        midi_file = MidiFile(n)
        break
if midi_file is None:
    midi_file = 'cannot find midi file'

#Form output json
for tracks in midi_file.tracks:
    track_data = {}
    time_signatures = []
    key_signatures = []
    for msg in tracks:
        if msg.type == 'track_name':
            track_data['instrument_name'] = msg.name
        if msg.type == 'time_signature':
            time_signatures.append({'numerator': msg.numerator, 'denominator': msg.denominator})
            track_data['time_signature'] = time_signatures
        if msg.type == 'key_signature':
            key_signatures.append({'key': msg.key})
            track_data['key_signature'] = key_signatures
    json_file.append(track_data)

#change to any variable to write on log
logwrite = str(midi_file)

#create log file with timestamp
log_path = Path(__file__).parent.parent / 'output'
log = open(log_path / f'log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt', 'w')
log.write(logwrite)
log.close()