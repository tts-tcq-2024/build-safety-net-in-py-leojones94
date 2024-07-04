import unittest
from soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    
    def test_no_argument(self):
        self.assertEqual(generate_soundex(), "")

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_vowel_separated_character(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    
if __name__ == '__main__':
    unittest.main()
