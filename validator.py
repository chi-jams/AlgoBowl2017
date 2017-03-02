
def validate( problem, solution ):
    machineFile = open( problem, 'r' )
    resultsFile = open( solution, 'r' )

    numTasks = eval( machineFile.readline() )
    numMachines = eval( machineFile.readline() )

    tasks = [int(t) for t in machineFile.readline().rstrip().split( ' ' )]
    machSpeeds = [int(m) for m in machineFile.readline().rstrip().split( ' ' ) ]

    machineFile.close()

    resultTime = eval( resultsFile.readline() )

    machLoads = []
    for i in range( 0, numMachines ):
        resultLine =  resultsFile.readline().rstrip().split( ' ' )
        if resultLine == ['']:
            machLoads.append( [0] )
        else:
            machLoads.append( [int(t) for t in resultLine ] )
    resultsFile.close()

    machTimes = []

    # Calculate the load on each machine
    # and get the run time by dividing by the machine speed
    for i, load in enumerate( machLoads ):
        totalLoad = 0
        for task in load:
            totalLoad += tasks[task - 1]
        machTimes.append( totalLoad / machSpeeds[i] )

    '''
    timeWasted = 0
    maxTime = max( machTimes )
    for time in machTimes:
        timeWasted += maxTime - time
    print( str( timeWasted ) + " clock cycles wasted" )

    targetEfficiency = 0
    idealUnit = sum( tasks ) / sum( machSpeeds )

    print( 'Toal task weight: ' + str( sum( tasks ) ) )
    idealLoads = [ idealUnit * speed for speed in machSpeeds ]
    for i in range( 0, len( idealLoads ) ):
        #print( idealLoads[i], machTimes[i] * machSpeeds[i] )
        targetEfficiency += abs( idealLoads[i] - ( machTimes[i] * machSpeeds[i] ) )
    print( str( targetEfficiency ) + " cycles away from theoretical optimal" )
    '''

    if( max( machTimes ) != resultTime ):
        print( "Output is invalid!" )
        print( max( machTimes ), resultTime )

for i in range( 1, 23 ):

    print( "Task " + str(i) + ":" )
    validate( "compInputs.txt", "other groups/output_from_" + str(i) + "_to_3.txt" )