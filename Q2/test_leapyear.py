import unittest
import leapyear

class TestCase(unittest.TestCase):
	def testLY(self):
		self.assertEqual(leapyear.leapyear(4), True);
		self.assertEqual(leapyear.leapyear(5), False);
		self.assertEqual(leapyear.leapyear(100), False);
		self.assertEqual(leapyear.leapyear(400), True);


if __name__ == '__main__':
	unittest.main()