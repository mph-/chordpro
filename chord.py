class Chord(object):

    EASY = 0
    HARD = 1
    USER = 2

    def __init__(self, name, frets, base_fret, type=USER):
        self.name = name
        self._base_fret = base_fret
        self._frets = frets
        self._type = type


    def __str__(self):
        return '%s base-fret %s frets %s' % (self.name, self._base_fret, self._frets)

