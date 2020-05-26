from .GloveLoader import GloveLoader
import numpy as np

import sys


class WordEmbedder:
    def __init__(self):
        self.gloveDictionary = self.__loadWordEmbedding()
        print('Size of Glove Dictionary:',
              (sys.getsizeof(self.gloveDictionary) / 1000000), 'MB')

    def __loadWordEmbedding(self):
        GL = GloveLoader()
        return GL.getGloveDictionary()

    def getVector(self, word):
        word = word.lower()
        if(word in self.gloveDictionary):
            # return np.asarray(self.gloveDictionary[word]).astype(np.float)
            return self.gloveDictionary[word]
        else:  # if word not found
            print('Unknown word:', word)
            subWordVectors = []
            for sub in word:
                # subWordVectors.append(np.asarray(
                    # self.gloveDictionary[sub]).astype(np.float))
                subWordVectors.append(self.gloveDictionary[sub])

            # add all vector
            subWordSum = np.zeros(len(subWordVectors[0]))
            for vec in subWordVectors:
                # print(np.asarray(vec.astype(np.float)))
                subWordSum = np.add(
                    subWordSum, np.asarray(vec.astype(np.float)))

            return subWordSum
