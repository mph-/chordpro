# -*- encoding: utf-8

from string import Template
from chord import Chord
from chords import Chords

def indicate_last(iterable):
    i = 0
    l = len(iterable)
    for x in iterable:
        i += 1
        yield i == l, x

class _MyTemplate(Template):
    delimiter = "§"

class TexVisitor(object):
    def __init__(self, template=None):

        if not template:
            template = "template.tex"
        template = open(template).read()
        self._result = []
        self._template = _MyTemplate(template)
        self._title = ""
        self._subtitle = ""
        self._intab = False
        self._chords = Chords()
        self._used_chords = []

    def visit_d(self, text):
        import sys

        c = text.split(' ', 1)
        chordname = c[0]

        c = c[1].split(' ', 3)
        if c[0] != 'base-fret' or c[2] != 'frets':
            sys.stderr.write('Invalid define format: ' + text + '\n')

        self._chords.add(Chord(chordname, c[3], c[1]))

    def visit_t(self, title):
        self._title = title

    def visit_st(self, subtitle):
        self._subtitle = subtitle

    def visit_c(self, comment):
        self._result.append("\\textbf{%s}\\\\" % comment)
    
    def visit_ci(self, comment):
        self._result.append("\\textit{%s}" % comment)

    def visit_soc(self):
        self._result.append("\\textbf{Chorus}\\begin{textit}")

    def visit_eoc(self):
        self._result.append("\\end{textit}")

    def visit_nl(self):
        self._result.append("")

    def visit_line(self, chords):
        line = []
        for last, (chord, text) in indicate_last(chords):
            if chord is None:
                line.append(text)
            else:

                if chord not in ('/', 'N.C.') and chord not in self._used_chords:
                    self._used_chords.append(chord)

                if text.isspace() or len(text) == 0:
                    line.append("\showchord{%s}%s" %
                            (chord + "|", "{ }" * len(text))
                            )
                    if last:
                        line.append('\ ')

                else:
                    if len(chord) >= len(text.strip()):
                        if not text[-1].isspace():
                            if not last:
                                chord += "_"
                                text = "{%s}" % text
                        else:
                            chord += "|"
                            text = "{%s}" % text

                    line.append("\showchord{%s}%s" % (chord, text))

        self._result.append("".join(line) + ('' if self._intab else '\\\\'))

    def result(self):

        chords = '\n'.join([self._chords.find(chordname).format() for chordname in self._used_chords]) + '\n'

        return self._template.substitute(
               block="\n".join(self._result),
               title=self._title,
               subtitle=self._subtitle,
               diagrams="",
               chords=chords
               )

