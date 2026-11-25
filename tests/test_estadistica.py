import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estadistica import media  # noqa: E402


class PruebasMedia(unittest.TestCase):
    def test_media_de_tres(self):
        self.assertEqual(media([1, 2, 3]), 2)

    def test_media_de_uno(self):
        self.assertEqual(media([5]), 5)

    def test_vacia_lanza_valueerror(self):
        with self.assertRaises(ValueError):
            media([])


if __name__ == "__main__":
    unittest.main()
