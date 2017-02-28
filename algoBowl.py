from firstPass import firstPass
from output import output

inputFile = 'testInput.txt'
fin = open( inputFile, 'r' )

numTasks = eval( fin.readline() )
numMachines = eval( fin.readline() )

tasks = [int(t) for t in fin.readline().split( ' ' )]
tasksIndex = tasks[:]
#print( tasks )
tasks.sort()

machSpeeds = [int(m) for m in fin.readline().split( ' ' ) ]
machSpeedsIndex = machSpeeds[:]
machSpeeds.sort()
#print( machSpeeds )
fin.close()


# INSERT FIRST PASS HERE
machines = firstPass(tasks,machSpeeds)
# INSERT SECOND PASS HERE

# INSERT CALC SPEED
output( inputFile, machines, tasksIndex, machSpeedsIndex )