from glob import glob
from algoBowl import theAlgorithm
import os

for inputFile in glob('inputs/*.txt'):
	dirname, filename = os.path.split(inputFile)
	outputFile = 'outputs/output_' + filename.split('_')[-1]
	theAlgorithm(inputFile, outputFile)