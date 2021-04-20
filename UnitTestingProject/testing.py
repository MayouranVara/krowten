import unittest
from main import search_algo
from main import matching
import pandas as pd

class MyTestCase(unittest.TestCase):
    def test_srch_algo(self):
        df = pd.read_excel("classeur.xlsx")
        question = 'java marketing'
        result = search_algo(df,question)
        tab = ['Onfroy', 'Jackson', 'McSkin', 'Paulusch', 'Gilogly']
        self.assertEqual(result,tab)

    def test_srch_algo_1(self):
        df = pd.read_excel("classeur.xlsx")
        question = 'java'
        result = search_algo(df,question)
        tab = ['Jackson']
        self.assertEqual(result,tab)

    def test_matching_1(self):
        test = matching('java','java')
        self.assertEqual(test,1)

    def test_matching(self):
        test = matching('java','jav')
        self.assertEqual(test,0)

if __name__ == '__main__':
    unittest.main()
