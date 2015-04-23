import dice
import argparse
import string
import re

def is_valid_roll(roll):
	"""use a cute regex to validate rolls"""
	return re.match('^\d*d\d+([+-]\d+)?$', roll) is not None

def handleRoll(roll):
	if(not is_valid_roll(roll)):
		print "roll not valid must be in the form of [N]dN[(+-)N]"
		return

	(times, roll) = string.split(roll, 'd', 1)
	times = int(times)
	if '-' in roll:
		(faces, modifier) = string.split(roll, '-', 1)
		modifier = - int(modifier)
	elif '+' in roll:
		(faces, modifier) = string.split(roll, '+', 1)
		modifier = int(modifier)
	else:
		faces = int(roll)
		modifier = 0
	die = dice.Die(int(faces))

	rolls = [die.roll() for x in xrange(0,times)]

	print "rolls: %s; total %s" % (rolls, sum(rolls) + modifier)

def main():
	#using argparse, which for now will not have much in the way of advantages, but provides flexibility in the future
	parser = argparse.ArgumentParser(description='Roll some dice.')
	parser.add_argument('rolls', metavar='roll', nargs='+', help='define a diceroll')

	args = parser.parse_args()

	for roll in args.rolls:
		handleRoll(roll)

if __name__ == '__main__':
	main()