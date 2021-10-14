#!/usr/bin/env python
import sys

index = {}
for line in sys.stdin:
	values = line.rstrip('\n').split()

	if values[0] in index:
		index[values[0]].append(values[1])
	else:
		index[values[0]] = [values[1]]

for word in index:
	len_words = len(index[word])
	for i in range(len_words):
		print('%s\t%s' % (word, index[word][i]))
		vote = float(1.0 / len_words)
		print('%s\t%s' % (index[word][i], vote))

sys.exit(0)
