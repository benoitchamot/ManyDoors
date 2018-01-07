from Items import *

class Room():

	chests = []
	creatures = []

	def __init__(self, chests, creatures):
		for each_chest in chests:
			self.chests.append(each_chest)

		for each_creature in creatures:	
			self.creatures.append(each_creature)
