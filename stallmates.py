import Type
import pokemonDB
import sys

stallmates = set()

# i = 0
for pokemon1_t1 in Type.types:
	for pokemon1_t2 in Type.types:
		for pokemon2_t1 in Type.types:
			for pokemon2_t2 in Type.types:
				# sys.stdout.write("\r" + str(i))
				poke1 = frozenset([pokemon1_t1, pokemon1_t2])
				poke2 = frozenset([pokemon2_t1, pokemon2_t2])
				pair = frozenset([poke1,poke2])
				if pair in stallmates:
					continue
				first = [t in Type.resistances(pokemon2_t1, pokemon2_t2) for \
				         t in Type.weaknesses(pokemon1_t1, pokemon1_t2)]
				second = [t in Type.resistances(pokemon1_t1, pokemon1_t2) for \
					      t in Type.weaknesses(pokemon2_t1, pokemon2_t2)]
				if all(first) and all(second):
					# print "Found pair!"
					stallmates.add(pair)
				# i = i + 1
# sys.stdout.write("\n")

for [typing1, typing2] in stallmates:
	try:
		[p1_t1, p1_t2] = typing1
	except:
		p1_t2 = None
	try:
		[p2_t1, p2_t2] = typing2
	except:
		p2_t2 = None
	
	def verify(p1t1, p1t2, p2t1, p2t2):
		first = [t in Type.resistances(p2t1, p2t2) for t in Type.weaknesses(p1t1, p1t2)]
		second = [t in Type.resistances(p1t1, p1t2) for t in Type.weaknesses(p2t1, p2t2)]
		return all(first) and all(second)
	
	if pokemonDB.both(p1_t1, p1_t2, p2_t1, p2_t2) and verify(p1_t1, p1_t2, p2_t1, p2_t2):
		print p1_t1 + "/" + str(p1_t2), "and", p2_t1 + "/" + str(p2_t2)
		print pokemonDB.reverseLookup(p1_t1, p1_t2)
		print "+", pokemonDB.reverseLookup(p2_t1, p2_t2)
		print "--------------------"
