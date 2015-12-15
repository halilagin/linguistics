#!/usr/bin/python



import csv
import sys
import kurdish.kurmanji.verb.inp.KJVPretagger as KJVPretagger

def run(cutoff_=10):
	tagnames=["VWishPresent","VWishPast","VImperative","VPresent","VFuture","VPast","VInfinitive"]
	for i in range(7):
		idx_=i
		tagname_=tagnames[i]
		kjvpretagger = KJVPretagger.KJVPretagger(
				indice=idx_,
				cutoff=cutoff_,
				tagname=tagname_,
				inputfile="/home/halil/root/linguistics/morphology-tool/kurjmorph/resources/python.data/kurmanji.verbs.csv",
				outputdir="/home/halil/root/linguistics/morphology-tool/kurjmorph/src/foma/lexicon"
				)
		kjvpretagger.dotag()
