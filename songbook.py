from tex_visitor import _MyTemplate

class Songbook(object):

    def __init__(self, file):

        self._titlestyle = None
        self._columns = 1
        self._songbooktitle = ''
        self._subtitles = True
        self._toc = False
        self.songs = []
        
        self.parse(file)

        self._template = _MyTemplate(open('songbook_template.tex').read())


    def parse_directive(self, line):

        import sys

        line = line.strip('{} ')
        s = line.split(':', 1)
        
        directives = {'titlestyle', 'columns', 'songbooktitle', 'toc', 
                      'subtitles_on',  'subtitles_off'}

        d = s[0].strip()

        # Parse chordpack directives.
        if d == 'titlestyle':
            self._titlestyle = s[1]
        elif d == 'columns':
            self._columns = s[1]
        elif d == 'songbooktitle':
            self._songbooktitle = s[1].replace('^', '\\\\\n')
        elif d == 'toc':
            self._toc = True
        elif d == 'subtitles_on':
            self._subtitles = True
        elif d == 'subtitles_off':
            self._subtitles = False
        else:
            sys.stderr.write('Unknown directive: ' + d + '\n')
        

    def parse_line(self, line):

        line = line.strip()            
        if line == '' or line[0] == '#':
            return

        if line[0] == '{':
            self.parse_directive(line)
        else:
            self.songs.append(line)


    def parse(self, file):

        for line in file.readlines():

            self.parse_line(line)
        

    def make(self, text):

        return self._template.substitute(
            title=self._songbooktitle,
            songs=text)

        


        
