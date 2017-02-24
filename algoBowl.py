from firstPass import firstPass
fin = open( 'testInput.txt', 'r' )

numTasks = eval( fin.readline() )
numMachines = eval( fin.readline() )

tasks = [int(t) for t in fin.readline().split( ' ' )]
print( tasks )
tasks.sort()

machSpeeds = [int(m) for m in fin.readline().split( ' ' ) ]
machSpeeds.sort()
print( machSpeeds )
fin.close()


# INSERT FIRST PASS HERE
firstPass(tasks,machSpeeds)
# INSERT SECOND PASS HERE

# INSERT CALC SPEED