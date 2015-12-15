#!/usr/bin/python



import csv
import sys
import dotag.KJVTagger as KJVTagger 

kjvTagger = KJVTagger.KJVTagger(datafile = "./data/kurmanji.verbs.csv")

kjvTagger.dotag()
