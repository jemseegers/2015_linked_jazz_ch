import re
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
					#print(newmusicians)

import json

with open ("newbies_to_lj.json", "w") as g:
	g.write(json.dumps(newmusicians, indent=4))



#convert list into string for regex. Add space between each object to assist compile
# 					chstring = ' '.join(newmusicians)

# #print (newmusicians)

# #compile pattern to find only names (The names appear to all start with capital letters,
# #and I don't see any other capital letters in the CH data set of name URIs. So this pulls out
# #a string from the first capital letter until a space, which you now have between each URI)

# 					x = re.compile('([A-X][^\s]+)')

# #search method
# 					m = x.findall(chstring)

# 					for person in m:
# 					    print (person)


#you may have to refine the regular expression parameters, but that was my idea on how to isolate
#these names.