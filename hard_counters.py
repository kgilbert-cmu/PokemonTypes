import Type
from optparse import OptionParser

Counters = []

def main():
	usage = "usage: %prog [options] arg"
	parser = OptionParser()
	parser.add_option("-w", action="store_true", dest="weak",
					help="strong or weak hard counters?")

	(options, args) = parser.parse_args() # user input is stored in "options"
	
	global Counters
	
	for t1 in Type.types: 
		for t2 in Type.types:
			if options.weak and Type.chart[t2].hitBy(t1) > 1:
				# print t1, "\tkills", t2
				Counters.append((t1,t2))
			elif Type.chart[t2].hitBy(t1) > 1 and Type.chart[t1].hitBy(t2) < 1:
				# print t1, "\thard counters", t2
				Counters.append((t1,t2))
		if Type.chart[t1].hitBy(t1) == 0.5:
			# print t1, "resists itself"
			pass
		if Type.chart[t1].hitBy(t1) == 2:
			# print t1, "kills itself"
			pass

if __name__ == "__main__":
    main()
			
HC = {}
for (t1,t2) in Counters:
	if t1 not in HC.keys():
		HC[t1] = [t2]
	else:
		HC[t1].append(t2)
		
HCTypes = [t for t in Type.types if t in HC.keys() and any([t in Ts for Ts in HC.values()])]

triangles = set()

for t1 in HCTypes:
	for t2 in HCTypes:
		for t3 in HCTypes:
			if not (t3 in HC[t1] or t3 in HC[t2]):
				continue
			elif not (t2 in HC[t1] or t2 in HC[t3]):
				continue
			elif not (t1 in HC[t2] or t1 in HC[t3]):
				continue
			else:
				fs = frozenset([t1, t2, t3])
				if len(fs) < 3:
					continue
				triangles.add(fs)

for tri in triangles:
	print tri
