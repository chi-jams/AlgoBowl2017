
def output( machines, tasksIndex, machSpeedsIndex ):
    runSpeeds = [ machine['runtime']/machine['speed'] for machine in machines ]
    print( max( runSpeeds ) )
    print( tasksIndex )
    print( machSpeedsIndex )

    
    for machine in machines:
        for task in machine['tasks']:
            print( tasksIndex.index( task ) + 1, end = ' ' )
        print()

