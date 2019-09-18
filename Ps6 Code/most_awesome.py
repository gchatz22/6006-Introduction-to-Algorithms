seen = {}
def most_awesome(C, R):
	'''
    Input: C | list of checkpoint pairs (c, h) with name c and height h
           R | list of route triples (c1, c2, a) for route {c1, c2}, awesome a
    Output:  | list representing a course having maximum awesomeness
    '''
	checks, routes = {}, {}
	global seen
	seen = {}
	best = (0,0)

	for c in C:
		checks[c[0]] = c[1]
		routes[c[0]] = []
	
	for r in R:
		if checks[r[0]]>=checks[r[1]]:
			routes[r[0]].append((r[1],r[2]))
		else:
			routes[r[1]].append((r[0],r[2]))

	for c in checks:
		if c in seen: el = seen[c]
		else:
			el = helper(checks,routes,c)
			seen[c] = el
		if el[1]>best[1]:
			best = el

	print(best)
	return best[0]


def helper(checks, routes, start):

	max_aw = ([start],0)
	recursion = 0

	for route in routes[start]:
		if route[0] in seen: recursion = seen[route[0]]
		else:
			recursion = helper(checks, routes, route[0])
			seen[route[0]] = recursion
		if recursion[1]+route[1] > max_aw[1]: max_aw = (recursion[0],recursion[1]+route[1])
	
	if max_aw!=([start],0): return ([start]+max_aw[0],max_aw[1])
	else: return ([start],0)


C = [("north_summit", 34), ( "west_bluff", 23), ( "eagle_ridge", 17), ("alpine_cliff", 24)]

R=[("alpine_cliff", "north_summit", 22),
    ( "eagle_ridge", "north_summit", 43),
    ("alpine_cliff", "west_bluff", 12),
    (  "west_bluff", "north_summit", 37),
    ( "eagle_ridge",  "west_bluff", 38)]

most_awesome(C,R)
