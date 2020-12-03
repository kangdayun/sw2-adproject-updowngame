import unittest

from numtry import Numtry

class TestNumtry(unittest.TestCase):

    def setUp(self):
        self.numA = Numtry('0')
        self.numB = Numtry('999')
        self.numC = Numtry('500')
        self.updownA = Numtry('Up')
        self.updownB = Numtry('Down')

    def tearDown(self):
        pass

    def testNumtry(self):
        self.numA.numtry('0')
        self.assertIn('0', self.numA.recordNums)
        self.numB.numtry('999')
        self.assertIn('999', self.numB.recordNums)
        self.numC.numtry('500')
        self.assertIn('500', self.numC.recordNums)

    def testGetRecordNums(self):
        self.numA.numtry('0')
        self.assertEqual(self.numA.getRecordNums(), '0')
        self.numB.numtry('999')
        self.assertEqual(self.numB.getRecordNums(), '999')
        self.numC.numtry('500')
        self.assertEqual(self.numC.getRecordNums(), '500')

    def testUpdownTry(self):
        self.updownA.updownTry('Up')
        self.assertIn('Up', self.updownA.recordUpdowns)
        self.updownB.updownTry('Down')
        self.assertIn('Down', self.updownB.recordUpdowns)

    def testGetRecordUpdown(self):
        self.updownA.updownTry('Up')
        self.assertEqual(self.updownA.getRecordUpdown(), '*** Up & Down Record ***\nUp')
        self.updownB.updownTry('Down')
        self.assertEqual(self.updownB.getRecordUpdown(), '*** Up & Down Record ***\nDown')

    def testFinishes(self):
        self.numA.numtry('0')
        self.assertTrue(self.numA.finished())
        self.numB.numtry('999')
        self.assertTrue(self.numB.finished())
        self.numC.numtry('500')
        self.assertTrue(self.numC.finished())


if __name__ == '__main__':
    unittest.main()
