"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, file):
        """ """
        self.file = file

        self.words = self.parse(file)

        self.count = len(self.words)

        print(f"{self.count} words read")


    def parse(self, filename):
        """ """
        file = open(filename, "r")
        out = []
        line = file.readline()
        while line:
            out.append(line.strip())
            line = file.readline()
        file.close()
        return out


    def random(self):
        """ """
        r = random.randrange(self.count)

        return self.words[r]
