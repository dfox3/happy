from villager import Villager
from random import randint, choice, sample, shuffle
import time
import csv
from math import ceil
import datetime
import os
import argparse
from itertools import combinations
from traits_categories import *
#--------------------------------------------------------------------------------------------------


def traitsModInteract(npc, npcs, i_list):
	npc_mods = [ t for t in npc.traits if t in INTERACT ]
	for t in npc_mods:

		if t == "stalker":
			i_list = []
			for i, n in enumerate(npcs):
				i_list.append(i)
				if n != npc and n.name == npc.traits["stalker"]:
					i_list = i_list + [ i for n in range(100) ]

		if t == "boys club":
			i_list = []
			for i, n in enumerate(npcs):
				i_list.append(i)
				if n != npc and n.sex == "male":
					i_list = i_list + [ i for n in range(20) ]

		if t == "girls club":
			i_list = []
			for i, n in enumerate(npcs):
				i_list.append(i)
				if n != npc and n.sex == "female":
					i_list = i_list + [ i for n in range(20) ]

		if t == "cliquey":
			i_list = []
			top_friends = npc.getTopFriends()
			for i, n in enumerate(npcs):
				i_list.append(i)
				if n != npc and n.id in top_friends:
					i_list = i_list + [ i for n in range(10) ]

		if t == "menace":
			i_list = []
			for i, n in enumerate(npcs):
				i_list.append(i)
				if n != npc and n.id in npc.enemies:
					i_list = i_list + [ i for n in range(10) ]

	return i_list

def traitsModInitiate():
	return

def traitsModResponse(npc, values, influence, dialog=""):
	npc_mods = [ t for t in npc.traits if t in RESPONSE ]
	for t in npc_mods:

		if t == "short fuse":
			if influence < 0:
				values = values + [ "insult" for i in range(25) ]
				values = values + [ "argue" for i in range(10) ]

		if t == "cte":
			values = values + [ npc.last_interaction_sent for i in range(10) ]
		
		if t == "pedantic":
			values = values + [ "argue" for i in range(10) ]

		if t == "mute":		
			# ignore
			values = [ "ignore" for x in range(5) ]
			values = values + disList(npc.happiness, 10, "ignore", m=-1)
			values = values + disList(npc.social, 33, "ignore", m=-1)
			values = values + disList(npc.open_mindedness, 50, "ignore", m=-1, k=-15)
			if dialog == "insult" or dialog == "compliment" or dialog == "story":
				values = values + disList(npc.social, 33, "ignore", m=-1)
			if dialog == "question":
				values = values + disList(npc.social, 33, "ignore", m=-1)

		if t == "clown":
			values = values + [ "joke" for i in range(30) ]
			values = values + [ "lament" for i in range(10) ]

		if t == "agreeable":
			if dialog == "argue":
				values = ["bye"]
				values = values + disList(npc.happiness, 10, "ignore", m=-1)
				values = values + disList(npc.social, 33, "ignore", m=-1)
				values = values + disList(npc.social, 33, "compliment", max_val=20)
				values = values + disList(npc.social, 70, "happiness", max_val=20)
				values = values + disList(npc.social, 33, "thanks", max_val=20)
				values = values + disList(npc.social, 33, "bye", max_val=20)


			
	return values

'''
def traitsModInfluence(npc, other, changes, influence, dialog):
	moved to illager.py to avoid circular logic
'''

def traitsModInterpret():
	return

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


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()