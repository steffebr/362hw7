import unittest
import fizzbuzz
import io
import sys

class TestCase(unittest.TestCase):
	def testNum(self):
		output = io.StringIO()
		sys.stdout = output
		fizzbuzz.fizzbuzz();
		self.assertEqual(output.getvalue(), "Fizz\n1\n2\nFizz\n4\n5\nFizz\n7\n8\nFizz\n10\n11\nFizz\n13\n14\nFizz\n16\n17\nFizz\n19\n20\nFizz\n22\n23\nFizz\n25\n26\nFizz\n28\n29\nFizz\n31\n32\nFizz\n34\n35\nFizz\n37\n38\nFizz\n40\n41\nFizz\n43\n44\nFizz\n46\n47\nFizz\n49\n50\nFizz\n52\n53\nFizz\n55\n56\nFizz\n58\n59\nFizz\n61\n62\nFizz\n64\n65\nFizz\n67\n68\nFizz\n70\n71\nFizz\n73\n74\nFizz\n76\n77\nFizz\n79\n80\nFizz\n82\n83\nFizz\n85\n86\nFizz\n88\n89\nFizz\n91\n92\nFizz\n94\n95\nFizz\n97\n98\nFizz\n")
		sys.stdout = sys.__stdout__

if __name__ == '__main__':
	unittest.main()