#!/usr/bin/python



import csv
import sys

class KJVPretagger(object):
	def __init__(self,datafile="/home/halil/root/linguistics/morphology-tool/kurjmorph/resources/python.data/kurmanji.verbs.csv"):
		#
		self.type = 'KJVTagger'
		self.datafile=datafile



	def dotag(self):
		if (len(sys.argv)!=3):
			print "%s indice tagname" % (sys.argv[0])
			exit(1)
		self.indice = int(sys.argv[1])
		self.tagname=sys.argv[2]
		with open(self.datafile, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for i,row in enumerate(reader):
				verb = row[self.indice]
				if not verb:
					continue
				print "%-16s\t%8s;" % (row[self.indice], self.tagname)


