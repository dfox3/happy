import datetime
from tabulate import tabulate

class Villager:
	def __init__(self, name="Decoy", surname= "Guy", age=18, sex="none", 
				 gender="none", species="Robot", sex_attractions=[], 
				 gender_attractions=[], species_attractions=["Robot"],
				 happiness=50, open_mindedness=50, 
				 social=50, giving=50, funnybone=50, money=0, beliefs={}, 
				 modifiers=[], coalitions=[], items=[], family={}, 
				 friends={}, enemies={}, properties=[]):
		self.name = name
		self.surname = surname
		self.age = age
		self.sex = sex
		self.gender = gender
		self.species = species
		self.sex_attractions = set(sex_attractions)
		self.gender_attractions = set(gender_attractions)
		self.species_attractions = set(species_attractions)
		self.happiness = happiness
		self.open_mindedness = open_mindedness
		self.social = social
		self.giving = giving
		self.funnybone = funnybone
		self.money = money
		self.beliefs = beliefs
		self.modifiers = modifiers
		self.coalitions = coalitions
		self.items = items
		self.family = family
		self.friends = friends
		self.enemies = enemies
		self.properties = properties
		self.time_init = str(datetime.datetime.now().time()).replace("/","-")

	def influence(self, other, influence):

		changes = []
		change = int(influence / 5)
		if self.happiness + change < 1:
			change = self.happiness - 1
		elif self.happiness + change > 100:
			change = 100 - self.happiness
		changes.append(change)
		if influence > 0:
			change = int((13 / (125 - self.open_mindedness)) * influence)
			if other.social < self.social:
				if other.social > self.social - change:
					changes.append(other.social - self.social)
				else:
					if self.social - change < 1:
						changes.append(1 - self.social)
					else:
						changes.append(-1 * change)
			elif other.social > self.social:
				if other.social < self.social + change:
					changes.append(other.social - self.social)
				else:
					if self.social + change > 100:
						changes.append(100 - self.social)
					else:
						changes.append(change)
			else:
				changes.append(0)
					
			change = int((22 / (125 - self.open_mindedness)) * influence)
			if other.giving < self.giving:
				if other.giving > self.giving - change:
					changes.append(other.giving - self.giving)
				else:
					if self.giving - change < 1:
						changes.append(1 - self.giving)
					else:
						changes.append(-1 * change)
			elif other.giving > self.giving:
				if other.giving < self.giving + change:
					changes.append(other.giving - self.giving)
				else:
					if self.giving + change > 100:
						changes.append(100 - self.giving)
					else:
						changes.append(change)
			else:
				changes.append(0)
					
			change = int((10 / (125 - self.funnybone)) * influence)
			if other.funnybone < self.funnybone:
				if other.funnybone > self.funnybone - change:
					changes.append(other.funnybone - self.funnybone)
				else:
					if self.funnybone - change < 1:
						changes.append(1 - self.funnybone)
					else:
						changes.append(-1 * change)
			elif other.funnybone > self.funnybone:
				if other.funnybone < self.funnybone + change:
					changes.append(other.funnybone - self.funnybone)
				else:
					if self.funnybone + change > 100:
						changes.append(100 - self.funnybone)
					else:
						changes.append(change)
			else:
				changes.append(0)
					
			change = int((6 / (125 - self.open_mindedness)) * influence)
			if other.open_mindedness < self.open_mindedness:
				if other.open_mindedness > self.open_mindedness - change:
					changes.append(other.open_mindedness - self.open_mindedness)
				else:
					if self.open_mindedness - change < 1:
						changes.append(1 - self.open_mindedness)
					else:
						changes.append(-1 * change)
			elif other.open_mindedness > self.open_mindedness:
				if other.open_mindedness < self.open_mindedness + change:
					changes.append(other.open_mindedness - self.open_mindedness)
				else:
					if self.open_mindedness + change > 100:
						changes.append(100 - self.open_mindedness)
					else:
						changes.append(change)
			else:
				changes.append(0)

		elif influence < 0:
			change = -1 * int((13 / (125 - self.open_mindedness)) * influence)
			if other.social < self.social:
				if self.social + change > 100:
					changes.append(100 - self.social)
				else:
					changes.append(change)
			elif other.social > self.social:
				if self.social - change < 1:
					changes.append(1 - self.social)
				else:
					changes.append(-1 * change)
			else:
				changes.append(0)
					
			change = -1 * int((22 / (125 - self.open_mindedness)) * influence)
			if other.giving < self.giving:
				if self.giving + change > 100:
					changes.append(100 - self.giving)
				else:
					changes.append(change)
			elif other.giving > self.giving:
				if self.giving - change < 1:
					changes.append(1 - self.giving)
				else:
					changes.append(-1 * change)
			else:
				changes.append(0)

			change = -1 * int((10 / (125 - self.funnybone)) * influence)
			if other.funnybone < self.giving:
				if self.funnybone + change > 100:
					changes.append(100 - self.funnybone)
				else:
					changes.append(change)
			elif other.funnybone > self.funnybone:
				if self.funnybone - change < 1:
					changes.append(1 - self.funnybone)
				else:
					changes.append(-1 * change)
			else:
				changes.append(0)

			change = -1 * int((6 / (125 - self.open_mindedness)) * influence)
			if other.open_mindedness < self.giving:
				if self.open_mindedness + change > 100:
					changes.append(100 - self.open_mindedness)
				else:
					changes.append(change)
			elif other.open_mindedness > self.open_mindedness:
				if self.open_mindedness - change < 1:
					changes.append(1 - self.open_mindedness)
				else:
					changes.append(-1 * change)
			else:
				changes.append(0)
		else:
			changes = changes + [0, 0, 0, 0]

		self.happiness += changes[0]
		self.social += changes[1]
		self.giving += changes[2]
		self.funnybone += changes[3]
		self.open_mindedness += changes[4]
		self.printBio(changes=changes)
				


	def printBio(self, changes=["", "", "", "", ""]):
		

		matrix = [["name:", self.name, ""],
				  ["surname:", self.surname, ""],
				  ["age:", self.age, ""],
				  ["sex:", self.sex, ""],
				  ["gender:", self.gender, ""],
				  ["species:", self.species, ""],
				  ["sex_attractions:", self.sex_attractions, ""],
				  ["gender_attractions:", self.gender_attractions, ""],
				  ["species_attractions:", self.species_attractions, ""],
				  ["happiness:", self.happiness, changes[0]],
				  ["open_mindedness:", self.open_mindedness, changes[4]],
				  ["social:", self.social, changes[1]],
				  ["giving:", self.giving, changes[2]],
				  ["funnybone:", self.funnybone, changes[3]],
				  ["money:", self.money, ""],
				  ["beliefs:", self.beliefs, ""],
				  ["modifiers:", self.modifiers, ""],
				  ["coalitions:", self.coalitions, ""],
				  ["items:", self.items, ""],
				  ["family:", self.family, ""],
				  ["friends:", self.friends, ""],
				  ["enemies:", self.enemies, ""],
				  ["properties:", self.properties, ""],
				  ["time_init:", self.time_init, ""]]

		#s = [ [ str(e) for e in row ] for row in matrix ]
		#ens = [ max(map(len, col)) for col in zip(*s) ]
		#fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		#table = [ fmt.format(*row) for row in s ]
		print("--------------------------------------------------------------")
		print(tabulate(matrix))
		print("\n")
		return