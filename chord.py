def fretmap(fret, base_fret):

    if fret not in ('-', '?', 'x'):
        fret = '%d' % (int(fret) + base_fret - 1)
    return fret


class Chord(object):

    EASY = 0
    HARD = 1
    USER = 2

    def __init__(self, name, fretsstr, base_fret, chordtype=USER):
        self.name = name.strip()
        self._base_fret = int(base_fret) if type(base_fret) != 'int' else base_fret
        self._frets = fretsstr.strip(' ').split(' ')
        self._type = chordtype

        if self._base_fret == 0:
            self._base_fret = 1


    def __str__(self):
        return '%s base-fret %s frets %s' % (self.name, self._base_fret, self._frets)


    def texname(self):

        return self.name.replace('#', '$\\sharp$').replace('b', '$\\flat$')


    def _format_fret(self, fret):

        if fret == 'x':
            return fret
        if fret in ('-', '?'):
            return 'x'

        fretnum = int(fret)
        if fretnum == 0 and self._base_fret == 1:
            return 'o'

        if fretnum > 9:
            return 'p{%d}' % fretnum
        
        return 'p%d' % fretnum


    def _format_gchord(self):
        if self._base_fret == 1:
            modifier = 't'
        elif self._base_fret < 9:
            modifier = '%d' % self._base_fret
        else:
            modifier = '{%d}' % self._base_fret

        return '\chord{' + modifier + '}{' + ','.join([self._format_fret(fret) for fret in self._frets]) + '}{' + self.texname() + '}'


    def _format_texchord(self):
        return self._format_gchord().replace('chord', 'drawchord')


    def _format_chordpro(self):

        return '{define %s base-fret %s frets %s}' % (self.name, self._base_fret, ' '.join(self._frets))


    def _format_simple(self):

        return self.name + ': ' + ' '.join([fretmap(fret, self._base_fret) for fret in self._frets])


    def format(self, format='texchord'):

        if format == 'texchord':
            return self._format_texchord()
        elif format == 'gchord':
            return self._format_gchord()
        elif format == 'chordpro':
            return self._format_chordpro()
        return self._format_simple()
