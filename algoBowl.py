from firstPass import firstPass
#from output import output
from validator import validate

def theAlgorithm(inFileName, outFileName):
	with open(inFileName, 'r') as fin:
		numTasks = int(fin.readline())
		numMachines = int(fin.readline())

		if numTasks > 1000:
			print("Error! Too many tasks! " + str(numTasks))
		if numMachines > 50:
			print("Error! Too many machines! " + str(numMachines))

		tasks = [int(t) for t in fin.readline().rstrip().split( ' ' )]
		#tasks.sort()


		machSpeeds = [int(m) for m in fin.readline().rstrip().split( ' ' ) ]

	if len(tasks) != numTasks:
		print("Error! Number of tasks not equal to actual number!")

	if len( machSpeeds ) != numMachines:
		print( "Error! Number of machines not equal to actual number!" )

	machines = firstPass(tasks,machSpeeds)

	with open(outFileName, 'w') as fout:
		print('\n'.join(str(m) for m in machines))
		runSpeeds = [float(sum(t['runtime'] for t in machine['tasks']))/float(machine['speed']) for machine in machines]
		fout.write(str(max(runSpeeds)) + '\n')

		machines.sort(key = lambda m: m['mach_index'])
		[fout.write(' '.join([str(t['index'] + 1) for t in m['tasks']]) + '\n') for m in machines]

	validate(inFileName, outFileName)

theAlgorithm('inputs/input_group10.txt', 'pleaseDearGodWork.txt')