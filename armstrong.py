import unittest


def is_armstrong(szam: int) -> bool:
    if szam < 0:
        return False

    szamjegyek = [int(c) for c in str(szam)]
    n = len(szamjegyek)

    return sum(jegy ** n for jegy in szamjegyek) == szam


class TestArmstrong(unittest.TestCase):

    def test_armstrong_szamok(self):
        self.assertTrue(is_armstrong(0))
        self.assertTrue(is_armstrong(1))
        self.assertTrue(is_armstrong(153))
        self.assertTrue(is_armstrong(370))
        self.assertTrue(is_armstrong(371))
        self.assertTrue(is_armstrong(9474))

    def test_nem_armstrong_szamok(self):
        self.assertFalse(is_armstrong(10))
        self.assertFalse(is_armstrong(100))
        self.assertFalse(is_armstrong(200))
        self.assertFalse(is_armstrong(9475))

    def test_negativ_szam(self):
        self.assertFalse(is_armstrong(-153))


if __name__ == "__main__":
    unittest.main()
