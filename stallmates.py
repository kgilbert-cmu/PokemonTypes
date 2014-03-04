import sqlite3

conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

query = "SELECT pokemon.name, types.name \
		 FROM pokemon \
		 JOIN pokemon_types ON (pokemon.id = pokemon_types.pokemon_id) \
		 JOIN types ON (types.id = pokemon_types.type_id) \
		 LIMIT 10"
c.execute(query)
dump = c.fetchall()

pokes = {}
for (name,type) in dump:
	if name not in pokes.keys():
		pokes[name] = [type]
	else:
		pokes[name].append(type)