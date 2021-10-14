#!/usr/bin/env python

import sys
import re
import os


stopwords = ['a','about', 'above', 'across','after', 'afterwards', 'again', 'against', 'all',
             'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among',
             'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone',
             'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at','back', 'be',
             'became', 'because','become','becomes','becoming','been','before','beforehand',
             'behind','being','below','beside','besides', 'between','beyond','bill','both', 'bottom',
             'by','can','cannot', 'cant', 'con','could', 'couldnt', 'de','describe', 'detail', 'do', 'done',
             'down', 'due', 'during', 'each', 'eg','eight', 'either', 'eleven', 'else',
             'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every','everyone','everything',
             'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'fire', 'first', 'five', 'for',
             'former', 'formerly', 'forty', 'four', 'from','front', 'full', 'further', 'get','give',
             'go', 'had', 'has', 'hasnt', 'have', 'he','hence', 'her', 'here', 'hereafter', 'hereby',
             'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his','how', 'however',
             'hundred', 'ie', 'if', 'in', 'inc','indeed', 'interest','into', 'is','it','its','itself',
             'keep', 'last', 'latter',   'latterly',   'least', 'less', 'ltd', 'made', 'many',
             'may', 'me','meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most','mostly',
             'move','much', 'must', 'my', 'myself', 'name','namely', 'neither','never','nevertheless',
             'next','nine', 'no']

for line in sys.stdin:
	doc_id = os.environ["map_input_file"]
	
	doc_id = os.path.split(doc_id)[-1]
	
	words = line.rstrip('\n').split()
	
	words = [re.sub('[^A-Za-z0-9]+', '',word.lower()) for word in words]
	
	words = [word for word in words if word not in stopwords]
	
	for word in words:
		print("%s\t%s:1" % (word, doc_id))
	
