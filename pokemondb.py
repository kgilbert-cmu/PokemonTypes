import sqlite3

conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

query = "SELECT pokemon.name, types.name \
		 FROM pokemon \
		 JOIN pokemon_types ON (pokemon.id = pokemon_types.pokemon_id) \
		 JOIN types ON (types.id = pokemon_types.type_id)"
c.execute(query)
dump = c.fetchall()

pokes = {}
for (name,type) in dump:
	if name not in pokes.keys():
		pokes[name] = [type]
	else:
		pokes[name].append(type)

typings = {}
for (name,types_list) in pokes.items():
	if len(types_list) == 1:
		types = (types_list[0], None)
	else:
		types = tuple(types_list)
	if types not in typings.keys():
		typings[types] = [name]
	else:
		typings[types].append(name)

def reverseLookup(primary, secondary = None):
	return typings[(primary, secondary)]

def both(p1_t1, p1_t2, p2_t1, p2_t2):
	if (p1_t1, p1_t2) in typings.keys() and (p2_t1, p2_t2) in typings.keys():
		return True
	else:
		return False
