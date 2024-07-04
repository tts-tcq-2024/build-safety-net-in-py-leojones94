import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    
    def test_no_argument(self):
        self.assertEqual(generate_soundex(), "")

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_adjacent_same_number_character(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_h_separated_character(self):
        self.assertEqual(generate_soundex("BHP"), "B000")

    def test_w_separated_character(self):
        self.assertEqual(generate_soundex("BWP"), "B000")

    def test_vowel_separated_character(self):
        self.assertEqual(generate_soundex("BAP"), "B100")

    
if __name__ == '__main__':
    unittest.main()
