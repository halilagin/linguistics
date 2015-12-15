#!/usr/bin/python



import csv
import sys
#import kurmanji.verb.inp.KJVPretagger as KJVPretagger
import kurdish.kurmanji.verb.inp.KJVPretagger as KJVPretagger

kjvpretagger = KJVPretagger.KJVPretagger()

kjvpretagger.dotag()
