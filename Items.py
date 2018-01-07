
class Item():
	def __init__(self, name, type, value, weight, armor, bonus_armor):
		self.name = name
		self.type = type
		self.value = value
		self.weight = weight
		self.armor = armor
		self.bonus_armor = bonus_armor

class Weapon(Item):
	# Type of weapons: fists (d4), knives (d6), swords (d12), longswords (d20)
	# Levels: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

	def __init__(self, name, type, value, weight, level):
		self.name = name
		self.type = type

		if type is 'fists':
			self.attack = 4
		elif type is 'knife':
			self.attack = 6
		elif type is 'sword':
			self.attack = 12
		elif type is 'longsword':
			self.attack = 20

		self.value = value
		self.weight = weight
		self.level = level

	def show_stats(self):
		print(self.name)
		print('  Type:   ' + self.type)
		print('  Level:  ' + str(self.level))
		print('  Damage: 1d' + str(self.attack) + '+' + str(self.level))
		print('  Weight: ' + str(self.weight) + ' kg')
		print('  Value:  ' + str(self.value) + ' GP')
		print(' ')

class Chest():
	def __init__(self, name, gold, potions, item):
		self.name = name
		self.gold = gold
		self.potions = potions
		self.item = item
