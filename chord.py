from fret import Fret

class Chord(object):

    EASY = 0
    HARD = 1
    USER = 2

    def __init__(self, name, fretsstr, base_fret, chordtype=USER):

        base_fret = int(base_fret) if type(base_fret) != 'int' else base_fret
        if base_fret == 0:
            base_fret = 1
        self.name = name.strip()
        self._base_fret = base_fret
        self._frets = [Fret(fret, base_fret) for fret in fretsstr.strip(' ').split(' ')]
        self._type = chordtype


    def __str__(self):

        return self._format_simple()
        

    def texname(self):

        return self.name.replace('#', '$\\sharp$').replace('b', '$\\flat$')


    def _format_gchord(self):
        if self._base_fret == 1:
            modifier = 't'
        elif self._base_fret < 9:
            modifier = '%d' % self._base_fret
        else:
            modifier = '{%d}' % self._base_fret

        return '\chord{' + modifier + '}{' + ','.join([fret.format_gchord(self._base_fret) for fret in self._frets]) + '}{' + self.texname() + '}'


    def _format_texchord(self):
        return self._format_gchord().replace('chord', 'drawchord')


    def _format_chordpro(self):

        fretsstr = ' '.join([fret.format(self._base_fret) for fret in self._frets])
        return '{define %s base-fret %s frets %s}' % (self.name, self._base_fret, fretsstr)


    def _format_simple(self):

        fretsstr = ' '.join([fret.format(0) for fret in self._frets])
        return '%s: %s' % (self.name, fretsstr)


    def format(self, format='texchord'):

        if format == 'texchord':
            return self._format_texchord()
        elif format == 'gchord':
            return self._format_gchord()
        elif format == 'chordpro':
            return self._format_chordpro()
        return self._format_simple()
