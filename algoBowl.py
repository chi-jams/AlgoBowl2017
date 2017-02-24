
fin = open( 'testInput.txt', 'r' )

numTasks = eval( fin.readline() )
numMachines = eval( fin.readline() )

print( numTasks )
print( numMachines )

tasks = fin.readline()
tasks = tasks.split( ' ' )
for i in range( len( tasks ) ):
    tasks[i] = int( tasks[i] )

print( tasks )

machSpeeds = fin.readline()
machSpeeds = machSpeeds.split( ' ' )
for i in range( len( machSpeeds ) ):
    machSpeeds[i] = int( machSpeeds[i] )

print( machSpeeds )


fin.close()