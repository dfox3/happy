from villager import Villager
from random import randint, choice, sample
import time
import csv
from math import ceil
import datetime
import os
import argparse
#--------------------------------------------------------------------------------------------------
#Command line input parameters
parser = argparse.ArgumentParser(description='Spike-ins Tag Reader')

parser.add_argument('-l',
                    metavar='-log',
                    type=str,
                    default="Jokerfication",
                    help="Log directory name. Overrides automatically generated log directory.")

#--------------------------------------------------------------------------------------------------
#GLOBAL variables
VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

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
	v1 = Villager()
	v2 = Villager(name="Conald", surname="Peter", age=53, social=95, giving=43, happiness=12, 
				  open_mindedness=8, species="Human", sex="male", gender="male", funnybone=40)
	v3 = Villager(name="Ponchis", surname="Gomez", age=28, social=75, giving=25, happiness=25,
				  open_mindedness=50, species="Human", sex="male", gender="male", funnybone=60)
	v4 = Villager(name="Michael", surname="Dizon", age=27, social=80, giving=90, happiness=10,
				  open_mindedness=80, species="Human", sex="male", gender="male", funnybone=63)
	v5 = Villager(name="Emily", surname="Lofaro", age=26, social=65, giving=90, happiness=82,
				  open_mindedness=85, species="Human", sex="female", gender="female", funnybone=58)
	v6 = Villager(name="Ben", surname="Pflughoeft", age=26, social=60, giving=72, happiness=40, 
				  open_mindedness=87, species="Human", sex="male", gender="male", funnybone=81)
	v7 = Villager(name="Emma", surname="", age=99, social=87, giving=99, happiness=93,
				  open_mindedness=50, species="Human", sex="female", gender="female", funnybone=50)
	v8 = Villager(name="Micah", surname="", age=99, social=74, giving=37, happiness=99, 
				  open_mindedness=69, species="Human", sex="male", gender="male", funnybone=89)
	v9 = Villager(name="Dylan", surname="", age=27, social=60, giving=95, happiness=75, 
				  open_mindedness=79, species="Human", sex="male", gender="male", funnybone=90)
	v10 = Villager(name="Jimmy", surname="Stewart", age=25, social=75, giving=50, happiness=25, 
				  open_mindedness=80, species="Human", sex="male", gender="male", funnybone=61)
	v11 = Villager(name="Dom", surname="Misja", age=3, social=15, giving=80, happiness=75, 
				  open_mindedness=25, species="Human", sex="male", gender="male", funnybone=55)
	v12 = Villager(name="Alex", surname="Lukasiewicz", age=4, social=90, giving=80, happiness=80, 
				  open_mindedness=70, species="Human", sex="female", gender="female", funnybone=65)
	v13 = Villager(name="Claire", surname="", age=12, social=90, giving=90, happiness=75, 
				  open_mindedness=65, species="Human", sex="female", gender="female", funnybone=40)
	v14 = Villager(name="Spongebob", surname="Squarepants", age=22, social=90, giving=90, happiness=90, 
				  open_mindedness=90, species="Sea Sponge", sex="male", gender="male", funnybone=90)
	v15 = Villager(name="Patrick", surname="Star", age=31, social=55, giving=50, happiness=95, 
				  open_mindedness=55, species="Starfish", sex="male", gender="male", funnybone=95)
	v16 = Villager(name="Squidward", surname="Tentacles", age=27, social=33, giving=10, happiness=23, 
				  open_mindedness=60, species="Squid", sex="male", gender="male", funnybone=10)
	v17 = Villager(name="Eugene", surname="Krabs", age=51, social=62, giving=1, happiness=40, 
				  open_mindedness=33, species="Crab", sex="male", gender="male", funnybone=52)
	v18 = Villager(name="Pearl", surname="Krabs", age=16, social=95, giving=35, happiness=40, 
				  open_mindedness=40, species="Whale", sex="female", gender="female", funnybone=20)
	v19 = Villager(name="Plankton", surname="", age=35, social=15, giving=5, happiness=5, 
				  open_mindedness=55, species="Plankton", sex="male", gender="male", funnybone=5)
	v20 = Villager(name="Oliver", surname="Nath", age=69, social=70, giving=60, happiness=40, 
				  open_mindedness=70, species="Human", sex="male", gender="male", funnybone=75)
	v21 = Villager(name="Amber", surname="", age=12, social=92, giving=99, happiness=85, 
				  open_mindedness=90, species="Human", sex="female", gender="female", funnybone=55)
	v22 = Villager(name="Kofi", surname="Oduro", age=41, social=92, giving=80, happiness=30, 
				  open_mindedness=12, species="Human", sex="male", gender="male", funnybone=22)
	v23 = Villager(name="Tony", surname="Soprano", age=52, social=64, giving=33, happiness=12, 
				  open_mindedness=40, species="Human", sex="male", gender="male", funnybone=45)

	#npcs = set([ v1, v2, v3, v4, v5 ]
	npcs = [ v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23 ]
	log_sub_folder = options.l
	if log_sub_folder == "Jokerfication":
		log_sub_folder = str(datetime.datetime.now().time()).replace("/","-")
	for n in npcs:
		primeDiagnostics(n, log_sub_folder)
	while True:
		index_list = []
		index_list_2 = []
		for i, n in enumerate(npcs):
			index_list = index_list + [ i for x in range(n.social) ]
			index_list_2 = index_list_2 + [ i for x in range(ceil(n.social/3)) ]
		samples = [choice(index_list)]
		while len(samples) < 2:
		    selection = choice(index_list_2)
		    if selection not in samples:
		        samples.append(selection)
		s1, s2 = interact(npcs[samples[0]], npcs[samples[1]], log_sub_folder)
		npcs[samples[0]] = s1
		npcs[samples[1]] = s2

		for n in npcs:
			printDiagnostics(n, log_sub_folder)

		time.sleep(1)


def interact(v1, v2, log_sub_folder):
	initiator, receiver = initiate(v1, v2)
	dialog = getDialogType(initiator, 1, 1, 1)
	influence_sent = interpretDialog(initiator, receiver, dialog)
	response = getResponseType(receiver, dialog, influence_sent, 1, 1, 1)
	influence_responded = interpretDialog(receiver, initiator, response)
	if initiator.time_init == v1.time_init:
		v2.influence(v1, influence_sent)
		v1.influence(v2, influence_responded)
		updateDiagnosticInteractionSent(v1, dialog, "initiator", influence_sent, v2, log_sub_folder)
		updateDiagnosticInteractionSent(v2, response, "receiver", influence_responded, v1, log_sub_folder)
		updateDiagnosticInteractionReceived(v1, response, "initiator", influence_responded, v2, log_sub_folder)
		updateDiagnosticInteractionReceived(v2, dialog, "receiver", influence_sent, v1, log_sub_folder)
	else:
		v1.influence(v2, influence_sent)
		v2.influence(v1, influence_responded)
		updateDiagnosticInteractionSent(v2, dialog, "initiator", influence_sent, v1,log_sub_folder)
		updateDiagnosticInteractionSent(v1, response, "receiver", influence_responded, v2, log_sub_folder)
		updateDiagnosticInteractionReceived(v2, response, "initiator", influence_responded, v1, log_sub_folder)
		updateDiagnosticInteractionReceived(v1, dialog, "receiver", influence_sent, v2, log_sub_folder)
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


def getDialogType(npc, family_val, friend_val, enemy_val):
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


	#family, friends, foes modifiers
	values = [ "compliment", "insult", "joke", "argue", "thanks", "ignore" ]
	values = values + [ "compliment" for x in range(2*int(family_val/20)) ]
	values = values + [ "compliment" for x in range(2*int(friend_val/20)) ]
	values = values + [ "insult" for x in range(4*int(enemy_val/20)) ]
	values = values + [ "joke" for x in range(2*int(friend_val/20)) ]
	values = values + [ "joke" for x in range(1*int(family_val/20)) ]
	values = values + [ "thanks" for x in range(1*int(family_val/20)) ]
	values = values + [ "thanks" for x in range(1*int(friend_val/20)) ]

	# compliments
	values = values + disList(npc.giving, 67, "compliment")
	values = values + disList(npc.happiness, 67, "compliment")

	# insults
	values = values + disList(npc.open_mindedness, 20, "insult", m=-1)
	values = values + disList(npc.happiness, 33, "insult", m=-1)

	# jokes
	values = values + disList(npc.funnybone, 50, "joke")
	values = values + disList(npc.happiness, 10, "joke", m=-1)
	values = values + disList(npc.happiness, 90, "joke")

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
	#print(values)

	return sample(values, 1)[0]


def getResponseType(npc, dialog, influence, family_val, friend_val, enemy_val):
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
	values = [ "ignore" ]
	if influence >= 0:
		#family, friends, foes modifiers
		values = values + [ "compliment" for x in range(1*int(family_val/20)) ]
		values = values + [ "compliment" for x in range(1*int(friend_val/20)) ]
		values = values + [ "insult" for x in range(2*int(enemy_val/20)) ]
		values = values + [ "joke" for x in range(1*int(friend_val/20)) ]
		values = values + [ "joke" for x in range(1*int(family_val/20)) ]
		values = values + [ "thanks" for x in range(2*int(family_val/20)) ]
		values = values + [ "thanks" for x in range(3*int(friend_val/20)) ]

		# compliments
		values = values + disList(npc.giving, 80, "compliment")
		values = values + disList(npc.happiness, 90, "compliment")

		# insults
		values = values + disList(npc.open_mindedness, 20, "insult", m=-1)
		values = values + disList(npc.happiness, 10, "insult", m=-1)

		# jokes
		values = values + disList(npc.funnybone, 75, "joke")
		values = values + disList(npc.happiness, 10, "joke", m=-1)
		values = values + disList(npc.happiness, 90, "joke")

		# argue
		if dialog == "joke":
			values = values + disList(npc.funnybone, 10, "argue", m=-1)
		if dialog == "argue":
			values = values + disList(npc.funnybone, 22, "argue", m=-1)
			values = values + disList(npc.happiness, 22, "argue", m=-1)
			values = values + disList(npc.open_mindedness, 33, "argue", m=-1)

		# thanks
		values = values + disList(npc.happiness, 33, "thanks")
		if dialog == "compliment":
			values = values + disList(npc.happiness, 33, "thanks")

		# ignore
		values = values + disList(npc.happiness, 5, "ignore", m=-1)
		values = values + disList(npc.social, 20, "ignore", m=-1)
		values = values + disList(npc.open_mindedness, 5, "ignore", m=-1)

	else:
		#family, friends, foes modifiers
		values = values + [ "compliment" for x in range(1*int(family_val/40)) ]
		values = values + [ "compliment" for x in range(1*int(friend_val/40)) ]
		values = values + [ "insult" for x in range(4*int(enemy_val/20)) ]
		values = values + [ "thanks" for x in range(1*int(family_val/20)) ]
		values = values + [ "thanks" for x in range(1*int(friend_val/20)) ]

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

		# argue
		if dialog == "joke":
			values = values + disList(npc.funnybone, 33, "argue", m=-1)
			values = values + disList(npc.happiness, 33, "argue", m=-1)
		if dialog == "argue":
			values = values + disList(npc.funnybone, 50, "argue", m=-1)
			values = values + disList(npc.happiness, 40, "argue", m=-1)
			values = values + disList(npc.open_mindedness, 66, "argue", m=-1)

		# thanks
		values = values + disList(npc.giving, 90, "thanks")
		values = values + disList(npc.happiness, 85, "thanks")
		values = values + disList(npc.social, 10, "thanks", m=-1)

		# ignore
		values = values + disList(npc.happiness, 10, "ignore", m=-1)
		values = values + disList(npc.social, 33, "ignore", m=-1)
		values = values + disList(npc.open_mindedness, 50, "ignore", m=-1, k=-15)
		if dialog == "insult" or dialog == "compliment":
			values = values + disList(npc.social, 33, "ignore", m=-1)

	#print(values)

	return sample(values, 1)[0]

def interpretDialog(initiator, receiver, dialog_type):
	values = [0]
	if dialog_type == "compliment":
		happy_mod = modifier(receiver.happiness, 20)
		values = values + [ int(randint(0,2)*happy_mod) if happy_mod > 0 else randint(-5,0) for x in range(abs(happy_mod)) ]
		give_mod = modifier(receiver.giving, 66)	
		values = values + [ randint(-5,0) if give_mod > 0 else int(randint(0,5)-(give_mod/2)) for x in range(abs(give_mod)) ]
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
		values = values + [ randint(0,5) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.funnybone, 88)
		values = values + [ int(randint(1,4)*happy_mod) for x in range(abs(happy_mod)) if happy_mod > 0 ]
		happy_mod = modifier(receiver.happiness, 66)	
		values = values + [ randint(0,5) for x in range(abs(happy_mod)) if happy_mod > 0  ]
		happy_mod = modifier(receiver.funnybone, 33)	
		values = values + [ randint(-5,0) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		happy_mod = modifier(receiver.funnybone, 22)	
		values = values + [ int(randint(-4,-1)*happy_mod) for x in range(abs(happy_mod)) if happy_mod < 0  ]
		influence = choice(values)

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
		values = values + [ randint(-12,--5) for x in range(abs(soc_mod)) if soc_mod > 0 ]
		soc_mod = distance(receiver.social, 40)	
		values = values + [ randint(0,5) for x in range(abs(soc_mod)) if soc_mod < 0 ]
		soc_mod = distance(receiver.social, 20)	
		values = values + [ randint(5,10) for x in range(abs(soc_mod)) if soc_mod < 0 ]
		influence = choice(values)


	if dialog_type[0] in VOWELS: 
		print(str(initiator.name) + " has influenced " + str(receiver.name) + " with an " + str(dialog_type) + " for " + str(influence) + " points.")
	else:
		print(str(initiator.name) + " has influenced " + str(receiver.name) + " with a " + str(dialog_type) + " for " + str(influence) + " points.")
	
	return influence

def modifier(value, center):
	if value > center:
		ret_val = 1 + int((value - center) / 5)
	else:
		ret_val = -1 - int((center - value) / 5)
	return ret_val

def distance(value, center):
	return value - center

def disList(value, center, dialog, k=0, m=1):
	dis = (m * distance(value, center)) + k
	if dis < 0:
		dis = 0
	return [ dialog for x in range(dis) ]

def primeDiagnostics(npc, log_sub_folder):
	if not os.path.exists("logs/" + str(log_sub_folder)):
		os.makedirs("logs/" + str(log_sub_folder))
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "mutations")
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "interactions-sent")
		os.makedirs("logs/" + str(log_sub_folder) + "/" + "interactions-received")
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


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()