from parser import shorten, lengthen
from chord import Chord
from chords import Chords


class ChordsDump(object):

    def __init__(self):
        self._used_chords = []
        self._chords = Chords()

    def visit_define(self, text):
        c = text.split(' ', 1)
        chordname = c[0]

        c = c[1].split(' ', 3)
        if c[0] != 'base-fret' or c[2] != 'frets':
            sys.stderr.write('Invalid define format: ' + text)

        self._chords.add(Chord(chordname, c[3], c[1]))

    def visit_line(self, chords):
        line = ''
        for chord, text in chords:
            if not chord:
                continue
            if chord not in ('/', 'N.C.') and chord not in self._used_chords:
                self._used_chords.append(chord)

    def result(self):
        for chord in self._chords.chords:
            print chord

        return ' '.join(self._used_chords) + '\n'

