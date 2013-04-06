#!/usr/bin/env python
"""ChordPro Parser"""

from songbook import Songbook

if __name__ == '__main__':
    import codecs, argparse, sys

    parser = argparse.ArgumentParser(description="Chordpro songbook")

    parser.add_argument('filename')
    parser.add_argument('--format', default="ascii")
    parser.add_argument('--output', default="-")

    args = parser.parse_args()

    file = codecs.open(args.filename, encoding='utf-8')
    out = open(args.output, "w") if args.output != "-" else sys.stdout

    songbook = Songbook(file)
    print songbook.songs
