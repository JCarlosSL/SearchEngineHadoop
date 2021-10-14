#!/usr/bin/env python
import sys

index = {}
index_links = {}
d = 0.85

def page_rank(arr):
	r = ((1-d)+d) * sum(arr)
	return r

def is_float(str):
	try:
		float(str)
		return True
	except ValueError:
		return False
		
for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	if is_float(value):
		if key in index:
			index[key].append(float(value))
		else:
			index[key]=[float(value)]
	else:
		if key in index_links:
			index_links[key].append(value)
		else:
			index_links[key]=[value]
	
for key in index:
	new_pr = page_rank(index[key])	
	out_links = ','.join(index_links[key])
	
	print('%s\t%s\t%s' % (key,out_links, new_pr))
		
sys.exit(0)


