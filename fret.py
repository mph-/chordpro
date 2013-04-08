class Fret(object):

    UNPLAYED = '-'
    MUTED = 'x'
    OPEN = 0

    def __init__(self, fret, base_fret=1):

        # Convert relative fret to an absolute fret.
        fret = fret.strip()
        if fret == '-':
            fretnum = Fret.UNPLAYED
        elif fret.lower() == 'x':
            fretnum = Fret.MUTED
        else:
            fretnum = int(fret)
            if fretnum != 0:
                fretnum += base_fret - 1

        self.fret = fretnum

    
    def __str__(self):

        return self.format()


    def format(self, base_fret=1, unplayed='-', muted='x'):

        if self.fret == Fret.UNPLAYED:
            return unplayed
        if self.fret == Fret.MUTED:
            return muted
        if self.fret == Fret.OPEN:
            return '0'

        # Return absolute fret number if base_fret is zero.
        if base_fret == 0:
            return '%d' % self.fret

        fret = self.fret - base_fret + 1
        return '%d' % fret


    def format_gchord(self, base_fret=1):

        if self.fret == Fret.UNPLAYED:
            return 'n'
        if self.fret == Fret.MUTED:
            return 'x'
        if self.fret == Fret.OPEN:
            return 'o'

        fret = self.fret - base_fret + 1

        if fret > 9:
            return 'p{%d}' % fret
        
        return 'p%d' % fret
