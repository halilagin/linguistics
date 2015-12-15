#!/usr/bin/python



import csv
import sys

class KJVTagger(object):
	def __init__(self):
		#
		self.type = 'KJVTagger'



	def dotag(self):
		if (len(sys.argv)!=3):
			print "%s indice tagname" % (sys.argv[0])
			exit(1)
		self.indice = int(sys.argv[1])
		self.tagname=sys.argv[2]
		with open('../data/kurmanji.verbs.csv', 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for i,row in enumerate(reader):
				verb = row[self.indice]
				if not verb:
					continue
				print "%-16s\t%8s;" % (row[self.indice], self.tagname)




kjvTagger = KJVTagger()

kjvTagger.dotag()
