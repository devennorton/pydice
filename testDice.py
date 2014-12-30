import unittest
import dice

class TestDice(unittest.TestCase):
	"""Test our dice class in a rather informal fassion"""
	
	def test_int_sided_die(self):
		"""Here we test dice with a simple integer number of facets.
		We create die with from 1 to 10 sides, and roll them each 1000 times, testing
		each roll to ensure it is within the expected range"""
		for sides in xrange(1,10):
			die = dice.Die(sides)
			for x in xrange(1,1000):
				rollvalue = die.roll()
				self.assertTrue(rollvalue <= sides and rollvalue >= 1, 
					msg="roll of %s is outside of range 1-%s" % (rollvalue, sides))

if __name__ == '__main__':
    unittest.main()