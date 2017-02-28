
machineFile = open( 'testInput.txt', 'r' )

numTasks = eval( machineFile.readline() )
numMachines = eval( machineFile.readline() )

tasks = [int(t) for t in machineFile.readline().rstrip().split( ' ' )]
machSpeeds = [int(m) for m in machineFile.readline().split( ' ' ) ]

machineFile.close()

resultsFile = open( 'testInputOut.txt', 'r' )

resultTime = eval( resultsFile.readline() )
print( resultTime )

machLoads = []
for i in range( 0, numMachines ):
    resultLine =  resultsFile.readline().rstrip().split( ' ' )
    if resultLine == ['']:
        machLoads.append( [0] )
    else:
        machLoads.append( [int(t) for t in resultLine ] )
print( machLoads )

machTimes = []

# Calculate the load on each machine
# and get the run time by dividing by the machine speed
for i, load in enumerate( machLoads ):
    totalLoad = 0
    for task in load:
        totalLoad += tasks[task - 1]
    machTimes.append( totalLoad / machSpeeds[i] )

if( max( machTimes ) == resultTime ):
    print( "Output is valid" )
else:
    print( "Output is invalid!" )
