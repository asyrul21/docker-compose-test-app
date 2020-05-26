from SupportClasses.WordEmbedderSpacy import WordEmbedderSpacy
import unittest
import numpy as np


class TestWordEmbedderSpacy(unittest.TestCase):
    def test_tokenTextType(self):
        word = 'hello'

        wes = WordEmbedderSpacy()
        token = wes.spacyProcessor(word)[0]

        print('Token:', token)
        print('Type:', type(token))
        self.assertEqual(type(token.text), str)

    def test_getVectorType(self):
        word = 'hello'

        wes = WordEmbedderSpacy()
        vector = wes.getVector(word)

        print('Vector Type:', type(vector))
        self.assertEqual(type(vector), np.ndarray)

    # def test_getVectorShape(self):
    #     word = 'hello'

    #     wes = WordEmbedderSpacy()
    #     vector = wes.getVector(word)

    #     print('Shape:', vector.shape)
    #     self.assertEqual(vector.shape, (300,))

    # def test_getVectorElementType(self):
    #     word = 'hello'

    #     wes = WordEmbedderSpacy()
    #     vector = wes.getVector(word)

    #     self.assertEqual(type(vector[0]), np.float32)

    # # unknown word
    # def test_getVectorForKUnknownType(self):
    #     word = 'wazzap'

    #     wes = WordEmbedderSpacy()
    #     vector = wes.getVector(word)

    #     self.assertEqual(type(vector[0]), np.float32)

    # def test_getVectorForKUnknownNot0(self):
    #     word = 'wazzap'

    #     wes = WordEmbedderSpacy()
    #     vector = wes.getVector(word)

    #     print('Unknown word vector:')
    #     print(vector)
    #     self.assertTrue(vector.all(), not 0)

    # def test_getVectorForKUnknownShape(self):
    #     word = 'wazzap'

    #     wes = WordEmbedderSpacy()
    #     vector = wes.getVector(word)

    #     print('Unknown word shape:', vector.shape)
    #     self.assertEqual(vector.shape, (300,))
