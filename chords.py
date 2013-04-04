from chord import Chord

class Chords(object):

    def __init__(self):

        self.chords = {}
        
	self.add(Chord('Ab', '1 3 3 2 1 1', 4, Chord.HARD))
        self.add(Chord('Ab+', '- - 2 1 1 0', 1, Chord.HARD))
        self.add(Chord('Ab4', '- - 1 1 2 4', 1, Chord.HARD))
        self.add(Chord('Ab7', '- - 1 1 1 2', 1, Chord.HARD))
        self.add(Chord('Ab11', '1 3 1 3 1 1', 4, Chord.HARD))
        self.add(Chord('Absus', '- - 1 1 2 4', 1, Chord.HARD))
        self.add(Chord('Absus4', '- - 1 1 2 4', 1, Chord.HARD))
        self.add(Chord('Abdim', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('Abmaj', '1 3 3 2 1 1', 4, Chord.HARD))
        self.add(Chord('Abmaj7', '- - 1 1 1 3', 1, Chord.HARD))
        self.add(Chord('Abmin', '1 3 3 1 1 1', 4, Chord.HARD))
        self.add(Chord('Abm', '1 3 3 1 1 1', 4, Chord.HARD))
        self.add(Chord('Abm7', '- - 1 1 1 1', 4, Chord.HARD))

        self.add(Chord('A', '- 0 2 2 2 0', 1, Chord.EASY))
        self.add(Chord('A+', '- 0 3 2 2 1', 1, Chord.HARD))
        self.add(Chord('A4', '0 0 2 2 0 0', 1, Chord.HARD))
        self.add(Chord('A6', '- - 2 2 2 2', 1, Chord.HARD))
        self.add(Chord('A7', '- 0 2 0 2 0', 1, Chord.EASY))
        self.add(Chord('A7+', '- - 3 2 2 1', 1, Chord.HARD))
        self.add(Chord('A7(9+)', '- 2 2 2 2 3', 1, Chord.HARD))
        self.add(Chord('A9', '- 0 2 1 0 0', 1, Chord.HARD))
        self.add(Chord('A11', '- 4 2 4 3 3', 1, Chord.HARD))
        self.add(Chord('A13', '- 0 1 2 3 1', 5, Chord.HARD))
        self.add(Chord('A7sus4', '0 0 2 0 3 0', 1, Chord.HARD))
        self.add(Chord('A9sus', '- 0 2 1 0 0', 1, Chord.HARD))
        self.add(Chord('Asus', '- - 2 2 3 0', 1, Chord.HARD))
        self.add(Chord('Asus2', '0 0 2 2 0 0', 1, Chord.HARD))
        self.add(Chord('Asus4', '- - 2 2 3 0', 1, Chord.HARD))
        self.add(Chord('Adim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('Amaj', '- 0 2 2 2 0', 1, Chord.HARD))
        self.add(Chord('Amaj7', '- 0 2 1 2 0', 1, Chord.HARD))
        self.add(Chord('Adim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('Amin', '- 0 2 2 1 0', 1, Chord.HARD))
        self.add(Chord('A/D', '- - 0 0 2 2', 1, Chord.HARD))
        self.add(Chord('A/F#', '2 0 2 2 2 0', 1, Chord.HARD))
        self.add(Chord('A/G#', '4 0 2 2 2 0', 1, Chord.HARD))

        self.add(Chord('Am', '- 0 2 2 1 0', 1, Chord.EASY))
        self.add(Chord('Am#7', '- - 2 1 1 0', 1, Chord.HARD))
        self.add(Chord('Am(7#)', '- 0 2 2 1 4', 1, Chord.HARD))
        self.add(Chord('Am6', '- 0 2 2 1 2', 1, Chord.HARD))
        self.add(Chord('Am7', '- 0 2 2 1 3', 1, Chord.EASY))
        self.add(Chord('Am7sus4', '0 0 0 0 3 0', 1, Chord.HARD))
        self.add(Chord('Am9', '- 0 1 1 1 3', 5, Chord.HARD))
        self.add(Chord('Am/G', '3 0 2 2 1 0', 1, Chord.HARD))
        self.add(Chord('Amadd9', '0 2 2 2 1 0', 1, Chord.HARD))
        self.add(Chord('Am(add9)', '0 2 2 2 1 0', 1, Chord.HARD))

        self.add(Chord('A#', '- 1 3 3 3 1', 1, Chord.HARD))
        self.add(Chord('A#+', '- - 0 3 3 2', 1, Chord.HARD))
        self.add(Chord('A#4', '- - 3 3 4 1', 1, Chord.HARD))
        self.add(Chord('A#7', '- - 1 1 1 2', 3, Chord.HARD))
        self.add(Chord('A#sus', '- - 3 3 4 1', 1, Chord.HARD))
        self.add(Chord('A#sus4', '- - 3 3 4 1', 1, Chord.HARD))
        self.add(Chord('A#maj', '- 1 3 3 3 1', 1, Chord.HARD))
        self.add(Chord('A#maj7', '- 1 3 2 3 -', 1, Chord.HARD))
        self.add(Chord('A#dim', '- - 2 3 2 3', 1, Chord.HARD))
        self.add(Chord('A#min', '- 1 3 3 2 1', 1, Chord.HARD))
        self.add(Chord('A#m', '- 1 3 3 2 1', 1, Chord.HARD))
        self.add(Chord('A#m7', '- 1 3 1 2 1', 1, Chord.HARD))

        self.add(Chord('Bb', '- 1 3 3 3 1', 1, Chord.EASY))
        self.add(Chord('Bb+', '- - 0 3 3 2', 1, Chord.HARD))
        self.add(Chord('Bb4', '- - 3 3 4 1', 1, Chord.HARD))
        self.add(Chord('Bb6', '- - 3 3 3 3', 1, Chord.HARD))
        self.add(Chord('Bb7', '- - 1 1 1 2', 3, Chord.HARD))
        self.add(Chord('Bb9', '1 3 1 2 1 3', 6, Chord.HARD))
        self.add(Chord('Bb11', '1 3 1 3 4 1', 6, Chord.HARD))
        self.add(Chord('Bbsus', '- - 3 3 4 1', 1, Chord.HARD))
        self.add(Chord('Bbsus4', '- - 3 3 4 1', 1, Chord.HARD))
        self.add(Chord('Bbmaj', '- 1 3 3 3 1', 1, Chord.HARD))
        self.add(Chord('Bbmaj7', '- 1 3 2 3 -', 1, Chord.HARD))
        self.add(Chord('Bbdim', '- - 2 3 2 3', 1, Chord.HARD))
        self.add(Chord('Bbmin', '- 1 3 3 2 1', 1, Chord.EASY))
        self.add(Chord('Bbm', '- 1 3 3 2 1', 1, Chord.HARD))
        self.add(Chord('Bbm7', '- 1 3 1 2 1', 1, Chord.HARD))
        self.add(Chord('Bbm9', '- - - 1 1 3', 6, Chord.HARD))

        self.add(Chord('B', '- 2 4 4 4 2', 1, Chord.EASY))
        self.add(Chord('B+', '- - 1 0 0 4', 1, Chord.HARD))
        self.add(Chord('B4', '- - 3 3 4 1', 2, Chord.HARD))
        self.add(Chord('B7', '0 2 1 2 0 2', 1, Chord.EASY))
        self.add(Chord('B7+', '- 2 1 2 0 3', 1, Chord.HARD))
        self.add(Chord('B7+5', '- 2 1 2 0 3', 1, Chord.HARD))
        self.add(Chord('B7#9', '- 2 1 2 3 -', 1, Chord.HARD))
        self.add(Chord('B7(#9)', '- 2 1 2 3 -', 1, Chord.HARD))
        self.add(Chord('B9', '1 3 1 2 1 3', 7, Chord.HARD))
        self.add(Chord('B11', '1 3 3 2 0 0', 7, Chord.HARD))
        self.add(Chord('B11/13', '- 1 1 1 1 3', 2, Chord.HARD))
        self.add(Chord('B13', '- 2 1 2 0 4', 1, Chord.HARD))
        self.add(Chord('Bsus', '- - 3 3 4 1', 2, Chord.HARD))
        self.add(Chord('Bsus4', '- - 3 3 4 1', 2, Chord.HARD))
        self.add(Chord('Bmaj', '- 2 4 3 4 -', 1, Chord.HARD))
        self.add(Chord('Bmaj7', '- 2 4 3 4 -', 1, Chord.HARD))
        self.add(Chord('Bdim', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('Bmin', '- 2 4 4 3 2', 1, Chord.HARD))
        self.add(Chord('B/F#', '0 2 2 2 0 0', 2, Chord.HARD))
        self.add(Chord('BaddE', '- 2 4 4 0 0', 1, Chord.HARD))
        self.add(Chord('B(addE)', '- 2 4 4 0 0', 1, Chord.HARD))
        self.add(Chord('BaddE/F#', '2 - 4 4 0 0', 1, Chord.HARD))

        self.add(Chord('Bm', '- 2 4 4 3 2', 1, Chord.EASY))
        self.add(Chord('Bm6', '- - 4 4 3 4', 1, Chord.HARD))
        self.add(Chord('Bm7', '- 1 3 1 2 1', 2, Chord.EASY))
        self.add(Chord('Bmmaj7', '- 1 4 4 3 -', 1, Chord.HARD))
        self.add(Chord('Bm(maj7)', '- 1 4 4 3 -', 1, Chord.HARD))
        self.add(Chord('Bmsus9', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('Bm(sus9)', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('Bm7b5', '1 2 4 2 3 1', 1, Chord.HARD))

        self.add(Chord('C', '- 3 2 0 1 0', 1, Chord.EASY))
        self.add(Chord('C+', '- - 2 1 1 0', 1, Chord.HARD))
        self.add(Chord('C4', '- - 3 0 1 3', 1, Chord.HARD))
        self.add(Chord('C6', '- 0 2 2 1 3', 1, Chord.HARD))
        self.add(Chord('C7', '0 3 2 3 1 0', 1, Chord.EASY))
        self.add(Chord('C9', '1 3 1 2 1 3', 8, Chord.HARD))
        self.add(Chord('C9(11)', '- 3 3 3 3 -', 1, Chord.HARD))
        self.add(Chord('C11', '- 1 3 1 4 1', 3, Chord.HARD))
        self.add(Chord('Csus', '- - 3 0 1 3', 1, Chord.HARD))
        self.add(Chord('Csus2', '- 3 0 0 1 -', 1, Chord.HARD))
        self.add(Chord('Csus4', '- - 3 0 1 3', 1, Chord.HARD))
        self.add(Chord('Csus9', '- - 4 1 2 4', 7, Chord.HARD))
        self.add(Chord('Cmaj', '0 3 2 0 1 0', 1, Chord.HARD))
        self.add(Chord('Cmaj7', '- 3 2 0 0 0', 1, Chord.HARD))
        self.add(Chord('Cmin', '- 1 3 3 2 1', 3, Chord.HARD))
        self.add(Chord('Cdim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('C/B', '- 2 2 0 1 0', 1, Chord.HARD))
        self.add(Chord('Cadd2/B', '- 2 0 0 1 0', 1, Chord.HARD))
        self.add(Chord('CaddD', '- 3 2 0 3 0', 1, Chord.HARD))
        self.add(Chord('C(addD)', '- 3 2 0 3 0', 1, Chord.HARD))
        self.add(Chord('Cadd9', '- 3 2 0 3 0', 1, Chord.HARD))
        self.add(Chord('C(add9)', '- 3 2 0 3 0', 1, Chord.HARD))

        self.add(Chord('Cm', '- 1 3 3 2 1', 3, Chord.EASY))
        self.add(Chord('Cm7', '- 1 3 1 2 1', 3, Chord.EASY))
        self.add(Chord('Cm11', '- 1 3 1 4 -', 3, Chord.HARD))

        self.add(Chord('C#', '- - 3 1 2 1', 1, Chord.HARD))
        self.add(Chord('C#+', '- - 3 2 2 1', 1, Chord.HARD))
        self.add(Chord('C#4', '- - 3 3 4 1', 4, Chord.HARD))
        self.add(Chord('C#7', '- - 3 4 2 4', 1, Chord.HARD))
        self.add(Chord('C#7(b5)', '- 2 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('C#sus', '- - 3 3 4 1', 4, Chord.HARD))
        self.add(Chord('C#sus4', '- - 3 3 4 1', 4, Chord.HARD))
        self.add(Chord('C#maj', '- 4 3 1 1 1', 1, Chord.HARD))
        self.add(Chord('C#maj7', '- 4 3 1 1 1', 1, Chord.HARD))
        self.add(Chord('C#dim', '- - 2 3 2 3', 1, Chord.HARD))
        self.add(Chord('C#min', '- - 2 1 2 0', 1, Chord.HARD))
        self.add(Chord('C#add9', '- 1 3 3 1 1', 4, Chord.HARD))
        self.add(Chord('C#(add9)', '- 1 3 3 1 1', 4, Chord.HARD))
        self.add(Chord('C#m', '- - 2 1 2 0', 1, Chord.HARD))
        self.add(Chord('C#m7', '- - 2 4 2 4', 1, Chord.HARD))

        self.add(Chord('Db', '- - 3 1 2 1', 1, Chord.HARD))
        self.add(Chord('Db+', '- - 3 2 2 1', 1, Chord.HARD))
        self.add(Chord('Db7', '- - 3 4 2 4', 1, Chord.HARD))
        self.add(Chord('Dbsus', '- - 3 3 4 1', 4, Chord.HARD))
        self.add(Chord('Dbsus4', '- - 3 3 4 1', 4, Chord.HARD))
        self.add(Chord('Dbmaj', '- - 3 1 2 1', 1, Chord.HARD))
        self.add(Chord('Dbmaj7', '- 4 3 1 1 1', 1, Chord.HARD))
        self.add(Chord('Dbdim', '- - 2 3 2 3', 1, Chord.HARD))
        self.add(Chord('Dbmin', '- - 2 1 2 0', 1, Chord.HARD))
        self.add(Chord('Dbm', '- - 2 1 2 0', 1, Chord.HARD))
        self.add(Chord('Dbm7', '- - 2 4 2 4', 1, Chord.HARD))

        self.add(Chord('D', '- - 0 2 3 2', 1, Chord.EASY))
        self.add(Chord('D+', '- - 0 3 3 2', 1, Chord.HARD))
        self.add(Chord('D4', '- - 0 2 3 3', 1, Chord.HARD))
        self.add(Chord('D6', '- 0 0 2 0 2', 1, Chord.HARD))
        self.add(Chord('D7', '- - 0 2 1 2', 1, Chord.EASY))
        self.add(Chord('D7#9', '- 2 1 2 3 3', 4, Chord.HARD))
        self.add(Chord('D7(#9)', '- 2 1 2 3 3', 4, Chord.HARD))
        self.add(Chord('D9', '1 3 1 2 1 3', 10, Chord.HARD))
        self.add(Chord('D11', '3 0 0 2 1 0', 1, Chord.HARD))
        self.add(Chord('Dsus', '- - 0 2 3 3', 1, Chord.HARD))
        self.add(Chord('Dsus2', '0 0 0 2 3 0', 1, Chord.HARD))
        self.add(Chord('Dsus4', '- - 0 2 3 3', 1, Chord.HARD))
        self.add(Chord('D7sus2', '- 0 0 2 1 0', 1, Chord.HARD))
        self.add(Chord('D7sus4', '- 0 0 2 1 3', 1, Chord.HARD))
        self.add(Chord('Dmaj', '- - 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('Dmaj7', '- - 0 2 2 2', 1, Chord.HARD))
        self.add(Chord('Ddim', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('Dmin', '- - 0 2 3 1', 1, Chord.EASY))
        self.add(Chord('D/A', '- 0 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D/B', '- 2 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D/C', '- 3 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D/C#', '- 4 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D/E', '- 1 1 1 1 -', 7, Chord.HARD))
        self.add(Chord('D/G', '3 - 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D5/E', '0 1 1 1 - -', 7, Chord.HARD))
        self.add(Chord('Dadd9', '0 0 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D(add9)', '0 0 0 2 3 2', 1, Chord.HARD))
        self.add(Chord('D9add6', '1 3 3 2 0 0', 10, Chord.HARD))
        self.add(Chord('D9(add6)', '1 3 3 2 0 0', 10, Chord.HARD))

        self.add(Chord('Dm', '- - 0 2 3 1', 1, Chord.EASY))
        self.add(Chord('Dm6(5b)', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('Dm7', '- - 0 2 1 1', 1, Chord.EASY))
        self.add(Chord('Dm#5', '- - 0 3 3 2', 1, Chord.HARD))
        self.add(Chord('Dm(#5)', '- - 0 3 3 2', 1, Chord.HARD))
        self.add(Chord('Dm#7', '- - 0 2 2 1', 1, Chord.HARD))
        self.add(Chord('Dm(#7)', '- - 0 2 2 1', 1, Chord.HARD))
        self.add(Chord('Dm/A', '- 0 0 2 3 1', 1, Chord.HARD))
        self.add(Chord('Dm/B', '- 2 0 2 3 1', 1, Chord.HARD))
        self.add(Chord('Dm/C', '- 3 0 2 3 1', 1, Chord.HARD))
        self.add(Chord('Dm/C#', '- 4 0 2 3 1', 1, Chord.HARD))
        self.add(Chord('Dm9', '- - 3 2 1 0', 1, Chord.HARD))

        self.add(Chord('D#', '- - 3 1 2 1', 3, Chord.HARD))
        self.add(Chord('D#+', '- - 1 0 0 4', 1, Chord.HARD))
        self.add(Chord('D#4', '- - 1 3 4 4', 1, Chord.HARD))
        self.add(Chord('D#7', '- - 1 3 2 3', 1, Chord.HARD))
        self.add(Chord('D#sus', '- - 1 3 4 4', 1, Chord.HARD))
        self.add(Chord('D#sus4', '- - 1 3 4 4', 1, Chord.HARD))
        self.add(Chord('D#maj', '- - 3 1 2 1', 3, Chord.HARD))
        self.add(Chord('D#maj7', '- - 1 3 3 3', 1, Chord.HARD))
        self.add(Chord('D#dim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('D#min', '- - 4 3 4 2', 1, Chord.HARD))
        self.add(Chord('D#m', '- - 4 3 4 2', 1, Chord.HARD))
        self.add(Chord('D#m7', '- - 1 3 2 2', 1, Chord.HARD))

        self.add(Chord('Eb', '- - 3 1 2 1', 3, Chord.HARD))
        self.add(Chord('Eb+', '- - 1 0 0 4', 1, Chord.HARD))
        self.add(Chord('Eb4', '- - 1 3 4 4', 1, Chord.HARD))
        self.add(Chord('Eb7', '- - 1 3 2 3', 1, Chord.HARD))
        self.add(Chord('Ebsus', '- - 1 3 4 4', 1, Chord.HARD))
        self.add(Chord('Ebsus4', '- - 1 3 4 4', 1, Chord.HARD))
        self.add(Chord('Ebmaj', '- - 1 3 3 3', 1, Chord.HARD))
        self.add(Chord('Ebmaj7', '- - 1 3 3 3', 1, Chord.HARD))
        self.add(Chord('Ebdim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('Ebadd9', '- 1 1 3 4 1', 1, Chord.HARD))
        self.add(Chord('Eb(add9)', '- 1 1 3 4 1', 1, Chord.HARD))
        self.add(Chord('Ebmin', '- - 4 3 4 2', 1, Chord.HARD))
        self.add(Chord('Ebm', '- - 4 3 4 2', 1, Chord.HARD))
        self.add(Chord('Ebm7', '- - 1 3 2 2', 1, Chord.HARD))

        self.add(Chord('E', '0 2 2 1 0 0', 1, Chord.EASY))
        self.add(Chord('E+', '- - 2 1 1 0', 1, Chord.HARD))
        self.add(Chord('E5', '0 1 3 3 - -', 7, Chord.HARD))
        self.add(Chord('E6', '- - 3 3 3 3', 9, Chord.HARD))
        self.add(Chord('E7', '0 2 2 1 3 0', 1, Chord.EASY))
        self.add(Chord('E7#9', '0 2 2 1 3 3', 1, Chord.HARD))
        self.add(Chord('E7(#9)', '0 2 2 1 3 3', 1, Chord.HARD))
        self.add(Chord('E7(5b)', '- 1 0 1 3 0', 1, Chord.HARD))
        self.add(Chord('E7b9', '0 2 0 1 3 2', 1, Chord.HARD))
        self.add(Chord('E7(b9)', '0 2 0 1 3 2', 1, Chord.HARD))
        self.add(Chord('E7(11)', '0 2 2 2 3 0', 1, Chord.HARD))
        self.add(Chord('E9', '1 3 1 2 1 3', 1, Chord.HARD))
        self.add(Chord('E11', '1 1 1 1 2 2', 1, Chord.HARD))
        self.add(Chord('Esus', '0 2 2 2 0 0', 1, Chord.HARD))
        self.add(Chord('Esus4', '0 2 2 2 0 0', 0, Chord.HARD))
        self.add(Chord('Emaj', '0 2 2 1 0 0', 1, Chord.HARD))
        self.add(Chord('Emaj7', '0 2 1 1 0 -', 1, Chord.HARD))
        self.add(Chord('Edim', '- - 2 3 2 3', 1, Chord.HARD))
        self.add(Chord('Emin', '0 2 2 0 0 0', 1, Chord.HARD))

        self.add(Chord('Em', '0 2 2 0 0 0', 1, Chord.EASY))
        self.add(Chord('Em6', '0 2 2 0 2 0', 1, Chord.HARD))
        self.add(Chord('Em7', '0 2 2 0 3 0', 1, Chord.EASY))
        self.add(Chord('Em/B', '- 2 2 0 0 0', 1, Chord.HARD))
        self.add(Chord('Em/D', '- - 0 0 0 0', 1, Chord.HARD))
        self.add(Chord('Em7/D', '- - 0 0 0 0', 1, Chord.HARD))
        self.add(Chord('Emsus4', '0 0 2 0 0 0', 1, Chord.HARD))
        self.add(Chord('Em(sus4)', '0 0 2 0 0 0', 1, Chord.HARD))
        self.add(Chord('Emadd9', '0 2 4 0 0 0', 1, Chord.HARD))
        self.add(Chord('Em(add9)', '0 2 4 0 0 0', 1, Chord.HARD))

        self.add(Chord('F', '1 3 3 2 1 1', 1, Chord.EASY))
        self.add(Chord('F+', '- - 3 2 2 1', 1, Chord.HARD))
        self.add(Chord('F+7+11', '1 3 3 2 0 0', 1, Chord.HARD))
        self.add(Chord('F4', '- - 3 3 1 1', 1, Chord.HARD))
        self.add(Chord('F6', '- 3 3 2 3 -', 1, Chord.HARD))
        self.add(Chord('F7', '1 3 1 2 1 1', 1, Chord.EASY))
        self.add(Chord('F9', '2 4 2 3 2 4', 1, Chord.HARD))
        self.add(Chord('F11', '1 3 1 3 1 1', 1, Chord.HARD))
        self.add(Chord('Fsus', '- - 3 3 1 1', 1, Chord.HARD))
        self.add(Chord('Fsus4', '- - 3 3 1 1', 1, Chord.HARD))
        self.add(Chord('Fmaj', '1 3 3 2 1 1', 1, Chord.HARD))
        self.add(Chord('Fmaj7', '- 3 3 2 1 0', 1, Chord.HARD))
        self.add(Chord('Fdim', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('Fmin', '1 3 3 1 1 1', 1, Chord.EASY))
        self.add(Chord('F/A', '- 0 3 2 1 1', 1, Chord.HARD))
        self.add(Chord('F/C', '- - 3 2 1 1', 1, Chord.HARD))
        self.add(Chord('F/D', '- - 0 2 1 1', 1, Chord.HARD))
        self.add(Chord('F/G', '3 3 3 2 1 1', 1, Chord.HARD))
        self.add(Chord('F7/A', '- 0 3 0 1 1', 1, Chord.HARD))
        self.add(Chord('Fmaj7/A', '- 0 3 2 1 0', 1, Chord.HARD))
        self.add(Chord('Fmaj7/C', '- 3 3 2 1 0', 1, Chord.HARD))
        self.add(Chord('Fmaj7(+5)', '- - 3 2 2 0', 1, Chord.HARD))
        self.add(Chord('Fadd9', '3 0 3 2 1 1', 1, Chord.HARD))
        self.add(Chord('F(add9)', '3 0 3 2 1 1', 1, Chord.HARD))
        self.add(Chord('FaddG', '1 - 3 2 1 3', 1, Chord.HARD))
        self.add(Chord('FaddG', '1 - 3 2 1 3', 1, Chord.HARD))

        self.add(Chord('Fm', '1 3 3 1 1 1', 1, Chord.EASY))
        self.add(Chord('Fm6', '- - 0 1 1 1', 1, Chord.HARD))
        self.add(Chord('Fm7', '1 3 1 1 1 1', 1, Chord.EASY))
        self.add(Chord('Fmmaj7', '- 3 3 1 1 0', 1, Chord.HARD))

        self.add(Chord('F#', '2 4 4 3 2 2', 1, Chord.EASY))
        self.add(Chord('F#+', '- - 4 3 3 2', 1, Chord.HARD))
        self.add(Chord('F#7', '- - 4 3 2 0', 1, Chord.EASY))
        self.add(Chord('F#9', '- 1 2 1 2 2', 1, Chord.HARD))
        self.add(Chord('F#11', '2 4 2 4 2 2', 1, Chord.HARD))
        self.add(Chord('F#sus', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('F#sus4', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('F#maj', '2 4 4 3 2 2', 0, Chord.HARD))
        self.add(Chord('F#maj7', '- - 4 3 2 1', 1, Chord.HARD))
        self.add(Chord('F#dim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('F#min', '2 4 4 2 2 2', 1, Chord.EASY))
        self.add(Chord('F#/E', '0 4 4 3 2 2', 1, Chord.HARD))
        self.add(Chord('F#4', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('F#m', '2 4 4 2 2 2', 1, Chord.EASY))
        self.add(Chord('F#m6', '- - 1 2 2 2', 1, Chord.HARD))
        self.add(Chord('F#m7', '- - 2 2 2 2', 1, Chord.EASY))
        self.add(Chord('F#m7-5', '1 0 2 3 3 3', 2, Chord.HARD))
        self.add(Chord('F#m/C#m', '- - 4 2 2 2', 1, Chord.HARD))

        self.add(Chord('Gb', '2 4 4 3 2 2', 1, Chord.EASY))
        self.add(Chord('Gb+', '- - 4 3 3 2', 1, Chord.HARD))
        self.add(Chord('Gb7', '- - 4 3 2 0', 1, Chord.EASY))
        self.add(Chord('Gb9', '- 1 2 1 2 2', 1, Chord.HARD))
        self.add(Chord('Gbsus', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('Gbsus4', '- - 4 4 2 2', 1, Chord.HARD))
        self.add(Chord('Gbmaj', '2 4 4 3 2 2', 1, Chord.HARD))
        self.add(Chord('Gbmaj7', '- - 4 3 2 1', 1, Chord.HARD))
        self.add(Chord('Gbdim', '- - 1 2 1 2', 1, Chord.HARD))
        self.add(Chord('Gbmin', '2 4 4 2 2 2', 1, Chord.HARD))
        self.add(Chord('Gbm', '2 4 4 2 2 2', 1, Chord.EASY))
        self.add(Chord('Gbm7', '- - 2 2 2 2', 1, Chord.HARD))

        self.add(Chord('G', '3 2 0 0 0 3', 1, Chord.EASY))
        self.add(Chord('G+', '- - 1 0 0 4', 1, Chord.HARD))
        self.add(Chord('G4', '- - 0 0 1 3', 1, Chord.HARD))
        self.add(Chord('G6', '3 - 0 0 0 0', 1, Chord.HARD))
        self.add(Chord('G7', '3 2 0 0 0 1', 1, Chord.EASY))
        self.add(Chord('G7+', '- - 4 3 3 2', 1, Chord.HARD))
        self.add(Chord('G7b9', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('G7(b9)', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('G7#9', '1 3 - 2 4 4', 3, Chord.HARD))
        self.add(Chord('G7(#9)', '1 3 - 2 4 4', 3, Chord.HARD))
        self.add(Chord('G9', '3 - 0 2 0 1', 1, Chord.HARD))
        self.add(Chord('G9(11)', '1 3 1 3 1 3', 3, Chord.HARD))
        self.add(Chord('G11', '3 - 0 2 1 1', 1, Chord.HARD))
        self.add(Chord('Gsus', '- - 0 0 1 3', 1, Chord.HARD))
        self.add(Chord('Gsus4', '- - 0 0 1 1', 1, Chord.HARD))
        self.add(Chord('G6sus4', '0 2 0 0 1 0', 1, Chord.HARD))
        self.add(Chord('G6(sus4)', '0 2 0 0 1 0', 1, Chord.HARD))
        self.add(Chord('G7sus4', '3 3 0 0 1 1', 1, Chord.HARD))
        self.add(Chord('G7(sus4)', '3 3 0 0 1 1', 1, Chord.HARD))
        self.add(Chord('Gmaj', '3 2 0 0 0 3', 1, Chord.HARD))
        self.add(Chord('Gmaj7', '- - 4 3 2 1', 2, Chord.HARD))
        self.add(Chord('Gmaj7sus4', '- - 0 0 1 2', 1, Chord.HARD))
        self.add(Chord('Gmaj9', '1 1 4 1 2 1', 2, Chord.HARD))
        self.add(Chord('Gmin', '1 3 3 1 1 1', 3, Chord.EASY))
        self.add(Chord('Gdim', '- - 2 3 2 3', 1, Chord.HARD))
        self.add(Chord('Gadd9', '1 3 - 2 1 3', 3, Chord.HARD))
        self.add(Chord('G(add9)', '1 3 - 2 1 3', 3, Chord.HARD))
        self.add(Chord('G/A', '- 0 0 0 0 3', 1, Chord.HARD))
        self.add(Chord('G/B', '- 2 0 0 0 3', 1, Chord.HARD))
        self.add(Chord('G/D', '- 2 2 1 0 0', 4, Chord.HARD))
        self.add(Chord('G/F#', '2 2 0 0 0 3', 1, Chord.HARD))

        self.add(Chord('Gm', '1 3 3 1 1 1', 3, Chord.EASY))
        self.add(Chord('Gm6', '- - 2 3 3 3', 1, Chord.HARD))
        self.add(Chord('Gm7', '1 3 1 1 1 1', 3, Chord.EASY))
        self.add(Chord('Gm/Bb', '3 2 2 1 - -', 4, Chord.HARD))

        self.add(Chord('G#', '1 3 3 2 1 1', 4, Chord.EASY))
        self.add(Chord('G#+', '- - 2 1 1 0', 1, Chord.HARD))
        self.add(Chord('G#4', '1 3 3 1 1 1', 4, Chord.HARD))
        self.add(Chord('G#7', '- - 1 1 1 2', 1, Chord.EASY))
        self.add(Chord('G#sus', '- - 1 1 2 4', 1, Chord.HARD))
        self.add(Chord('G#sus4', '- - 1 1 2 4', 1, Chord.HARD))
        self.add(Chord('G#maj', '1 3 3 2 1 1', 4, Chord.HARD))
        self.add(Chord('G#maj7', '- - 1 1 1 3', 1, Chord.HARD))
        self.add(Chord('G#dim', '- - 0 1 0 1', 1, Chord.HARD))
        self.add(Chord('G#min', '1 3 3 1 1 1', 4, Chord.HARD))
        self.add(Chord('G#m', '1 3 3 1 1 1', 4, Chord.EASY))
        self.add(Chord('G#m6', '- - 1 1 0 1', 1, Chord.HARD))
        self.add(Chord('G#m7', '- - 1 1 1 1', 4, Chord.EASY))
        self.add(Chord('G#m9maj7', '- - 1 3 0 3', 1, Chord.HARD))
        self.add(Chord('G#m9(maj7)', '- - 1 3 0 3', 1, Chord.HARD))


    def add(self, chord):

        self.chords[chord.name] = chord
                           
                 
