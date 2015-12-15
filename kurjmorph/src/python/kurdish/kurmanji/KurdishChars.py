#!/usr/bin/python
# -*- coding: utf-8 -*- 


class KurdishAlphabet(object):
	def __init__(self):
		self.type="KurdishChars"
		self.alphabet = ['a','b','c','ç','d','e','ê','f','g','h','i','î','j','k','l','m','n','o','p','q','r','s','ş','t','u','û','v','x','w','y','z']
		self.vowels = ['a','e','ê','i','î','o','u','û']
		self.consonants = ['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','ş','t','v','x','w','y','z']
	def show(self):
		print "alphabet.size:%d\nalphabet.vowels.size:%d\nalphabet.consonants.size:%d" % (len(self.alphabet),len(self.vowels), len(self.consonants))


krd = KurdishAlphabet()
krd.show()
