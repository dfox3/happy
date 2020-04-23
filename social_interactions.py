from villager import Villager
from random import randint, choice, sample, shuffle
import time
import csv
from math import ceil
import datetime
import os
import argparse
from itertools import combinations
from trait_modifiers import *

#--------------------------------------------------------------------------------------------------
#Command line input parameters
parser = argparse.ArgumentParser(description='Social Interactions')

parser.add_argument('-l',
                    metavar='-log',
                    type=str,
                    default="Jokerfication",
                    help="Log directory name. Overrides automatically generated log directory.")
parser.add_argument('-i',
                    metavar='-iterations',
                    type=int,
                    default=-1,
                    help="Set number of interations in simulation.")
parser.add_argument('-t',
                    metavar='-timewait',
                    type=int,
                    default=-1,
                    help="Set how much time to wait between iterations.")
parser.add_argument('-r',
                    metavar='-recalibrate',
                    type=int,
                    default=10,
                    help="Set how many interations are needed before happiness recalibration.")

#--------------------------------------------------------------------------------------------------
#GLOBAL variables
VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
TERMINATORS = {"thanks", "ignore", "bye", "hug"}
#--------------------------------------------------------------------------------------------------
#Main wrapper
def main():
	options = parser.parse_args()
	'''
	class Villager:
		def __init__(self, name="Decoy", age=18, sex="none", 
					 gender="none", happiness=50, open_mindedness=50, 
					 social=50, giving=50, money=0, beliefs=[], 
					 modifiers=[], coalitions=[], items=[], family=[], 
					 friends=[], enemies=[], properties=[]):
			self.name = name
			self.age = age
			self.sex = sex
			self.gender = gender
			self.happiness = happiness
			self.open_mindedness = open_mindedness
			self.social = social
			self.giving = giving
			self.money = money
			self.beliefs = beliefs
			self.modifiers = modifiers
			self.coalitions = coalitions
			self.items = items
			self.family = family
			self.friends = friends
			self.enemies = enemies
			self.properties = properties
	'''
	npcs = [ Villager(),
	Villager(name="Conald", surname="Peter", age=53, social=95, giving=43, happiness=12, 
				  open_mindedness=8, species="Human", sex="male", gender="male", funnybone=40,
				  traits={"menace":"", "cte":"", "short fuse":"", "manic":"", "depressed":""}),
	Villager(name="Ponchis", surname="Gomez", age=28, social=75, giving=25, happiness=25,
				  open_mindedness=50, species="Human", sex="male", gender="male", funnybone=60),
	Villager(name="Michael", surname="Dizon", age=27, social=80, giving=90, happiness=10,
				  open_mindedness=80, species="Human", sex="male", gender="male", funnybone=63),
	Villager(name="Emily", surname="Lofaro", age=26, social=65, giving=90, happiness=82,
				  open_mindedness=85, species="Human", sex="female", gender="female", funnybone=58,
				  traits={"sensitive":""}),
	Villager(name="Ben", surname="Pflughoeft", age=26, social=60, giving=72, happiness=40, 
				  open_mindedness=87, species="Human", sex="male", gender="male", funnybone=81),
	Villager(name="Emma", surname="", age=99, social=87, giving=99, happiness=93,
				  open_mindedness=50, species="Human", sex="female", gender="female", funnybone=50),
	Villager(name="Micah", surname="", age=99, social=74, giving=37, happiness=99, 
				  open_mindedness=69, species="Human", sex="male", gender="male", funnybone=89,
				  traits={"pedantic":"", "thick skin":""}),
	Villager(name="Dylan", surname="", age=27, social=60, giving=95, happiness=60, 
				  open_mindedness=79, species="Human", sex="male", gender="male", funnybone=90,
				  traits={"cliquey":"", "bad breath":"", "thick skin":""}),
	Villager(name="Jimmy", surname="Stewart", age=25, social=75, giving=50, happiness=25, 
				  open_mindedness=80, species="Human", sex="male", gender="male", funnybone=61,
				  traits={"sensitive":""}),
	Villager(name="Dom", surname="Misja", age=3, social=15, giving=80, happiness=75, 
				  open_mindedness=25, species="Human", sex="male", gender="male", funnybone=55,
				  traits={"rock":""}),
	Villager(name="Alex", surname="Lukasiewicz", age=4, social=90, giving=80, happiness=80, 
				  open_mindedness=70, species="Human", sex="female", gender="female", funnybone=65),
	Villager(name="Claire", surname="", age=12, social=90, giving=90, happiness=75, 
				  open_mindedness=65, species="Human", sex="female", gender="female", funnybone=40),
	Villager(name="Spongebob", surname="Squarepants", age=22, social=90, giving=90, happiness=90, 
				  open_mindedness=90, species="Sea Sponge", sex="male", gender="male", funnybone=90,
				  traits={"clown":"", "manic":""}),
	Villager(name="Patrick", surname="Star", age=31, social=55, giving=50, happiness=95, 
				  open_mindedness=55, species="Starfish", sex="male", gender="male", funnybone=95,
				  traits={"body odor":""}),
	Villager(name="Squidward", surname="Tentacles", age=27, social=33, giving=10, happiness=23, 
				  open_mindedness=60, species="Squid", sex="male", gender="male", funnybone=10,
				  traits={"depressed":""}),
	Villager(name="Eugene", surname="Krabs", age=51, social=62, giving=1, happiness=40, 
				  open_mindedness=33, species="Crab", sex="male", gender="male", funnybone=52),
	Villager(name="Pearl", surname="Krabs", age=16, social=95, giving=35, happiness=40, 
				  open_mindedness=40, species="Whale", sex="female", gender="female", funnybone=20,
				  traits={"girls club":"", "short fuse":""}),
	Villager(name="Plankton", surname="", age=35, social=15, giving=5, happiness=5, 
				  open_mindedness=55, species="Plankton", sex="male", gender="male", funnybone=5,
				  traits={"short fuse":"", "depressed":"", "stalker": "Spongebob"}),
	Villager(name="Oliver", surname="Nath", age=69, social=70, giving=60, happiness=40, 
				  open_mindedness=70, species="Human", sex="male", gender="male", funnybone=75,
				  traits={"depressed":"", "pedantic":""}),
	Villager(name="Amber", surname="", age=12, social=92, giving=99, happiness=85, 
				  open_mindedness=90, species="Human", sex="female", gender="female", funnybone=55,
				  traits={"short fuse":""}),
	Villager(name="Kofi", surname="Oduro", age=41, social=92, giving=80, happiness=30, 
				  open_mindedness=12, species="Human", sex="male", gender="male", funnybone=22),
	Villager(name="Tony", surname="Soprano", age=52, social=64, giving=33, happiness=12, 
				  open_mindedness=40, species="Human", sex="male", gender="male", funnybone=45,
				  traits={"boys club":"", "misogynist":""}),
	Villager(name="Mutes", surname="Muter", age=52, species="Human", sex="male", gender="male",
				  traits={"mute":""}),
	]

	#npcs = set([ v1, v2, v3, v4, v5 ]
	#npcs = [ v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23 ]
	id_index_map = { n.id: i for i, n in enumerate(npcs) }

	log_sub_folder = options.l
	if log_sub_folder == "Jokerfication":
		log_sub_folder = str(datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
	for n in npcs:
		primeDiagnostics(n, log_sub_folder)
	loop = True
	count = 1
	while loop:
		index_list = []
		index_list_2 = []
		for i, n in enumerate(npcs):
			index_list = index_list + [ i for x in range(ceil(n.social)) ]
			index_list_2 = index_list_2 + [ i for x in range(ceil(n.social/3)) ]
		shuffle(index_list)
		samples = [choice(index_list)]
		if npcs[samples[0]].happiness > 75 or npcs[samples[0]].happiness < 25:
			for n in npcs[samples[0]].enemies:
				index_list_2 = index_list_2 + [ id_index_map[n] for x in range(int(npcs[samples[0]].enemies[n]/10)+1) ]
		else:
			for n in npcs[samples[0]].friends:
				index_list_2 = index_list_2 + [ id_index_map[n] for x in range(int(npcs[samples[0]].friends[n]/20)+1) ]
		index_list_2 = traitsModInteract(npcs[samples[0]], npcs, index_list_2)
		shuffle(index_list_2)
		while len(samples) < 2:
		    selection = choice(index_list_2)
		    if selection not in samples:
		        samples.append(selection)
		s1, s2 = interact(npcs[samples[0]], npcs[samples[1]], log_sub_folder)
		npcs[samples[0]] = s1
		npcs[samples[1]] = s2

		for n in npcs:
			if count % options.r == 0:
				n.calibratePassiveHappiness()
				n.calibratePassiveColleagues()
			printDiagnostics(n, log_sub_folder)
		if count % options.r == 0:
			for i in range(len(npcs)):
				for pair in list(combinations(npcs, i)):
					if len(pair) == 2:
						readTheRoom(pair[0], pair[1])
		updateDiagnosticFriends(s1, s2, count, log_sub_folder)
		updateDiagnosticFriends(s2, s1, count, log_sub_folder)
		updateDiagnosticEnemies(s1, s2, count, log_sub_folder)
		updateDiagnosticEnemies(s2, s1, count, log_sub_folder)

		if options.t != -1:
			time.sleep(options.t)
		if options.i != -1:
			if count > options.i:
				loop = False
		count += 1



def interact(v1, v2, log_sub_folder):
	initiator, receiver = initiate(v1, v2)
	dialog = getDialogType(initiator, receiver)
	influence_sent = interpretDialog(initiator, receiver, dialog)
	response = getResponseType(receiver, initiator, dialog, influence_sent)
	influence_responded = interpretDialog(receiver, initiator, response)
	print("initiator:\t" + str(initiator.id))
	print("receiver:\t" + str(receiver.id))
	print("v1:\t" + str(v1.id))
	print("v2:\t" + str(v2.id))
	if initiator.id == v1.id:
		v2.influence(v1, influence_sent, dialog=dialog)
		v1.influence(v2, influence_responded, dialog=response)
		updateDiagnosticInteractionSent(v1, dialog, "initiator", influence_sent, v2, log_sub_folder)
		updateDiagnosticInteractionSent(v2, response, "receiver", influence_responded, v1, log_sub_folder)
		updateDiagnosticInteractionReceived(v1, response, "initiator", influence_responded, v2, log_sub_folder)
		updateDiagnosticInteractionReceived(v2, dialog, "receiver", influence_sent, v1, log_sub_folder)
	else:
		v1.influence(v2, influence_sent, dialog=dialog)
		v2.influence(v1, influence_responded, dialog=response)
		updateDiagnosticInteractionSent(v2, dialog, "initiator", influence_sent, v1,log_sub_folder)
		updateDiagnosticInteractionSent(v1, response, "receiver", influence_responded, v2, log_sub_folder)
		updateDiagnosticInteractionReceived(v2, response, "initiator", influence_responded, v1, log_sub_folder)
		updateDiagnosticInteractionReceived(v1, dialog, "receiver", influence_sent, v2, log_sub_folder)
	
	extension = 0
	while response not in TERMINATORS:
		extension += 1
		if extension % 2 == 1:
			response = getResponseType(initiator, receiver, response, influence_responded, past_greetings=True)
			influence_responded = interpretDialog(initiator, receiver, response)
			if initiator.id == v1.id:
				v2.influence(v1, influence_responded, dialog=response)
				updateDiagnosticInteractionSent(v1, response, "receiver", influence_responded, v2, log_sub_folder)
				updateDiagnosticInteractionReceived(v2, response, "receiver", influence_responded, v1, log_sub_folder)
			else:
				v1.influence(v2, influence_responded, dialog=response)
				updateDiagnosticInteractionSent(v2, response, "receiver", influence_responded, v1, log_sub_folder)
				updateDiagnosticInteractionReceived(v1, response, "receiver", influence_responded, v2, log_sub_folder)
		else:
			response = getResponseType(receiver, initiator, response, influence_responded, past_greetings=True)
			influence_responded = interpretDialog(receiver, initiator, response)
			if initiator.id == v1.id:
				v1.influence(v2, influence_responded, dialog=response)
				updateDiagnosticInteractionSent(v2, response, "receiver", influence_responded, v1, log_sub_folder)
				updateDiagnosticInteractionReceived(v1, response, "receiver", influence_responded, v2, log_sub_folder)
			else:
				v2.influence(v1, influence_responded, dialog=response)
				updateDiagnosticInteractionSent(v1, response, "receiver", influence_responded, v2, log_sub_folder)
				updateDiagnosticInteractionReceived(v2, response, "receiver", influence_responded, v1, log_sub_folder)
	
	return v1, v2


def initiate(v1, v2):
	v1_bounds = []
	v2_bounds = []
	v1_bounds.append(v1.social - 25)
	if v1_bounds[0] < 1:
		v1_bounds[0] = 1
	v1_bounds.append(v1.social + 25)
	if v1_bounds[1] > 100:
		v1_bounds[1] = 100
	v2_bounds.append(v2.social - 25)
	if v2_bounds[0] < 1:
		v2_bounds[0] = 1
	v2_bounds.append(v2.social + 25)
	if v2_bounds[1] > 100:
		v2_bounds[1] = 100
	v1_roll = randint(v1_bounds[0], v1_bounds[1])
	print(str(v1.name) + " rolls " + str(v1_roll) + " for initiative." )
	v2_roll = randint(v2_bounds[0], v2_bounds[1])
	print(str(v2.name) + " rolls " + str(v2_roll) + " for initiative." )
	initiator = ""
	receiver = ""
	if v1_roll > v2_roll:
		print(str(v1.name) + " wins initiative.")
		initiator = v1
		receiver = v2
	elif v1_roll < v2_roll:
		print(str(v2.name) + " wins initiative.")
		initiator = v2
		receiver = v1
	else:
		if v1.social > v2.social:
			print("Tied goes to socialite. " + str(v1.name) + " wins.")
			initiator = v1
			receiver = v2
		elif v1.social < v2.social:
			print("Tie goes to socialite. " + str(v2.name) + " wins.")
			initiator = v2
			receiver = v1
		else:
			if randint(0,1) == 0:
				print("Tie goes to socialite, but these individuals are equal. Fate predicts " + str(v1.name) + " wins.")
				initiator = v1
				receiver = v2
			else:
				print("Tie goes to socialite, but these individuals are equal. Fate predicts " + str(v2.name) + " wins.")
				initiator = v2
				receiver = v1
	return initiator, receiver


def getDialogType(npc, receiver):
	#compliments
	#insults
	#jokes
	#stories
	#questions
	#small talk
	#advice
	#flirting
	#lamenting
	#arguing
	#staring
	#dancing
	#singing
	#roughhousing
	#gossiping
	#shaming
	#rhyme games
	#equivocation
	#propagating
	#spreading lies and rumors
	#thanks
	#ignore

	family_val = 1
	friend_val = 1
	enemy_val = 1
	if receiver in npc.family:
		family_val = npc.family[receiver.id]
	if receiver in npc.friends:
		family_val = npc.friends[receiver.id]
	if receiver in npc.family:
		family_val = npc.enemies[receiver.id]

	#family, friends, foes modifiers
	values = [ "greetings", "compliment", "insult", "joke", "story", "question", "small talk", "advice", "lament", "argue", "thanks", "ignore"]
	values = values + [ "compliment" for x in range(2*ceil(family_val/20)) ]
	values = values + [ "compliment" for x in range(2*ceil(friend_val/20)) ]
	values = values + [ "insult" for x in range(4*ceil(enemy_val/20)) ]
	values = values + [ "argue" for x in range(2*ceil(enemy_val/20)) ]
	values = values + [ "question" for x in range(2*ceil(enemy_val/20)) ]
	values = values + [ "advice" for x in range(3*ceil(family_val/20)) ]
	values = values + [ "lament" for x in range(1*ceil(family_val/20)) ]
	values = values + [ "lament" for x in range(1*ceil(friend_val/20)) ]
	values = values + [ "joke" for x in range(2*ceil(friend_val/20)) ]
	values = values + [ "joke" for x in range(1*ceil(family_val/20)) ]
	values = values + [ "story" for x in range(1*ceil(friend_val/20)) ]
	values = values + [ "story" for x in range(1*ceil(family_val/20)) ]
	values = values + [ "thanks" for x in range(1*ceil(family_val/20)) ]
	values = values + [ "thanks" for x in range(1*ceil(friend_val/20)) ]

	# greetings
	values = values + disList(npc.social, 1, "greetings")
	values = values + disList(npc.social, 1, "greetings")
	values = values + disList(npc.social, 1, "greetings")

	# compliments
	values = values + disList(npc.giving, 70, "compliment")
	values = values + disList(npc.happiness, 75, "compliment")

	# insults
	values = values + disList(npc.open_mindedness, 20, "insult", m=-1)
	values = values + disList(npc.happiness, 33, "insult", m=-1)

	# jokes
	values = values + disList(npc.funnybone, 66, "joke")
	values = values + disList(npc.happiness, 10, "joke", m=-1)
	values = values + disList(npc.happiness, 90, "joke")

	# story
	values = values + disList(npc.funnybone, 30, "story", max_val=20)
	values = values + disList(npc.funnybone, 70, "story", m=-1, max_val=20)
	values = values + disList(npc.happiness, 10, "story", m=-1)
	values = values + disList(npc.happiness, 90, "story")
	values = values + disList(npc.social, 90, "story")

	# question
	values = values + disList(npc.open_mindedness, 50, "question", max_val=10)
	values = values + disList(npc.open_mindedness, 90, "question", max_val=10)
	values = values + disList(npc.social, 90, "question")
	values = values + disList(npc.happiness, 20, "question", m=-1, max_val=10)

	# small talk
	values = values + disList(npc.social, 50, "small talk", max_val=15)

	# advice
	values = values + disList(npc.funnybone, 33, "advice", m=-1, max_val=2)
	values = values + disList(npc.open_mindedness, 20, "advice", m=-1, max_val=5)
	values = values + disList(npc.open_mindedness, 90, "advice", max_val=5)

	# lament
	values = values + disList(npc.happiness, 50, "lament", m=-1, max_val=5)
	values = values + disList(npc.happiness, 30, "lament", m=-1, max_val=10)
	values = values + disList(npc.happiness, 10, "lament", m=-1)
	values = values + disList(npc.social, 90, "lament", max_val=5)

	# argue
	values = values + disList(npc.funnybone, 33, "argue", m=-1)
	values = values + disList(npc.happiness, 33, "argue", m=-1)
	values = values + disList(npc.happiness, 90, "argue")
	values = values + disList(npc.open_mindedness, 75, "argue")

	# thanks
	values = values + disList(npc.happiness, 95, "thanks")
	values = values + disList(npc.social, 10, "thanks", m=-1)

	# ignore
	values = values + disList(npc.happiness, 10, "ignore", m=-1)
	values = values + disList(npc.social, 20, "ignore", m=-1)
	values = values + disList(npc.open_mindedness, 15, "ignore", m=-1)
	print(values)
	shuffle(values)
	#print(values)
	return sample(values, 1)[0]


def getResponseType(npc, receiver, dialog, influence, past_greetings=False):
	#greetings
	#compliments
	#insults
	#jokes
	#stories
	#questions
	#small talk
	#advice
	#flirting
	#lamenting
	#arguing
	#staring
	#dancing
	#singing
	#roughhousing
	#gossiping
	#shaming
	#rhyme games
	#equivocation
	#propagating
	#spreading lies and rumors
	#thanks
	#ignore
	#bye
	#hug

	family_val = 1
	friend_val = 1
	enemy_val = 1
	if receiver in npc.family:
		family_val = npc.family[receiver.id]
	if receiver in npc.friends:
		family_val = npc.friends[receiver.id]
	if receiver in npc.family:
		family_val = npc.enemies[receiver.id]

	values = [ "compliment", "insult", "joke", "story", "question", "small talk", "argue", "ignore", "bye"]
	if influence >= 0:
		#family, friends, foes modifiers
		values = values + [ "compliment" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "compliment" for x in range(1*ceil(friend_val/20)) ]
		values = values + [ "insult" for x in range(2*ceil(enemy_val/20)) ]
		values = values + [ "argue" for x in range(1*ceil(enemy_val/20)) ]
		values = values + [ "question" for x in range(2*ceil(enemy_val/20)) ]
		values = values + [ "advice" for x in range(3*ceil(family_val/20)) ]
		values = values + [ "lament" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "lament" for x in range(1*ceil(friend_val/20)) ]
		values = values + [ "joke" for x in range(1*ceil(friend_val/20)) ]
		values = values + [ "joke" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "story" for x in range(1*ceil(friend_val/20)) ]
		values = values + [ "story" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "thanks" for x in range(2*ceil(family_val/20)) ]
		values = values + [ "thanks" for x in range(3*ceil(friend_val/20)) ]
		values = values + [ "bye" for x in range(3*ceil(enemy_val/20)) ]

		# greetings
		if dialog == "greetings" and past_greetings == False:
			values = values + disList(npc.social, 20, "greetings")
			values = values + disList(npc.social, 20, "greetings")
			values = values + disList(npc.social, 20, "greetings")
		if past_greetings:
			values = values + disList(npc.social, 20, "greetings", m=-1)

		# compliments
		values = values + disList(npc.giving, 80, "compliment", max_val=10)
		values = values + disList(npc.happiness, 90, "compliment")

		# insults
		values = values + disList(npc.open_mindedness, 20, "insult", m=-1)
		values = values + disList(npc.happiness, 10, "insult", m=-1)

		# jokes
		values = values + disList(npc.funnybone, 75, "joke")
		values = values + disList(npc.happiness, 10, "joke", m=-1)
		values = values + disList(npc.happiness, 90, "joke")

		# story
		values = values + disList(npc.happiness, 5, "story", m=-1)
		values = values + disList(npc.happiness, 95, "story")
		values = values + disList(npc.social, 95, "story")
		if dialog == "story":
			values = values + disList(npc.happiness, 10, "story", m=-1)
			values = values + disList(npc.happiness, 90, "story")
			values = values + disList(npc.social, 85, "story")

		# question
		values = values + disList(npc.open_mindedness, 50, "question", max_val=2)
		values = values + disList(npc.open_mindedness, 90, "question", max_val=4)
		if dialog == "story":
			values = values + disList(npc.open_mindedness, 50, "question", max_val=2)
			values = values + disList(npc.open_mindedness, 90, "question", max_val=4)
			values = values + disList(npc.happiness, 20, "question", m=-1, max_val=5)
			values = values + disList(npc.social, 80, "question", max_val=10)
		if dialog == "question":
			values = values + disList(npc.social, 20, "question", m=-1, max_val=10)

		# small talk
		if dialog == "greetings":
			values = values + disList(npc.social, 50, "small talk", max_val=5)
		if dialog == "small talk":
			values = values + disList(npc.social, 50, "small talk", max_val=15)

		# advice
		values = values + disList(npc.funnybone, 33, "advice", m=-1, max_val=2)
		values = values + disList(npc.open_mindedness, 20, "advice", m=-1, max_val=2)
		values = values + disList(npc.open_mindedness, 90, "advice", max_val=2)
		if dialog == "question":
			values = values + disList(npc.funnybone, 33, "advice", m=-1)
			values = values + disList(npc.social, 40, "advice", max_val=10)
			values = values + disList(npc.happiness, 80, "advice", max_val=5)

		# lament
		values = values + disList(npc.happiness, 30, "lament", m=-1, max_val=10)
		values = values + disList(npc.happiness, 10, "lament", m=-1)
		values = values + disList(npc.social, 90, "lament", max_val=5)

		# argue
		if dialog == "joke":
			values = values + disList(npc.funnybone, 10, "argue", m=-1)
		if dialog == "argue":
			values = values + disList(npc.funnybone, 22, "argue", m=-1)
			values = values + disList(npc.happiness, 22, "argue", m=-1)
			values = values + disList(npc.open_mindedness, 33, "argue", m=-1)

		# thanks
		if dialog != "greetings":
			if dialog != "question" and dialog != "argue" and dialog != "insult":
				values = values + disList(npc.happiness, 33, "thanks")
				if dialog == "compliment":
					values = values + disList(npc.happiness, 33, "thanks")
			if dialog == "argue":
				values = values + disList(npc.happiness, 33, "thanks", max_val=5)
				values = values + disList(npc.happiness, 90, "thanks", max_val=5)
			if dialog == "insult":
				values = values + disList(npc.happiness, 90, "thanks", max_val=5)
				values = values + disList(npc.happiness, 22, "thanks", max_val=10, m=-1)
		else:
			values = values + disList(npc.social, 33, "thanks", m=-1, max_val=10)

		# ignore
		if dialog != "greetings":
			values = values + disList(npc.happiness, 5, "ignore", m=-1)
			values = values + disList(npc.social, 20, "ignore", m=-1)
			values = values + disList(npc.open_mindedness, 5, "ignore", m=-1)
			if dialog == "insult" or dialog == "compliment" or dialog == "story":
				values = values + disList(npc.social, 22, "ignore", m=-1)
			if dialog == "question":
				values = values + disList(npc.social, 33, "ignore", m=-1, max_val=10)
		else:
			values = values + disList(npc.social, 33, "ignore", m=-1, max_val=10)

		# bye
		if dialog != "greetings":
			values = values + disList(npc.happiness, 5, "bye", m=-1)
			values = values + disList(npc.social, 20, "bye", m=-1)
			values = values + disList(npc.open_mindedness, 15, "bye", m=-1)
			if dialog == "insult" or dialog == "compliment":
				values = values + disList(npc.social, 60, "bye", max_val=15, m=-1)
			if dialog == "question" or dialog == "story":
				values = values + disList(npc.social, 33, "bye", m=-1, max_val=10)
			if dialog != "question":
				values = values + disList(npc.social, 1, "bye", max_val=10)
		else:
			values = values + disList(npc.social, 33, "bye", m=-1, max_val=10)


	else:
		#family, friends, foes modifiers
		values = values + [ "compliment" for x in range(1*ceil(family_val/40)) ]
		values = values + [ "compliment" for x in range(1*ceil(friend_val/40)) ]
		values = values + [ "story" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "insult" for x in range(4*ceil(enemy_val/20)) ]
		values = values + [ "argue" for x in range(4*ceil(enemy_val/20)) ]
		values = values + [ "question" for x in range(2*ceil(enemy_val/20)) ]
		values = values + [ "lament" for x in range(2*ceil(family_val/20)) ]
		values = values + [ "lament" for x in range(2*ceil(friend_val/20)) ]
		values = values + [ "advice" for x in range(3*ceil(family_val/20)) ]
		values = values + [ "thanks" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "thanks" for x in range(1*ceil(friend_val/20)) ]
		values = values + [ "bye" for x in range(1*ceil(family_val/20)) ]
		values = values + [ "bye" for x in range(2*ceil(friend_val/20)) ]
		values = values + [ "bye" for x in range(5*ceil(enemy_val/20)) ]

		# greetings
		if dialog == "greetings" and past_greetings == False:
			values = values + disList(npc.social, 50, "greetings")
			values = values + disList(npc.social, 50, "greetings")
			values = values + disList(npc.social, 50, "greetings")
		if past_greetings:
			values = values + disList(npc.social, 10, "greetings", m=-1)

		# compliments
		values = values + disList(npc.giving, 95, "compliment")
		values = values + disList(npc.happiness, 95, "compliment")
		values = values + disList(npc.social, 15, "compliment", m=-1)
		values = values + disList(npc.happiness, 5, "compliment", m=-1)
		if dialog == "argue":
			values = values + disList(npc.open_mindedness, 77, "compliment")

		# insults
		values = values + disList(npc.open_mindedness, 50, "insult", m=-1)
		values = values + disList(npc.giving, 66, "insult", m=-1, k=-10)
		values = values + disList(npc.happiness, 40, "insult", m=-1, k=-10)

		# jokes
		values = values + disList(npc.funnybone, 90, "joke")

		# story
		values = values + disList(npc.happiness, 99, "story")
		values = values + disList(npc.social, 97, "story")
		if dialog == "story":
			values = values + disList(npc.happiness, 5, "story", m=-1)
			values = values + disList(npc.happiness, 95, "story")
			values = values + disList(npc.social, 95, "story")

		# question
		values = values + disList(npc.open_mindedness, 30, "question", max_val=5)
		values = values + disList(npc.open_mindedness, 90, "question", max_val=5)
		if dialog == "story":
			values = values + disList(npc.open_mindedness, 30, "question", max_val=2)
			values = values + disList(npc.open_mindedness, 90, "question", max_val=4)
			values = values + disList(npc.happiness, 20, "question", m=-1, max_val=5)
			values = values + disList(npc.social, 80, "question", max_val=10)
		if dialog == "question":
			values = values + disList(npc.social, 20, "question", m=-1, max_val=10)

		# small talk
		if dialog == "small talk":
			values = values + disList(npc.social, 50, "small talk", max_val=5)

		# advice
		if dialog == "question":
			values = values + disList(npc.funnybone, 33, "advice", m=-1, max_val=10)
			values = values + disList(npc.social, 40, "advice", max_val=5)
			values = values + disList(npc.happiness, 80, "advice", max_val=5)

		# lament
		values = values + disList(npc.happiness, 30, "lament", m=-1)
		values = values + disList(npc.happiness, 10, "lament", m=-1)
		values = values + disList(npc.social, 90, "lament", max_val=5)

		# argue
		if dialog == "joke":
			values = values + disList(npc.funnybone, 33, "argue", m=-1)
			values = values + disList(npc.happiness, 33, "argue", m=-1)
		if dialog == "argue":
			values = values + disList(npc.funnybone, 50, "argue", m=-1, max_val=20)
			values = values + disList(npc.happiness, 60, "argue", m=-1, max_val=40)
			values = values + disList(npc.open_mindedness, 66, "argue", m=-1)
		if dialog == "insult":
			values = values + disList(npc.funnybone, 60, "argue", m=-1, max_val=30)
			values = values + disList(npc.happiness, 60, "argue", m=-1, max_val=40)
			values = values + disList(npc.open_mindedness, 66, "argue", m=-1)

		# thanks
		values = values + disList(npc.giving, 90, "thanks")
		values = values + disList(npc.happiness, 85, "thanks")
		values = values + disList(npc.social, 10, "thanks", m=-1)

		# ignore
		values = values + disList(npc.happiness, 10, "ignore", m=-1)
		values = values + disList(npc.social, 33, "ignore", m=-1)
		values = values + disList(npc.open_mindedness, 50, "ignore", m=-1, k=-15)
		if dialog == "insult" or dialog == "compliment" or dialog == "story":
			values = values + disList(npc.social, 33, "ignore", m=-1)
		if dialog == "question":
			values = values + disList(npc.social, 33, "ignore", m=-1)

		# bye
		values = values + disList(npc.happiness, 33, "bye", m=-1)
		values = values + disList(npc.social, 33, "bye", m=-1)
		values = values + disList(npc.open_mindedness, 33, "bye", m=-1)
		values = values + disList(npc.social, 1, "bye", max_val=25)
		if dialog == "insult" or dialog == "compliment" or dialog == "story":
			values = values + disList(npc.social, 60, "bye", max_val=15, m=-1)
		if dialog == "question" or dialog == "greetings":
			values = values + disList(npc.social, 33, "bye", m=-1, max_val=15)

	values = traitsModResponse(npc, values, influence, dialog=dialog)
	print(values)
	shuffle(values)
	#print(values)
	return sample(values, 1)[0]

def interpretDialog(initiator, receiver, dialog_type):
	values = [0]
	influence = 0
	if dialog_type == "greetings":
		happy_mod = modifier(receiver.happiness, 80)
		values = values + [ int(randint(1,2)*happy_mod) if happy_mod > 0 else 1 for x in range(abs(happy_mod)) ]
		happy_mod = modifier(receiver.social, 20)
		values = values + [ int(randint(-2,-1)*happy_mod) if happy_mod < 0 else 1 for x in range(abs(happy_mod)) ]
		influence = choice(values)

	if dialog_type == "compliment":
		happy_mod = modifier(receiver.happiness, 20)
		values = values + [ int(randint(1,2)*happy_mod) if happy_mod > 0 else randint(-5,0) for x in range(abs(happy_mod)) ]
		give_mod = modifier(receiver.giving, 66)	
		values = values + [ randint(-5,0) if give_mod > 0 else int(randint(1,5)-(give_mod/2)) for x in range(abs(give_mod)) ]
		influence = choice(values)
	
	if dialog_type == "insult":
		happy_mod = modifier(receiver.happiness, 20)
		values = values + [ randint(0,5) if happy_mod < 0 else int(randint(-5,0)*happy_mod) for x in range(abs(happy_mod)) ]
		give_mod = distance(receiver.giving, 33)	
		values = values + [ randint(-5,0) if give_mod > 0 else randint(0,5) for x in range(abs(give_mod)) ]
		funny_mod = distance(receiver.funnybone, 85)	
		values = values + [ randint(0,5) for x in range(abs(funny_mod)) if funny_mod > 0 ]
		funny_mod = distance(receiver.funnybone, 95)	
		values = values + [ randint(5,20) for x in range(abs(funny_mod)) if funny_mod > 0 ]
		influence = choice(values)
	
	if dialog_type == "joke":
		happy_mod = modifier(receiver.funnybone, 66)
		values = values + [ randint(1,5) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.funnybone, 88)
		values = values + [ int(randint(1,4)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.happiness, 66)	
		values = values + [ randint(1,5) for x in range(abs(happy_mod)) if happy_mod > 0  ]
		happy_mod = modifier(receiver.funnybone, 33)	
		values = values + [ randint(-5,0) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		happy_mod = modifier(receiver.funnybone, 22)	
		values = values + [ int(randint(-4,-1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		influence = choice(values)
	
	if dialog_type == "story":
		happy_mod = modifier(receiver.funnybone, 77)
		values = values + [ int(randint(1,4)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.happiness, 77)
		values = values + [ int(randint(1,2)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.social, 77)
		values = values + [ int(randint(1,4)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.social, 44)
		values = values + [ int(randint(-1,0)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.social, 22)
		values = values + [ int(randint(-4,-1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.funnybone, 22)	
		values = values + [ int(randint(-4,1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		influence = choice(values)
	
	if dialog_type == "question":
		happy_mod = modifier(receiver.funnybone, 33)
		values = values + [ int(randint(1,5)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.funnybone, 95)
		values = values + [ int(randint(-5,-1)) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.happiness, 77)
		values = values + [ int(randint(1,2)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.social, 77)
		values = values + [ int(randint(1,4)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.social, 44)
		values = values + [ int(randint(-1,0)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.social, 22)
		values = values + [ int(randint(-4,-1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.open_mindedness, 22)	
		values = values + [ int(randint(-4,1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		happy_mod = modifier(receiver.open_mindedness, 75)	
		values = values + [ int(randint(2,3)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0  ]
		influence = choice(values)

	if dialog_type == "small talk":
		happy_mod = modifier(receiver.social, 33)
		values = values + [ int(randint(-5,-1)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.social, 11)
		values = values + [ int(randint(-10,-4)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.social, 75)
		values = values + [ int(randint(0,2)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.happiness, 15)
		values = values + [ int(randint(-5,-1)) for x in range(abs(happy_mod)) if happy_mod < 0 ]

	if dialog_type == "advice":
		happy_mod = modifier(receiver.open_mindedness, 66)
		values = values + [ int(randint(0,5)) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.open_mindedness, 88)
		values = values + [ int(randint(4,10)) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.open_mindedness, 33)
		values = values + [ int(randint(-5,0)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.open_mindedness, 11)
		values = values + [ int(randint(-10,-4)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.giving, 20)
		values = values + [ int(randint(0,5)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.giving, 90)
		values = values + [ int(randint(-5,0)) for x in range(abs(happy_mod)) if happy_mod > 0 ]

	if dialog_type == "advice":
		happy_mod = modifier(receiver.social, 80)
		values = values + [ int(randint(0,2)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.social, 40)
		values = values + [ int(randint(-2,0)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.happiness, 40)
		values = values + [ int(randint(0,2)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.happiness, 40)
		values = values + [ int(randint(-5,0)) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.happiness, 90)
		values = values + [ int(randint(0,5)) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.giving, 77)
		values = values + [ int(randint(0,5)) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.giving, 44)
		values = values + [ int(randint(-5,0)) for x in range(abs(happy_mod)) if happy_mod < 0 ]
		happy_mod = modifier(receiver.funnybone, 80)
		values = values + [ int(randint(-5,0)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]

	if dialog_type == "argue":
		happy_mod = modifier(receiver.open_mindedness, 66)
		values = values + [ randint(0,5) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.open_mindedness, 88)
		values = values + [ int(randint(1,4)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.funnybone, 33)	
		values = values + [ randint(0,5) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		happy_mod = modifier(receiver.funnybone, 66)	
		values = values + [ randint(-10,0) for x in range(abs(happy_mod)) if happy_mod > 0  ]
		happy_mod = modifier(receiver.open_mindedness, 33)	
		values = values + [ randint(-5,0) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		happy_mod = modifier(receiver.open_mindedness, 22)	
		values = values + [ int(randint(-4,-1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		influence = choice(values)

	if dialog_type == "thanks":
		happy_mod = modifier(receiver.happiness, 33)
		values = values + [ int(randint(0,1)*happy_mod/2) if happy_mod > 0 else randint(-5,0) for x in range(abs(happy_mod)) ]
		give_mod = distance(receiver.giving, 33)	
		values = values + [ randint(2,5) for x in range(abs(give_mod)) if (give_mod > 0 and give_mod < 33) ]
		values = values + [ randint(-5,0) for x in range(abs(give_mod)) if give_mod < 0 ]
		influence = choice(values)

	if dialog_type == "ignore":
		soc_mod = distance(receiver.social, 60)	
		values = values + [ randint(-5,0) for x in range(abs(soc_mod)) if soc_mod > 0 ]
		soc_mod = distance(receiver.social, 80)	
		values = values + [ randint(-12,-5) for x in range(abs(soc_mod)) if soc_mod > 0 ]
		soc_mod = distance(receiver.social, 40)	
		values = values + [ randint(0,5) for x in range(abs(soc_mod)) if soc_mod < 0 ]
		soc_mod = distance(receiver.social, 20)	
		values = values + [ randint(5,10) for x in range(abs(soc_mod)) if soc_mod < 0 ]
		influence = choice(values)

	if dialog_type == "bye":
		soc_mod = distance(receiver.social, 80)	
		values = values + [ randint(-5,0) for x in range(abs(soc_mod)) if soc_mod > 0 ]
		soc_mod = distance(receiver.social, 20)	
		values = values + [ randint(0,5) for x in range(abs(soc_mod)) if soc_mod < 0 ]
		influence = choice(values)


	if dialog_type[0] in VOWELS: 
		print(str(initiator.name) + " has influenced " + str(receiver.name) + " with an " + str(dialog_type) + " for " + str(influence) + " points.")
	else:
		print(str(initiator.name) + " has influenced " + str(receiver.name) + " with a " + str(dialog_type) + " for " + str(influence) + " points.")
	
	return influence

def readTheRoom(v1, v2):
	value_1 = 0
	if v2.id in v1.enemies and v1.id in v2.enemies and v2.id in v1.friends and v1.id in v2.friends:
		if v1.enemies[v2.id] > 1:
			value_1 = -1 * v1.enemies[v2.id]
		elif v1.friends[v2.id] > 1:
			value_1 = v1.friends[v2.id]

		value_2 = 0
		if v2.enemies[v1.id] > 1:
			value_2 = -1 * v2.enemies[v1.id]
		elif v2.friends[v1.id] > 1:
			value_2 = v2.friends[v1.id]

		change = float(int(value_1 + value_2) / 2.0)
		adj = 0
		order = [[v1, v2], [v2, v1]]
		for o in order:
			if change > 0:
				if o[0].enemies[o[1].id] > 1:
					adj = int(float(change - o[0].enemies[o[1].id]) / 2.0)
					o[0].enemies[o[1].id] -= adj
					if o[0].enemies[o[1].id] < 1:
						adj = -1 * o[0].enemies[o[1].id]
						o[0].enemies[o[1].id] = 1
						o[0].friends[o[1].id] += adj
				else:
					adj = int(float(change - o[0].friends[o[1].id]) / 2.0)
					o[0].friends[o[1].id] += adj
			elif change < 0:
				change = abs(change)
				if o[0].friends[o[1].id] > 1:
					adj = int(float(change - o[0].friends[o[1].id]) / 2.0)
					o[0].friends[o[1].id] -= adj
					if o[0].friends[o[1].id] < 1:
						adj = -1 * o[0].friends[o[1].id]
						o[0].friends[o[1].id] = 1
						o[0].enemies[o[1].id] += adj
				else:
					adj = int(float(change - o[0].enemies[o[1].id]) / 2.0)
					o[0].enemies[o[1].id] += adj
			if o[0].friends[o[1].id] > 100:
				o[0].friends[o[1].id] = 100
			if o[0].friends[o[1].id] < 1:
				o[0].friends[o[1].id] = 1
			if o[0].enemies[o[1].id] > 100:
				o[0].enemies[o[1].id] = 100
			if o[0].enemies[o[1].id] < 1:
				o[0].enemies[o[1].id] = 1







def modifier(value, center):
	if value > center:
		ret_val = 1 + int((value - center) / 5)
	else:
		ret_val = -1 - int((center - value) / 5)
	return ret_val

def distance(value, center):
	return value - center

def disList(value, center, dialog, k=0, m=1, max_val=100):
	dis = (m * distance(value, center)) + k
	if dis < 0:
		dis = 0
	if dis > max_val:
		dis = max_val
	return [ dialog for x in range(dis) ]

def primeDiagnostics(npc, log_sub_folder):
	if not os.path.exists("logs/" + str(log_sub_folder)):
		os.makedirs("logs/" + str(log_sub_folder))
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "mutations")
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "interactions-sent")
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "interactions-received")
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "friends")
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "enemies")
	fields=['happiness','social','open_mindedness', 'giving', "funnybone"]
	with open("logs/" + str(log_sub_folder) + "/mutations/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'w') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
	fields=['dialog','order','feedback','receiver']
	with open("logs/" + str(log_sub_folder) + "/interactions-sent/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'w') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
	fields=['dialog','order','influence','sender']
	with open("logs/" + str(log_sub_folder) + "/interactions-received/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'w') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
	fields=['npc','friend','iteration','value']
	with open("logs/" + str(log_sub_folder) + "/friends/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'w') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
	fields=['npc','enemy','iteration','value']
	with open("logs/" + str(log_sub_folder) + "/enemies/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'w') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

def printDiagnostics(npc, log_sub_folder):
	fields=[str(npc.happiness),str(npc.social),str(npc.open_mindedness), str(npc.giving), str(npc.funnybone)]
	with open("logs/" + str(log_sub_folder) + "/mutations/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

def updateDiagnosticInteractionSent(npc, dialog, order, feedback, receiver, log_sub_folder):
	fields=[str(dialog),str(order),str(feedback),str(receiver.name)]
	with open("logs/" + str(log_sub_folder) + "/interactions-sent/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

def updateDiagnosticInteractionReceived(npc, dialog, order, influence, sender, log_sub_folder):
	fields=[str(dialog),str(order),str(influence),str(sender.name)]
	with open("logs/" + str(log_sub_folder) + "/interactions-received/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

def updateDiagnosticFriends(npc, friend, i, log_sub_folder):
	fields=[str(npc.name),str(friend.name),str(i),str(npc.friends[friend.id])]
	with open("logs/" + str(log_sub_folder) + "/friends/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

def updateDiagnosticEnemies(npc, enemy, i, log_sub_folder):
	fields=[str(npc.name),str(enemy.name),str(i),str(npc.enemies[enemy.id])]
	with open("logs/" + str(log_sub_folder) + "/enemies/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()