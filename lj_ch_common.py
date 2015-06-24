from rdflib import Graph

g = Graph()
g.parse("ch_linkedJazz.nt", format="nt")

len(g) # prints 2

import pprint
for s,p,o in g:
    print(s)