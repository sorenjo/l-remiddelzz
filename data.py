from random import randint
import numpy

class Opgave:
    def __init__(self):
        self.h1 = randint(1,10)
        self.h2 = randint(1,10)
        self.facit = numpy.round(self.h1/self.h2, 2)
        self.tekst = "En maskine arbejder med en hastighed på {} enheder per sekund. Den anden maskine arbejder med en hastighed på {} per sekund. Hvad er den optimale ratio mellem de to maskiner? (to decimaler)"
