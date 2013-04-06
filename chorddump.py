#!/usr/bin/env python
"""ChordPro chord dump"""

from parser import *
from chords_dump import *

if __name__ == '__main__':
    import codecs, argparse, sys

    parser = argparse.ArgumentParser(description="Chordpro converter")

    parser.add_argument('filename')
    parser.add_argument('--format', default="simple")

    args = parser.parse_args()

    file = codecs.open(args.filename, encoding='utf-8')
    parsed = parse(file)

    sys.stdout.write(show(parsed, ChordsDump, frets=True, format=args.format))

