
fin = open( 'compInputs.txt', 'r' )

tasks = [ task for task in fin.read().split( '\n' ) ]
fin.close()

tasks.reverse()

fout = open( 'compInputsOut.txt', 'w' )

for task in tasks:
    print( task )
    fout.write( str(task) + ' ' )

fout.close()



