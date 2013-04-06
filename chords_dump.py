from chord import Chord
from chords import Chords


class ChordsDump(object):

    def __init__(self, frets=False, format='gchord'):
        self._used_chords = []
        self._chords = Chords()
        self._frets = frets
        self._format = format


    def visit_d(self, text):
        import sys

        c = text.split('base-fret', 1)
        if len(c) != 2:
            sys.stderr.write('Invalid define format: ' + text + '\n')
            return

        chordname = c[0]

        c = c[1].split('frets', 1)
        if len(c) != 2:
            sys.stderr.write('Invalid define format: ' + text + '\n')
            return

        self._chords.add(Chord(chordname, c[1], c[0]))


    def visit_line(self, chords):
        line = ''
        for chord, text in chords:
            if not chord:
                continue
            if chord not in ('/', 'N.C.') and chord not in self._used_chords:
                self._used_chords.append(chord)


    def result(self):

        if self._frets:
            return '\n'.join([self._chords.find(chordname).format(self._format) for chordname in self._used_chords]) + '\n'

        return ' '.join(self._used_chords) + '\n'

