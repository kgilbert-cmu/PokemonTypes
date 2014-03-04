types = ["Normal", "Fight", "Flying", "Poison", "Ground",  \
"Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", \
"Electr", "Psychc", "Ice", "Dragon", "Dark", "Fairy"] 

class Type:	
	def __init__(self, weak, resist, immune):
		defend = dict(zip(types,list([1]*len(types))))
		for t in weak:
			defend[t] = 2
		for t in resist:
			defend[t] = 0.5
		for t in immune:
			defend[t] = 0
		self.defend = dict(defend)
	
	def items(self):
		return self.defend.items()
		
	def hitBy(self, type):
		return self.defend[type]
		
chart = {}
chart["Normal"] = Type(["Fight"],[],["Ghost"])
chart["Fight"] = Type(["Flying", "Psychc", "Fairy"],["Rock", "Bug", "Dark"],[])
chart["Flying"] = Type(["Rock", "Electr", "Ice"],["Fight", "Bug", "Grass"],["Ground"])
chart["Poison"] = Type(["Ground", "Psychc"],["Fight", "Poison", "Bug", "Grass", "Fairy"],[])
chart["Ground"] = Type(["Water", "Grass", "Ice"],["Poison", "Rock"],["Electr"])
chart["Rock"] = Type(["Fight", "Ground", "Steel", "Water", "Grass"],["Normal", "Flying", "Poison", "Fire"],[])
chart["Bug"] = Type(["Flying", "Rock", "Fire"],["Fight", "Ground", "Grass"],[])
chart["Ghost"] = Type(["Ghost", "Dark"],["Poison", "Bug"],["Normal", "Fight"])
chart["Steel"] = Type(["Fight", "Ground", "Fire"],["Normal", "Flying", "Rock", "Bug", "Steel", "Grass", "Psychc", "Ice", "Dragon", "Fairy"],["Poison"])
chart["Fire"] = Type(["Ground", "Rock", "Water"],["Bug", "Steel", "Fire", "Grass", "Ice", "Fairy"],[])
chart["Water"] = Type(["Grass", "Electr"],["Steel", "Fire", "Water", "Ice"],[])
chart["Grass"] = Type(["Flying", "Poison", "Bug", "Fire", "Ice"],["Ground", "Water", "Grass", "Electr"],[])
chart["Electr"] = Type(["Ground"],["Flying", "Steel", "Electr"],[])
chart["Psychc"] = Type(["Bug", "Ghost", "Dark"],["Fight", "Psychc"],[])
chart["Ice"] = Type(["Fight", "Rock", "Steel", "Fire"],["Ice"],[])
chart["Dragon"] = Type(["Ice", "Dragon", "Fairy"],["Fire", "Water", "Grass", "Electr"],[])
chart["Dark"] = Type(["Fight", "Bug", "Fairy"],["Ghost", "Dark"],["Psychc"])
chart["Fairy"] = Type(["Poison", "Steel"],["Fight", "Bug", "Dark"],["Dragon"])

def weaknesses(primary, secondary = None):
	p = chart[primary]
	if secondary == None:
		return [k for (k,v) in p.items() if v > 1]
	s = chart[secondary]
	weak = []
	for t in types:
		if p.hitBy(t) * s.hitBy(t) > 1:
			weak.append(t)
	return weak
	
def resistances(primary, secondary = None):
	p = chart[primary]
	if secondary == None:
		return [k for (k,v) in p.items() if v < 1]
	s = chart[secondary]
	weak = []
	for t in types:
		if p.hitBy(t) * s.hitBy(t) < 1:
			weak.append(t)
	return weak
