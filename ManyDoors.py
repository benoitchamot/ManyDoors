from Characters import *
from Items import *

def create_hero():
	#name = input("What is your name? ")
	#print("What is your kind? ")
	#print("1 - Dwarf")
	#print("2 - Human")
	#print("3 - Elf")
	#choice = input()
	
	#if choice is '1':
	#	race = 'Dwarf'
	#elif choice is '2':
	#	race = 'Human'
	#elif choice is '3':
	#	race = 'Elf'
	
	return Hero('Bob', 1, 'Dwarf')



# Start game

# Create hero and display characteristics
hero = create_hero()
hero.display()

# Make new weapons
sword = Weapon('Common Sword', 'sword', 200, 12, 1)

# Create one chest with some gold, potions and one weapon
gold = 100
potions = 23
item = Weapon('Common Knife', 'knife', 2, 0.2, 2)
chest = Chest('Old Chest', gold, potions, item)



# Create a creature to fight
creat = Creature("Guard", 1, "Human")
creat.define_weapon(sword)

# Encounter
hero.encounter(creat)
hero.find_chest(chest)
hero.display()



# Actions
# attack
# bribe
# inventory
# loot
# open content
# run
# drink potion
