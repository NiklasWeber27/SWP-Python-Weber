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
        self.assertTrue(Pokersimulator.ispair([0, 0]))
        self.assertFalse(Pokersimulator.ispair([0, 1, 2]))

    def test_istwopairs(self):
        self.assertTrue(Pokersimulator.istwopairs([0, 13, 0, 13]))
        self.assertFalse(Pokersimulator.istwopairs([0, 1, 2, 3]))

    def test_isdrilling(self):
        self.assertTrue(Pokersimulator.isdrilling([0, 0, 0]))
        self.assertFalse(Pokersimulator.isdrilling([0, 1, 2]))

    def test_isstraight(self):
        self.assertTrue(Pokersimulator.isstraight([0, 1, 2, 3, 4]))
        self.assertFalse(Pokersimulator.isstraight([0, 1, 2, 3, 5]))

    def test_isflush(self):
        self.assertTrue(Pokersimulator.isflush([0, 0, 0, 0, 0]))
        self.assertFalse(Pokersimulator.isflush([0, 0, 0, 0, 1]))

    def test_isfullhouse(self):
        self.assertTrue(Pokersimulator.isfullhouse([0, 0, 0, 1, 1]))
        self.assertFalse(Pokersimulator.isfullhouse([0, 1, 2, 3, 4]))

    def test_isvierling(self):
        self.assertTrue(Pokersimulator.isvierling([0, 0, 0, 0]))
        self.assertFalse(Pokersimulator.isvierling([0, 1, 2, 3, 4]))

    def test_isstraightflush(self):
        self.assertTrue(Pokersimulator.isstraightflush([0, 1, 2, 3, 4], [0, 0, 0, 0, 0]))
        self.assertFalse(Pokersimulator.isstraightflush([0, 1, 2, 3, 5], [0, 0, 0, 0, 0]))

    def test_isroyalflush(self):
        self.assertTrue(Pokersimulator.isroyalflush([8, 9, 10, 11, 12], [0, 0, 0, 0, 0]))
        self.assertFalse(Pokersimulator.isroyalflush([0, 1, 2, 3, 4], [0, 0, 0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
