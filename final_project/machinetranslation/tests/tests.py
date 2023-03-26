import unittest
from ..translator import get_translator_instance, englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def setUp(self):
        self.translator = get_translator_instance()
    
    def test_words(self):
        self.assertEqual(englishToFrench(self.translator, 'Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(self.translator, 'World'), 'Monde')
        self.assertEqual(englishToFrench(self.translator, 'Hello world'), 'Bonjour le monde')

    def test_null(self):
        self.assertIsNone(englishToFrench(self.translator, ''), None)


class TestFrenchToEnglish(unittest.TestCase):
    def setUp(self):
        self.translator = get_translator_instance()
    
    def test1_words(self):
        self.assertEqual(frenchToEnglish(self.translator, 'Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(self.translator, 'Monde'), 'World')
        self.assertEqual(frenchToEnglish(self.translator, 'Bonjour le monde'), 'Hello World')
        
    def test_null(self):
        self.assertIsNone(frenchToEnglish(self.translator, ''), None)

unittest.main()
