import numpy as np
import glob


class GloveLoader:
    def __init__(self, folder='GloveFiles/'):
        self.folder = folder
        self.gloveDict = {}

    def __readGloveMultiple(self):
        dictionary = {}
        # loop through all files in a folder
        print('Loading Glove word embeddings...')
        for file in glob.glob(self.folder + '*.txt'):
            # open each file
            with open(file, 'r', encoding="ISO-8859-1") as in_file:
                stripped = (line.strip() for line in in_file)

                for line in stripped:
                    if(line):
                        frags = line.split(' ')
                        word = frags[0]
                        # floatList = [float(n) for n in frags[1:]]
                        # cast to no array
                        # vector = np.asarray(floatList)

                        vector = frags[1:]
                        print('Vector:', vector)
                        print('type:', type(vector))
                        # insert into dictionary
                        dictionary.update({word: vector})

                if(not self.gloveDict):
                    self.gloveDict = dictionary

        print('Glove embeddings loaded.')

    # public
    def getGloveDictionary(self):
        if(not self.gloveDict):
            self.__readGloveMultiple()
            return self.gloveDict
        else:
            return self.gloveDict
