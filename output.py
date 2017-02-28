
def output( inputFile, machines, tasksIndex, machSpeedsIndex ):
    fout = open( inputFile.replace( '.txt', 'Out.txt' ), 'w' )

    runSpeeds = [ machine['runtime']/machine['speed'] for machine in machines ]
    print( max( runSpeeds ) )
    fout.write( str( max( runSpeeds ) ) + '\n' )
    #print( tasksIndex )
    #print( machSpeedsIndex )

    for speed in machSpeedsIndex:
        machineIndex = -1
        for i in range( 0, len( machines ) ):
            if machines[i]['speed'] == speed:
                machineIndex = i
                break
        # Change the machine speed to an inviable number so it can't
        # be found again
        machines[machineIndex]['speed'] = -1

        for task in machines[machineIndex]['tasks']:
            taskIndex = str( tasksIndex.index( task ) + 1 )
            print( taskIndex, end = ' ' )
            fout.write( taskIndex + ' ' )
        print()
        fout.write( '\n' )
