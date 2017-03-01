from firstPass import firstPass
#from output import output
from validator import validate

'''
inputFile = 'inputs/input_group8.txt'
fin = open( inputFile, 'r' )

numTasks = int( fin.readline() ) #Why was this "eval"? .-.
numMachines = int( fin.readline() )

if numTasks > 1000:
	print( "Error! Too many tasks! " + str( numTasks ) )
if numMachines > 50:
	print( "Error! Too many machines! " + str( numMachines ) )

tasks = [int(t) for t in fin.readline().rstrip().split( ' ' )]
tasksIndex = tasks[:]
#print( tasks )
tasks.sort()

if len( tasksIndex ) != numTasks:
	print( "Error! Number of tasks not equal to actual number!" )

machSpeeds = [int(m) for m in fin.readline().rstrip().split( ' ' ) ]

#machSpeedsIndex = machSpeeds[:]
#machSpeeds.sort() <--sort in firstPass after adding index

#print( machSpeeds )

if len( machSpeeds ) != numMachines :
	print( "Error! Number of machines not equal to actual number!" )

fin.close()


# INSERT FIRST PASS HERE
machines = firstPass(tasks,machSpeeds)
# INSERT SECOND PASS HERE

# INSERT CALC SPEED
output( inputFile, machines, tasksIndex, machSpeedsIndex )

# VALIDATE OUR OWN OUTPUT
validate( inputFile, inputFile.replace( '.txt', 'Out.txt' ) )
'''

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
		runSpeeds = [machine['runtime']/machine['speed'] for machine in machines]
		fout.write(str(max(runSpeeds)) + '\n')

		machines.sort(key = lambda m: m['mach_index'])
		[fout.write(' '.join([str(t['index'] + 1) for t in m['tasks']]) + '\n') for m in machines]

	#validate(inFileName, outFileName)


#theAlgorithm('inputs/input_group1.txt', 'pleaseDearGodWork.txt')