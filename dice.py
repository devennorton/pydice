import random

class Die(object):
	"""docstring for Dice"""
	def __init__(self, sides):
		super(Die, self).__init__()
		self.sides = sides
		
	def roll(self):
		return random.randint(1, self.sides)