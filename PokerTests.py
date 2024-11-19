import unittest
import Pokersimulator

class PokerTest(unittest.TestCase):
    def test_getcolor(self):
        self.assertEqual(Pokersimulator.getcolor(0, 13), 0)
        self.assertEqual(Pokersimulator.getcolor(51, 13), 3)

    def test_getnumber(self):
        self.assertEqual(Pokersimulator.getnumber(0, 13), 0)
        self.assertEqual(Pokersimulator.getnumber(51, 13), 12)

    def test_ispair(self):
        self.assertTrue(Pokersimulator.ispair([0, 13]))
        self.assertFalse(Pokersimulator.ispair([0, 1, 2]))

if __name__ == '__main__':
    unittest.main()
