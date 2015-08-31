from rdflib import Graph

ch = Graph()
ch.parse("ch_linkedJazz.nt", format="nt")

lj = Graph()
lj.parse("lj_data.nt", format="nt")

matches = []

len(ch) # prints 2

import pprint
for s,p,o in ch:
    #print(s)
    for a,b,c in lj:
   		if o==a:
   			
   			if o not in matches:
   				matches.append(o)
#print(len(matches))

slist = []

for s,p,o in ch:
	if o in matches:
		slist.append(s)

g = Graph()

for s,p,o in ch:
	if s in slist:
		g.add((s,p,o))
g.serialize("ch_lj_matches.nt", format='nt')