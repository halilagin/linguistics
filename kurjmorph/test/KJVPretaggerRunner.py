#!/usr/bin/python



import csv
import sys
#import kurmanji.verb.inp.KJVPretagger as KJVPretagger
import kurdish.kurmanji.verb.inp.KJVPretaggerRunner as KJVPretaggerRunner

#KJVPretaggerRunner.run(10)
KJVPretaggerRunner.runPastTenseFomaGenerator(1000000,"VerbStems.foma")

