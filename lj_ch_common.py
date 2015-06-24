from rdflib import Graph

ch = Graph()
ch.parse("ch_linkedJazz.nt", format="nt")

lj = Graph()
lj.parse("lj_data.nt", format="nt")

len(ch) # prints 2

import pprint
for s,p,o in ch:
    print(s)
    for a,b,c in lj:
    	print(a)