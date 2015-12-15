#!/usr/bin/python


import csv
from Levenshtein import distance
import sys


def rowempty(row):
	for o in row:
		if not o:
			return False
	return True

CSVCOLUMNCOUNT=7
argc =  len(sys.argv)
idx=-1
levenshtein_sums=[]
for i in range(CSVCOLUMNCOUNT):
	levenshtein_sums.append(0)


if argc!=2:
	print( "usage: %s indice"% sys.argv[0] )
	exit(1)
else:
	idx=int(sys.argv[1])

with open('../kurmanji.verbs.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for i,row in enumerate(reader):
		if rowempty(row):
			continue
		if i==0:
			continue
		for col_i in range(CSVCOLUMNCOUNT):
			if idx==0 or idx==1:
				continue
			if col_i==0 or col_i==1:
				continue
			if col_i!=idx:
				levenshtein_sums[col_i] += distance(row[idx],row[col_i])


print levenshtein_sums, sum(levenshtein_sums)
