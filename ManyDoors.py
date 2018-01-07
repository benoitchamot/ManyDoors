from Characters import *
from Items import *
from Rooms import *

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
chest1 = Chest('Old Chest', gold, potions, item)
chest2 = Chest('Big Chest', gold, potions, item)

# Create a creature to fight
creat = Creature("Guard", 1, "Human")
creat.define_weapon(sword)

# Create a room to visit
room = Room([chest1, chest2], [creat])

# Visit room's creatures and find room's chests
if room.creatures:
	for each_creature in room.creatures:
		hero.encounter(each_creature)

if room.chests:
	for each_chest in room.chests:
		hero.find_chest(each_chest)

# Actions
# attack
# bribe
# inventory
# loot
# open content
# run
# drink potion
