#!/usr/bin/python

from setuptools import setup

setup(name='kurdishmorph',
      version='0.0.1',
      description='Kurmanji Morphology Analyzer',
      url='http://github.com/halilagin/kurjmorph',
      author='Halil Agin',
      author_email='halil.agin@gmail.com',
      license='MIT',
      packages=['kurdish','kurdish.kurmanji', 'kurdish.kurmanji.verb', 'kurdish.kurmanji.verb.inp'],
      zip_safe=False)
