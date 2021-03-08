import unittest
import leapyear

class TestCase(unittest.TestCase):
	def testLY(self):
		self.assertEqual(leapyear.leapyear(4), True);
		self.assertEqual(leapyear.leapyear(5), False);

if __name__ == '__main__':
	unittest.main()