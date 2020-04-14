from villager import Villager
from random import randint, choice, sample
import time
import csv
#print(random.randint(0,9))

def main():
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
	v2 = Villager(name="Conald", surname="Peter", age=53, social=88, giving=43, happiness=12, 
				  open_mindedness=8, species="Human", sex="male", gender="male")
	v3 = Villager(name="Ponchis", surname="Gomez", age=28, social=75, giving=25, happiness=25,
				  open_mindedness=50, species="Human", sex="male", gender="male")
	v4 = Villager(name="Michael", surname="Dizon", age=27, social=80, giving=90, happiness=10,
				  open_mindedness=80, species="Human", sex="male", gender="male")
	v5 = Villager(name="Emily", surname="Lofaro", age=26, social=65, giving=90, happiness=82,
				  open_mindedness=85, species="Human", sex="female", gender="female")
	v6 = Villager(name="Ben", surname="Pflughoeft", age=26, social=60, giving=72, happiness=40, 
				  open_mindedness=87, species="Human", sex="male", gender="male")
	v7 = Villager(name="Emma", surname="", age=99, social=87, giving=99, happiness=93,
				  open_mindedness=50, species="Human", sex="female", gender="female")
	v8 = Villager(name="Micah", surname="", age=99, social=74, giving=37, happiness=99, 
				  open_mindedness=69, species="Human", sex="male", gender="male")
	v9 = Villager(name="Dylan", surname="", age=27, social=60, giving=95, happiness=75, 
				  open_mindedness=79, species="Human", sex="male", gender="male")
	v10 = Villager(name="Jimmy", surname="Stewart", age=25, social=75, giving=50, happiness=25, 
				  open_mindedness=80, species="Human", sex="male", gender="male")
	v11 = Villager(name="Dom", surname="Misja", age=3, social=15, giving=80, happiness=75, 
				  open_mindedness=25, species="Human", sex="male", gender="male")
	v12 = Villager(name="Alex", surname="Lukasiewicz", age=4, social=90, giving=80, happiness=80, 
				  open_mindedness=70, species="Human", sex="female", gender="female")
	v13 = Villager(name="Claire", surname="", age=12, social=90, giving=90, happiness=75, 
				  open_mindedness=65, species="Human", sex="female", gender="female")
	v14 = Villager(name="Spongebob", surname="Squarepants", age=22, social=90, giving=90, happiness=90, 
				  open_mindedness=90, species="Sea Sponge", sex="male", gender="male")
	v15 = Villager(name="Patrick", surname="Star", age=31, social=55, giving=50, happiness=95, 
				  open_mindedness=55, species="Starfish", sex="male", gender="male")
	v16 = Villager(name="Squidward", surname="Tentacles", age=27, social=33, giving=10, happiness=23, 
				  open_mindedness=60, species="Squid", sex="male", gender="male")
	v16 = Villager(name="Eugene", surname="Krabs", age=51, social=62, giving=1, happiness=40, 
				  open_mindedness=33, species="Crab", sex="male", gender="male")
	v16 = Villager(name="Pearl", surname="Krabs", age=16, social=95, giving=35, happiness=40, 
				  open_mindedness=40, species="Whale", sex="female", gender="female")
	v16 = Villager(name="Plankton", surname="", age=35, social=15, giving=5, happiness=5, 
				  open_mindedness=55, species="Plankton", sex="male", gender="male")
	#social 65
	#happy 82
	#open mindedness 85
	#giving 90
	print(v1.printBio())
	print(v2.printBio())
	print(v3.printBio())
	print(v4.printBio())
	print(v5.printBio())
	#npcs = set([ v1, v2, v3, v4, v5 ]
	npcs = [ v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13 ]
	for n in npcs:
		primeDiagnostics(n)
	while True:
		#npcs = [ v1, v2, v3, v4, v5, v6, v7, v8, v9 ]
		#npcs = [ v2, v6 ]
		#npcs = [ v7, v8 ]
		index_list = [ x for x in range(len(npcs)) ]
		samples = sample(index_list, 2)
		s1, s2 = interact(npcs[samples[0]], npcs[samples[1]])
		npcs[samples[0]] = s1
		npcs[samples[1]] = s2

		for n in npcs:
			printDiagnostics(n)

		time.sleep(15)


def interact(v1, v2):
	initiator, receiver = initiate(v1, v2)
	if initiator.time_init == v1.time_init:
		response, influence = sendDialog(v1, v2)
		v2.influence(v1, influence)
		interpretResponse(v1, response)
	else:
		response, influence = sendDialog(v2, v1)
		v1.influence(v2, influence)
		interpretResponse(v2, response)
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

def sendDialog(initiator, receiver):
	dialog_type = getDialogType(initiator)
	response = ""
	influence = 0
	if dialog_type == "compliment":
		#soc_dis = distance(receiver.social, 33)
		#values = [ randint(0,7) if soc_dis > 0 else randint(-5,0) for x in range(abs(soc_dis)) ]
		happy_mod = modifier(receiver.happiness, 20)
		values = [ int(randint(0,5)*happy_mod) if happy_mod > 0 else randint(-7,0) for x in range(abs(happy_mod)) ]
		give_mod = distance(receiver.giving, 66)	
		values = values + [ randint(-3,0) if give_mod > 0 else int(randint(0,5)-(give_mod/2)) for x in range(abs(give_mod)) ]
		influence = choice(values)
		print(str(initiator.name) + " has influenced " + str(receiver.name) + " with a " + str(dialog_type) + " for " + str(influence) + " points.")
	
	if dialog_type == "insult":
		happy_mod = modifier(receiver.happiness, 20)
		values = [ int(randint(0,2)*happy_mod) if happy_mod < 0 else randint(-7,0) for x in range(abs(happy_mod)) ]
		give_mod = distance(receiver.giving, 33)	
		values = values + [ randint(-6,0) if give_mod > 0 else randint(0,2) for x in range(abs(give_mod)) ]
		influence = choice(values)
		print(str(initiator.name) + " has influenced " + str(receiver.name) + " with a " + str(dialog_type) + " for " + str(influence) + " points.")
	


	return response, influence

def getDialogType(villager):
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


	values = [ "compliment" for x in range(5) ]
	values = values + [ "insult" for x in range(5) ]
	# compliments
	giv_dis = distance(villager.giving, 67)
	if giv_dis < 0:
		giv_dis = 0
	values = values + [ "compliment" for x in range(giv_dis) ]
	hap_dis = distance(villager.happiness, 67)
	if hap_dis < 0:
		hap_dis = 0
	values = values + [ "compliment" for x in range(hap_dis) ]
	opm_dis = -1 * distance(villager.open_mindedness, 20)
	if opm_dis < 0:
		opm_dis = 0
	# insults
	values = values + [ "insult" for x in range(opm_dis) ]
	uhp_dis = -1 * distance(villager.happiness, 33)
	if uhp_dis < 0:
		uhp_dis = 0
	values = values + [ "insult" for x in range(uhp_dis) ]
	print(values)
	return sample(values, 1)[0]

def interpretResponse(initator, response):
	return

def modifier(value, center):
	if value > center:
		ret_val = 1 + int((value - center) / 5)
	else:
		ret_val = -1 - int((center - value) / 5)
	return ret_val

def distance(value, center):
	return value - center


def primeDiagnostics(npc):
	fields=['happiness','social','open_mindedness', 'giving']
	with open("logs/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'w') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

def printDiagnostics(npc):
	fields=[str(npc.happiness),str(npc.social),str(npc.open_mindedness), str(npc.giving)]
	with open("logs/" + str(npc.name) + "_" + str(npc.time_init) + ".csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()