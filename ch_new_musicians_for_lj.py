from rdflib import Graph

ch = Graph()
ch.parse("ch_linkedJazz.nt", format="nt")

lj = Graph()
lj.parse("lj_data.nt", format="nt")

newmusicians = []

len(ch) # prints 2

import pprint
for s,p,o in ch:
		#print(s)
		for a,b,c in lj:
			if o!=a:
				if o not in newmusicians:
					newmusicians.append(o)
					print(newmusicians)