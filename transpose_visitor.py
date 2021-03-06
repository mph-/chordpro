from note import *
from re import compile

class TransposeVisitor(object):
    chord_regex = compile(r"[A-G](?:#|b)?")

    def __init__(self, transpose):
        self._transpose = transpose
        self._result = []

    def visit(self, command, *args):
        self._result.append((command,) + args)

    def visit_line(self, chords):
        if self._transpose == 0:
            self._result.append(("line", chords))
        else:
            def do_transpose(chord):
                print chord
                if chord is None:
                    return None
                for c in self.chord_regex.findall(chord):
                    print c
                    n = note_to_number(c) + self._transpose
                    chord = chord.replace(c, number_to_note(n % 12))
                print chord
                return chord

            self._result.append(
                ("line", [
                    (do_transpose(chord), text)
                    for chord, text in chords
                    ]
                )
            )

    def result(self):
        return self._result
