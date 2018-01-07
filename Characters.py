import random

def d6(nb, mod):
	score = mod
	
	for i in range(0,nb):
		score = score + random.randint(1,6)
		
	return score

class Item():
	def __init__(self, name, type, value, weight):
		self.name = name
		self.type = type
		self.value = value
		self.weight = weight
		
class Weapon(Item):
	def __init__(self, name, type, value, weight, attack):
		self.name = name
		self.type = type
		self.value = value
		self.weight = weight
		self.attack = attack
		
class Shield(Item):
	def __init__(self, name, type, value, weight, armor):
		self.name = name
		self.type = type
		self.value = value
		self.weight = weight
		self.armor = armor
		
class Character:
	armor = 0
	
	dead = False
	
	dexterity = 0
	strength = 0
	charisma = 0
	intelligence = 0
	dodge = 3
	
	def __init__(self, name, level, race):
		self.name = name
		self.level = level
		self.race = race
		
		self.health = d6(3,self.strength)
		
		# The basic character fights with his fists
		fists = Weapon("Fists", "Basic", 0, 0, 0)
		self.equiped_weapon = fists
		no_shield = Shield("None", "Basic", 0, 0, 0)
		self.equiped_shield = no_shield
		
	def get_damage(self, damage):
		# Armor always protects the character
		self.health = self.armor + self.health - damage
		
		if self.health < 0:
			self.health = 0
			self.dead = True
		
	def display(self):
		print(self.name + " the " + self.race)
		print("Level " + str(self.level))
		
	def fight(self, Ennemy):
		# Self attacks Ennemy with equipped weapon
		# Ennemy defends with Dodge and/or Shield
		# Ennemy loses Armor and Health accordingly
		
		# First only assume melee weapons (strength)
		strength = self.strength + self.equiped_weapon.attack
		
		# Throw three dice, must be higher than ennemy's dodge abilities
		if d6(3,0) > Ennemy.dodge:
			print(Ennemy.name + " loses " + str(strength) + " health. " + str(Ennemy.health) + " remaining.")
			Ennemy.get_damage(strength)
		else:
			print("Miss!")
	
class Hero(Character):
	
	# Inventory
	weapons = []
	objects = []
	potions = 0
	gold = 0
	
	def display_armor(self):
		print(self.armor)
		
	def weight_inventory(self):
		weight = 0
		for i in range (0, len(self.weapons)):
			weight = weight + self.weapons[i].weight
		for i in range(0, len(self.objects)):
			weight = weight + self.objects[i].weight
			
		if self.equiped_shield:
			weight = weight + self.equiped_shield.weight
			
		return weight
		
	def loot(self, gold, potions, items):
		# Add gold to gold count
		# Add potions to potions count
		# Add Items (list of objects) to inventory
		self.gold = self.gold + gold
		
		self.potions = self.potions + potions
		
		for i in range(0, len(items)):
			if items[i].type is 'weapon':
				self.weapons.append(items[i])
			else:
				self.objects.append(items[i])
				
	def show_inventory(self):
		print("Inventory")
		print("---------")
		print("Gold: " + str(self.gold))
		print("Potions: " + str(self.potions))
		print("---------")
		
		for i in range (0, len(self.weapons)):
			print(self.weapons[i].name)
			
		print("---------")
		for i in range (0, len(self.objects)):
			print(self.objects[i].name)
			
		print("=========")
		print(str(self.weight_inventory()) + " kg")
		
	def store_weapon(self):
		# Remove currently equipped weapon
		# Remove bonus/malus from weapon
		pass
		
	def equip_weapon(self, weapon):
		# Equip Weapon
		# Add bonus/malus from weapon
		self.equiped_weapon = weapon
		
	def change_weapon(self, weapon):
		self.store_weapon()
		self.equip_weapon(weapon)
		
	def drink_potion(self):
		# Remove potion from inventory (if possible)
		# Increase health
		if self.potions > 0:
			self.potions = self.potions - 1
			self.health = self.health + 10
			# To-do: add max health!
		
class Creature(Character):
	loot_gp = 12
	
	def display_loot(self):
		print(self.loot_gp)


