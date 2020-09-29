from random import randint
import numpy
from random import shuffle

class Opgave:
    def __init__(self):
        self.h1 = randint(1,10)
        self.h2 = randint(1,10)
        self.facit = numpy.round(self.h1/self.h2, 2)
        self.tekst = "En maskine arbejder med en hastighed på {} enheder per sekund. Den anden maskine arbejder med en hastighed på {} per sekund. Hvad er den optimale ratio mellem de to maskiner? (to decimaler)".format(self.h1, self.h2)
        self.svar1 = numpy.round(randint(1,10)/randint(1,10), 2)
        self.svar2 = numpy.round(randint(1,10)/randint(1,10), 2)
        self.svar_liste = []
        self.svar_liste.append(self.facit)
        self.svar_liste.append(self.svar1)
        self.svar_liste.append(self.svar2)
        shuffle(self.svar_liste)
