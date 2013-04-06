#!/usr/bin/env python
"""ChordPro Parser"""

from songbook import Songbook
from parser import *
from tex_visitor import *

if __name__ == '__main__':
    import codecs, argparse, sys, os.path

    parser = argparse.ArgumentParser(description="Chordpro songbook")

    parser.add_argument('filename')
    parser.add_argument('--output', default="-")

    args = parser.parse_args()

    file = codecs.open(args.filename, encoding='utf-8')
    out = open(args.output, "w") if args.output != "-" else sys.stdout

    dirname = os.path.dirname(args.filename)

    songbook = Songbook(file)

    for song in songbook.songs:

        file = codecs.open(os.path.join(dirname, song), encoding='utf-8') 
        parsed = parse(file)

        out.write(show(parsed, TexVisitor, template='song_template.tex'))
        

        


