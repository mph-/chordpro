class Fret(object):

    def __init__(self, fret, base_fret=1):

        # Convert relative fret to an absolute fret with -2 unplayed, -1 muted, and 0 open.
        fret = fret.strip()
        if fret == '-':
            fretnum = -2
        elif fret.lower() == 'x':
            fretnum = -1
        else:
            fretnum = int(fret)
            if fretnum != 0:
                fretnum += base_fret - 1

        self.fret = fretnum

    
    def __str__(self):

        return self.format()


    def format(self, base_fret=1):

        if self.fret == -2:
            return '-'
        if self.fret == -1:
            return 'x'

        if base_fret == 0:
            return '%d' % self.fret

        fret = self.fret - base_fret + 1
        return '%d' % fret


    def format_gchord(self, base_fret=1):

        if self.fret == -2:
            return 'n'
        if self.fret == -1:
            return 'x'
        if self.fret == 0:
            return 'o'

        fret = self.fret - base_fret + 1

        if fret > 9:
            return 'p{%d}' % fret
        
        return 'p%d' % fret
