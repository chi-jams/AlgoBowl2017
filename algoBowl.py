from firstPass import firstPass
from output import output
from validator import validate

inputFile = 'inputs/input_group8.txt'
fin = open( inputFile, 'r' )

numTasks = eval( fin.readline() )
numMachines = eval( fin.readline() )

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
machSpeedsIndex = machSpeeds[:]
machSpeeds.sort()
#print( machSpeeds )

if len( machSpeedsIndex ) != numMachines :
    print( "Error! Number of machines not equal to actual number!" )

fin.close()


# INSERT FIRST PASS HERE
machines = firstPass(tasks,machSpeeds)
# INSERT SECOND PASS HERE

# INSERT CALC SPEED
output( inputFile, machines, tasksIndex, machSpeedsIndex )

# VALIDATE OUR OWN OUTPUT
validate( inputFile, inputFile.replace( '.txt', 'Out.txt' ) )