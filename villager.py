import datetime
from tabulate import tabulate
from random import randint, choice, sample, shuffle
from math import ceil
from collections import defaultdict
from statistics import median, mean
from traits_categories import *

class Villager:
	def __init__(self, name="Decoy", surname= "Guy", aliases={}, 
				 age=18, sex="none", gender="none", species="Robot", 
				 sex_attractions=[], gender_attractions=[], 
				 species_attractions=["Robot"],happiness=50, 
				 open_mindedness=50, social=50, giving=50, funnybone=50, 
				 strength=50, dexterity=50, stamina=50, intelligence=50, 
				 speed=50, alive=True, inspiration=0, money=0, 
				 encyclopedia={}, tech={}, beliefs={}, 
				 traits=[], coalitions=[], items=[], family={}, 
				 friends={}, enemies={}, lovers={}, properties=[]):
		self.name = name
		self.surname = surname
		self.aliases = aliases
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
		self.strength = strength
		self.dexterity = dexterity
		self.stamina = stamina
		self.intelligence = intelligence
		self.speed = speed
		self.alive = alive
		self.inspiration = inspiration
		self.money = money
		self.encyclopedia = encyclopedia
		self.tech = tech
		self.beliefs = beliefs
		self.traits = traits
		self.coalitions = coalitions
		self.items = items
		self.family = family
		self.friends = friends
		self.enemies = enemies
		self.lovers = lovers
		self.properties = properties
		self.last_interactions_happiness = []
		self.last_interactions_ids = []
		self.last_interactions_influence = []
		self.last_interaction_type_received = "small talk"
		self.last_interaction_type_sent = "small talk"

		self.time_init = str(datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
		self.id = str(self.name) + "_" + str(self.surname) + "_" + str(self.time_init)

	def influence(self, other, influence, dialog=""):
		#print("Entering an influence loop, self: " + str(self.id) + ". other: " + str(other.id))
		#store interaction in memory
		self.last_interactions_happiness.append(other.happiness)
		self.last_interactions_ids.append(other.id)
		self.last_interactions_influence.append(influence)
		if dialog != "":
			self.last_interaction_type_received = dialog
			other.last_interaction_type_sent = dialog

		#update beliefs and encyclopedia

		#update friends, enemies
		change = 1 + abs(int(influence/8))
		if other.id not in self.family:
			self.family[other.id] = 0
		if other.id not in self.friends:
			self.friends[other.id] = 1
		if other.id not in self.enemies:
			self.enemies[other.id] = 1
		if other.id not in self.lovers:
			self.lovers[other.id] = 1

		if influence > 0:
			change = ceil(float(change))
			if self.enemies[other.id] > 1:
				self.enemies[other.id] -= change
				if self.enemies[other.id] < 1:
					change = 1 + (-1 * self.enemies[other.id])
					self.enemies[other.id] = 1
					self.friends[other.id] += change
					if self.friends[other.id] > 100:
						self.friends[other.id] = 100
			else:
				self.friends[other.id] += change
				if self.friends[other.id] > 100:
					self.friends[other.id] = 100
		elif influence < 0:
			if self.friends[other.id] > 1:
				self.friends[other.id] -= change
				if self.friends[other.id] < 1:
					change = 1 + (-1 * self.friends[other.id])
					self.friends[other.id] = 1
					self.enemies[other.id] += ceil(change*1.3)
					if self.enemies[other.id] > 100:
						self.enemies[other.id] = 100
			else:
				self.enemies[other.id] += ceil(change*1.3)
				if self.enemies[other.id] > 100:
					self.enemies[other.id] = 100

		#calibrate social sliders
		changes = []
		change = int(influence / 5)
		if self.happiness + change < 1:
			change = self.happiness - 1
		elif self.happiness + change > 100:
			change = 100 - self.happiness
		changes.append(change)
		if influence > 0:
			change = int((13 / (125 - self.open_mindedness)) * influence)
			if other.social <= self.social:
				if self.social - change < 1:
					changes.append(1 - self.social)
				else:
					changes.append(-1 * change)
			else:
				if self.social + change > 100:
					changes.append(100 - self.social)
				else:
					changes.append(change)
					
			change = int((22 / (125 - self.open_mindedness)) * influence)
			if other.giving <= self.giving:
				if self.giving - change < 1:
					changes.append(1 - self.giving)
				else:
					changes.append(-1 * change)
			else:
				if self.giving + change > 100:
					changes.append(100 - self.giving)
				else:
					changes.append(change)
					
			change = int((10 / (125 - self.funnybone)) * influence)
			if other.funnybone <= self.funnybone:
				if self.funnybone - change < 1:
					changes.append(1 - self.funnybone)
				else:
					changes.append(-1 * change)
			else:
				if self.funnybone + change > 100:
					changes.append(100 - self.funnybone)
				else:
					changes.append(change)
					
			change = int((6 / (125 - self.open_mindedness)) * influence)
			if other.open_mindedness <= self.open_mindedness:
				if self.open_mindedness - change < 1:
					changes.append(1 - self.open_mindedness)
				else:
					changes.append(-1 * change)
			else:
				if self.open_mindedness + change > 100:
					changes.append(100 - self.open_mindedness)
				else:
					changes.append(change)

		elif influence < 0:
			change = -1 * int((13 / (125 - self.open_mindedness)) * influence)
			if other.social <= self.social:
				if self.social + change > 100:
					changes.append(100 - self.social)
				else:
					changes.append(change)
			else:
				if self.social - change < 1:
					changes.append(1 - self.social)
				else:
					changes.append(-1 * change)
					
			change = -1 * int((22 / (125 - self.open_mindedness)) * influence)
			if other.giving <= self.giving:
				if self.giving + change > 100:
					changes.append(100 - self.giving)
				else:
					changes.append(change)
			else:
				if self.giving - change < 1:
					changes.append(1 - self.giving)
				else:
					changes.append(-1 * change)

			change = -1 * int((10 / (125 - self.funnybone)) * influence)
			if other.funnybone <= self.giving:
				if self.funnybone + change > 100:
					changes.append(100 - self.funnybone)
				else:
					changes.append(change)
			else:
				if self.funnybone - change < 1:
					changes.append(1 - self.funnybone)
				else:
					changes.append(-1 * change)

			change = -1 * int((6 / (125 - self.open_mindedness)) * influence)
			if other.open_mindedness <= self.giving:
				if self.open_mindedness + change > 100:
					changes.append(100 - self.open_mindedness)
				else:
					changes.append(change)
			else:
				if self.open_mindedness - change < 1:
					changes.append(1 - self.open_mindedness)
				else:
					changes.append(-1 * change)
		else:
			changes = changes + [0, 0, 0, 0]

		self.happiness += changes[0]
		self.social += changes[1]
		self.giving += changes[2]
		self.funnybone += changes[3]
		self.open_mindedness += changes[4]
		changes = self.traitsModInfluence(other, changes, influence, dialog)
		self.printBio(other, changes=changes)
				
	def calibratePassiveHappiness(self):
		count = 0
		shuffle(self.last_interactions_happiness)
		calibrate = True
		if len(self.last_interactions_happiness) == 0:
			calibrate = False
		while calibrate:
			self.happiness += int((float(self.last_interactions_happiness[count] - 50)/10.0) / float(ceil(float(101 - self.open_mindedness) / 10.0))) 
			if self.happiness > 85:
				self.happiness = 85
			if self.happiness < 15:
				self.happiness = 15
			count += 1
			if count == ceil(float(self.open_mindedness) / 10.0) or count == len(self.last_interactions_happiness):
				calibrate = False
		self.last_interactions_happiness = []
		mut_directions = [-1, 1]
		shuffle(mut_directions)
		mut_vals = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 9, 10]
		shuffle(mut_vals)
		self.happiness -= choice(mut_directions) * choice(mut_vals)
		if self.happiness > 95:
			self.happiness = 95
		if self.happiness < 5:
			self.happiness = 5

		#self.happiness -= int((self.happiness - 50) / (self.open_mindedness / 10))

	def calibratePassiveColleagues(self):
		#friend recalibration
		encounter_dict = defaultdict(int)
		positives = [ self.last_interactions_ids[i] for i, x in enumerate(self.last_interactions_influence) if (x > 0 and self.friends[self.last_interactions_ids[i]] > 1) ]
		positives = positives + [ x for x in self.friends if self.friends[x] > 1 ]
		for e in positives:
			encounter_dict[e] += 1
		percent_dict = { n: int(float(encounter_dict[e]) / float(len(positives)) * 100) for n in encounter_dict }
		for p in percent_dict:
			if self.enemies[p] > 1:
				change = int(float(percent_dict[p] - self.enemies[p]) / 2.0)
				if change < 0:
					self.enemies[p] = abs(change)
				elif change > 0:
					self.enemies[p] = 1
					self.friends[p] = change
				else:
					self.enemies[p] = 1
					self.friends[p] = 1
			else:
				self.friends[p] = int(float(self.friends[p] + percent_dict[p]) / 2.0)
				if self.happiness > 85:
					if self.friends[p] > 95:
						self.friends[p] = 95
					elif self.friends[p] < 5:
						self.friends[p] = 5
				else:
					if self.friends[p] > 85:
						self.friends[p] = 85
					elif self.friends[p] < 1:
						self.friends[p] = 1

		#enemy recalibrations
		encounter_dict = defaultdict(int)
		negatives = [ self.last_interactions_ids[i] for i, x in enumerate(self.last_interactions_influence) if (x < 0 and self.enemies[self.last_interactions_ids[i]] > 1) ]
		for e in negatives:
			encounter_dict[e] += 1
		percent_dict = { n: int(float(encounter_dict[e]) / float(len(negatives)) * 100) for n in encounter_dict }
		for p in percent_dict:
			if self.friends[p] > 1:
				change = int(float(percent_dict[p] - self.friends[p]) / 2.0)
				if change < 0:
					self.friends[p] = abs(change)
				elif change > 0:
					self.friends[p] = 1
					self.enemies[p] = change
				else:
					self.friends[p] = 1
					self.enemies[p] = 1

			else:
				self.enemies[p] = int((float(self.enemies[p]) + float(percent_dict[p])) / 2.0)
				if self.happiness < 15:
					if self.enemies[p] > 95:
						self.enemies[p] = 95
					elif self.enemies[p] < 5:
						self.enemies[p] = 5
				else:
					if self.enemies[p] > 85:
						self.enemies[p] = 85
					elif self.enemies[p] < 1:
						self.enemies[p] = 1

		self.last_interactions_ids = []
		self.last_interactions_influence = []

	def getTopFriends(self):
		top_friends = {}
		if len(self.friends.keys()) != 0:
			median_friend_value = mean([ self.friends[k] for k in self.friends ])
			top_friends = { k: self.friends[k] for k in self.friends if self.friends[k] > median_friend_value }
		return { k: v for (k, v) in sorted(top_friends.items(), key=lambda item: item[1]) }

	def traitsModInfluence(self, other, changes, influence, dialog):
		HAPPY = 0
		SOCIAL = 1
		GIVING = 2
		OPENMIND = 3
		FUNNY = 4
		npc_mods = [ t for t in self.traits if t in INFLUENCE ]
		for t in npc_mods:

			if t == "rock":
				changes[HAPPY] //= 2

			if t == "manic":
				if changes[HAPPY] > 0:
					changes[HAPPY] *= 3
					changes[HAPPY] //= 2

			if t == "depressed":
				if changes[HAPPY] < 0:
					changes[HAPPY] *= 3
					changes[HAPPY] //= 2

			if t == "sensitive":
				changes[HAPPY] *= 2

			if t == "misogynist":
				if other.gender == "female":
					changes = [ i // 2 for i in changes ]

			if t == "misandrist":
				if other.gender == "male":
					changes = [ i // 2 for i in changes ]

			if t == "thick skin":
				if dialog == "insult":
					changes = [ 1, 0, 0, 0, 0 ]

		other_mods = [ t for t in other.traits if t in INFLUENCE ]
		for t in other_mods:

			if t == "body odor":
				changes[HAPPY] -= 1
				changes[SOCIAL] -= 1

			if t == "bad breath":
				changes[HAPPY] -= 1
				changes[SOCIAL] -= 1

			if t == "mute":
				if dialog == "ignore":
					changes = [ i // 2 for i in changes ]

		print(changes)
		return changes


	def printBio(self, other, changes=["", "", "", "", ""]):
		'''

		self.name = name
		self.surname = surname
		self.aliases = aliases
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
		self.strength = strength
		self.dexterity = dexterity
		self.stamina = stamina
		self.intelligence = intelligence
		self.speed = speed
		self.alive = alive
		self.inspiration = inspiration
		self.money = money
		self.encyclopedia = encyclopedia
		self.tech = tech
		self.beliefs = beliefs
		self.traits = traits
		self.coalitions = coalitions
		self.items = items
		self.family = family
		self.friends = friends
		self.enemies = enemies
		self.lovers = lovers
		self.properties = properties
		self.last_interactions_happiness = []
		self.time_init = str(datetime.datetime.now().time()).replace("/","-")
		self.id = str(self.name) + "_" + str(self.surname) + "_" + str(self.time_init)
		'''

		matrix = [["name:", self.name, ""],
				  ["surname:", self.surname, ""],
				  ["aliases:", self.aliases, ""],
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
				  ["strength:", self.strength, ""],
				  ["dexterity:", self.dexterity, ""],
				  ["stamina:", self.stamina, ""],
				  ["intelligence:", self.intelligence, ""],
				  ["speed:", self.speed, ""],
				  ["alive:", self.alive, ""],
				  ["inspiration:", self.inspiration, ""],
				  ["money:", self.money, ""],
				  ["encyclopedia:", self.encyclopedia, ""],
				  ["tech:", self.tech, ""],
				  ["beliefs:", self.beliefs, ""],
				  ["traits:", self.traits, ""],
				  ["coalitions:", self.coalitions, ""],
				  ["items:", self.items, ""],
				  ["family:", self.family[other.id], ""],
				  ["friends:", self.friends[other.id], ""],
				  ["enemies:", self.enemies[other.id], ""],
				  ["lovers:", self.lovers[other.id], ""],
				  ["properties:", self.properties, ""],
				  #["last_interactions_happiness:", self.last_interactions_happiness, ""],
				  #["last_interactions_ids:", self.last_interactions_ids, ""],
				  ["time_init:", self.time_init, ""],
				  ["id:", self.id, ""],
				  ]

		#s = [ [ str(e) for e in row ] for row in matrix ]
		#ens = [ max(map(len, col)) for col in zip(*s) ]
		#fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		#table = [ fmt.format(*row) for row in s ]
		print("--------------------------------------------------------------")
		print(tabulate(matrix))
		print("\n")
		return