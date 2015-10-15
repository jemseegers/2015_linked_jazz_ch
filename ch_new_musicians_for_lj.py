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
#print(len(newmusicians))

slist = []

for s,p,o in ch:
	if o in newmusicians:
		slist.append(s)

g = Graph()

for s,p,o in ch:
	if s in slist:
		g.add((s,p,o))
g.serialize("ch_new_musicians_notinlj.nt", format='nt')