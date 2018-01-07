import random
import time

from Items import *

def dice(nb, typ, mod):
	score = mod
	
	for i in range(0,nb):
		score = score + random.randint(1,typ)
		
	return score
		
class Character:
	dead = False
	
	# Main characteristics
	strength = 10
	dodge = 0.1
	# charisma = 0

	# Computed characteristics
	armor = 0

	# Inventory
	potions = 20
	gold = 0
	
	def __init__(self, name, level, race):
		self.name = name
		self.level = level
		self.race = race
		
		self.max_health = 50

		# The basic character has no armor
		self.armor = 0
		self.protection = 0
		
		# The basic character fights with his fists
		fists = Weapon("Fists", "fists", 0, 0, 0)
		self.equiped_weapon = fists

		# The basic character has no shield (not implemented yet)
		# no_shield = Shield("None", "Basic", 0, 0, 0)
		# self.equiped_shield = no_shield

		# Compute vitality based on max health and armor
		self.vitality = self.max_health + self.armor

	def get_damage(self, damage):
		# Armor always protects the character
		self.vitality = self.vitality + self.protection - damage
		
		if self.vitality <= 0:
			self.vitality = 0
			self.dead = True

	def drink_potion(self):
		# Remove potion from inventory (if possible)
		# Increase health
		if self.potions > 0:
			self.potions = self.potions - 1
			self.vitality = self.vitality + 10
			print("You drink a potion. " + str(self.vitality) + " health remaining.")

			if self.potions == 0:
				print("This was your last potion.")

		else:
			print("You drank your last potion already.")

		
	def display(self):
		print(self.name + " the " + self.race)
		print("  Vitality:   " + str(self.vitality))
		print("  Protection: " + str(self.protection))
		print(' ')
		self.equiped_weapon.show_stats()
		print(' ')

	def describe(self):
		if self.equiped_weapon.type is 'fists':
			print('The character does not seem to have any weapon.')
		else:
			print('The character has a ' + self.equiped_weapon.type + '.')

	def attacks(self, Ennemy):
		# Self attacks Ennemy with equipped weapon
		# Ennemy defends with Dodge and/or Shield
		# Ennemy loses Armor and Health accordingly
		
		# First only assume melee weapons (strength)
		damage = self.strength + dice(1, self.equiped_weapon.attack, self.equiped_weapon.level)
		
		# Give the chance to the ennemy to dogde based on his characteristics
		if random.randint(0,100) > Ennemy.dodge:
			Ennemy.get_damage(damage)
			print(Ennemy.name + " loses " + str(damage) + " vitality. " + str(Ennemy.vitality) + " remaining.")
		else:
			print("Miss!")

class Hero(Character):
	
	# Inventory
	weapons = []
	objects = []
	
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

	def fight(self, Enemy):
		print("Fight! " + self.name + " vs " + Enemy.name)
		print("----------------")

		while (self.dead is False) and (Enemy.dead is False):
			
			action = int(input("1. Drink. 2. Attack: "))

			if action is 1:
				self.drink_potion()
			elif action is 2:
				self.attacks(Enemy)
			time.sleep(0.2)

			# The enemy can attack only if it is still alive
			if Enemy.dead is False:
				Enemy.attacks(self)

		if self.dead:
			print("Your hero died.")
		else:
			print("You killed your enemy.")

	def encounter(self, pnj):
		print('You see a ' + pnj.race + '. ')
		pnj.describe()

		print('1. Fight')
		print('2. Leave')
		action = input('What do you do? ')

		if action is '1':
			self.fight(pnj)
		elif action is '2':
			print('You walk away.')

	def find_chest(self, chest):
		print('You find a ' + chest.name + '.')
		print(' ')
		print('1. Open')
		print('2. Leave')
		action = input('What do you do? ')

		if action is '1':
			print('You find ' + str(chest.gold) + ' gold and ' + str(chest.potions) + ' potions.')
			print(' ')
			self.loot(chest.gold, chest.potions, [])

			print('The chest also contains ')
			print('  ' + chest.item.name + ', Level ' + str(chest.item.level))
			print(' ')

			print('1. Take and equip')
			print('2. Take')
			print('3. Leave')
			take = input('Do you take it?')

			if take is '1':
				self.loot(0, 0, [chest.item])
				self.equip_weapon(chest.item)
			elif take is '2':
				self.loot(0, 0, [chest.item])
			else:
				print('You walk away.')
		
class Creature(Character):

	def define_weapon(self, weapon):
		self.equiped_weapon = weapon



