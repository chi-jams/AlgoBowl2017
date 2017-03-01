from glob import glob

def get_runtimes(dirname):
	files = sorted(glob(dirname + '/*.txt'))
	for f in files:
		with open(f, 'r') as fil:
			runtime = float(fil.readline())
			yield "%.3f" % runtime
		

comp_dirs = ['outputs','test']

runtimes_list = zip(*[get_runtimes(d) for d in comp_dirs])

print('\n'.join('\t'.join(c) for c in list(runtimes_list)))
