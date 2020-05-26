from SupportClasses.WordEmbedder import WordEmbedder
import numpy as np
import en_core_web_md
import pickle


class WordEmbedderSpacy(WordEmbedder):
    def __init__(self):
        self.spacyProcessor = self.__loadWordEmbedding()
        # self.spacyProcessor = self.__loadSpacyPickle()

    def __loadWordEmbedding(self):
        print('Loading Spacy Word Embeddings...')
        spc = en_core_web_md.load()
        print('Spacy Word Embeddings loaded.')
        return spc

    def __loadSpacyPickle(self):
        print('Reading spacy.pckl')
        f = open('spacy.pckl', 'rb')
        item = pickle.load(f)
        f.close()
        return item

    def __handleUnknown(self, token):
        print('Unknown word:', token.text)
        subWordVectors = []
        for char in token.text:
            # tokenise
            charToken = self.spacyProcessor(char)[0]
            charVector = charToken.vector

            subWordVectors.append(charVector)

        # add all vector
        subWordSum = np.zeros(len(subWordVectors[0]))
        for vec in subWordVectors:
            subWordSum = np.add(
                subWordSum, vec)

        return subWordSum.astype(np.float32)

    def getVector(self, word):
        word = word.lower()

        token = self.spacyProcessor(word)[0]

        if(token.has_vector):
            print('Vector present.')
            return token.vector

        else:
            # if word not found
            return self.__handleUnknown(token)
