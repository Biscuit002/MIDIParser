from mido import MidiFile
from pathlib import Path

mid = MidiFile('/workspaces/MIDIParser/data/swan-lake-no.-10-scne-in-b-minor-opus-20--tchaikovsky.mid')
log = open('mid.txt', 'w')
log.write(str(mid))