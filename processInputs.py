from glob import glob
import os

for inputFile in glob('inputs/*.txt'):
	dirname, filename = os.path.split(inputFile)
	outPath = 'outputs/output_' + filename.split('_')[-1]
	with open(outPath, 'w') as fout:
		with open(inputFile, 'r') as fin:
			fout.write(fin.read())