import unittest
import fizzbuzz
import io
import sys

class TestCase(unittest.TestCase):
	def testNum(self):
		output = io.StringIO()
		sys.stdout = output
		fizzbuzz.fizzbuzz();
		self.assertEqual(output.getvalue(), "Buzz\n1\n2\n3\n4\nBuzz\n6\n7\n8\n9\nBuzz\n11\n12\n13\n14\nBuzz\n16\n17\n18\n19\nBuzz\n21\n22\n23\n24\nBuzz\n26\n27\n28\n29\nBuzz\n31\n32\n33\n34\nBuzz\n36\n37\n38\n39\nBuzz\n41\n42\n43\n44\nBuzz\n46\n47\n48\n49\nBuzz\n51\n52\n53\n54\nBuzz\n56\n57\n58\n59\nBuzz\n61\n62\n63\n64\nBuzz\n66\n67\n68\n69\nBuzz\n71\n72\n73\n74\nBuzz\n76\n77\n78\n79\nBuzz\n81\n82\n83\n84\nBuzz\n86\n87\n88\n89\nBuzz\n91\n92\n93\n94\nBuzz\n96\n97\n98\n99\n")
		sys.stdout = sys.__stdout__

if __name__ == '__main__':
	unittest.main()