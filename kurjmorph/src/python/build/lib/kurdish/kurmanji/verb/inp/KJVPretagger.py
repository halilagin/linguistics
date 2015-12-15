#!/usr/bin/python



import csv
import sys

class KJVPretagger(object):
	def __init__(self,
			indice=0,
			cutoff=10,
			tagname="DummyTag",
			inputfile="/home/halil/root/linguistics/morphology-tool/kurjmorph/resources/python.data/kurmanji.verbs.csv", 
			outputdir="/home/halil/root/linguistics/morphology-tool/kurjmorph/src/foma/lexicon", 
			):
		#
		self.type_ = 'KJVPretagger'

		self.indice=indice
		self.cutoff=cutoff
		self.tagname=tagname
		self.inputfile=inputfile
		self.outputdir=outputdir
		if self.cutoff!=1000000:
			self.filename="kurmanji."+self.tagname+"."+str(self.cutoff)
		else:   
			self.filename="kurmanji."+self.tagname
		self.filepath = self.outputdir + "/" + self.filename



	def dotag(self):
		out = open(self.filepath, 'w')
		with open(self.inputfile, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='|')
			counter=0
			for i,row in enumerate(reader):
				if i==0:
					continue
				verb = row[self.indice]
				if not verb:
					continue
				line =  "%-16s\t%8s;\n" % (row[self.indice], self.tagname)
				out.write(line)
				counter+=1
				if counter==self.cutoff:
					break
		out.close()

	def cmd(self):
		if (len(sys.argv)!=4):
			print "%s indice cutoff tagname" % (sys.argv[0])
			exit(1)
		self.indice = int(sys.argv[1])
		self.cutoff=int(sys.argv[2])
		self.tagname=sys.argv[3]
		#self.inputfile= default one
		#self.outputdir= default one
		self.filepath = self.outputdir + "/" + self.filename
		self.dotag()
		


