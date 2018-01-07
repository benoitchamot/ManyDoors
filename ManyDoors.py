from Characters import *

def create_hero():
	name = input("What is your name? ")
	print("What is your kind? ")
	print("1 - Dwarf")
	print("2 - Human")
	print("3 - Elf")
	choice = input()
	
	if choice is '1':
		race = 'Dwarf'
	elif choice is '2':
		race = 'Human'
	elif choice is '3':
		race = 'Elf'
	
	return Hero(name, 1, race)

# Start game

# Create hero and display characteristics
hero = create_hero()
hero.display()

# Make a new weapon
sword = Weapon('Sword', 'weapon', 200, 12, 1)

# Make a new shield
shield = Shield('Shield', 'shield', 1200, 5, 2)

# Get weapon, shield and basic equipment
hero.loot(10, 2, [sword, shield])
hero.equip_weapon(sword)

# Create a creature to fight
creat = Creature("Guard", 1, "Human")

hero.show_inventory()

hero.fight(creat)


# Actions
# attack
# bribe
# inventory
# loot
# open content
# run
# drink potion
