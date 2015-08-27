from rdflib import Graph

ch = Graph()
ch.parse("ch_linkedJazz.nt", format="nt")

lj = Graph()
lj.parse("lj_data.nt", format="nt")

matches = {}

len(ch) # prints 2

import pprint
for s,p,o in ch:
    #print(s)
    for a,b,c in lj:
    	#print(a)
    	#if o == a:
    		#print(a)

		if o not in matches:
			matches[o] = o

		if a not in matches:
			matches[a] = a
				print matches