
def firstPass( tasks, machSpeeds ):
    avgWeight = sum( tasks ) / sum( machSpeeds )

    idealMachWeights = [w * avgWeight for w in machSpeeds]

    machines = [{'mach_index' : i, 'max_runtime' : w, 'speed' : machSpeeds[i], 'tasks' : [], 'runtime' : 0} for i,w in enumerate(idealMachWeights)]
    machines.sort(key = lambda m: m['speed'])

    tasks = [{'runtime' : r, 'index' : i} for i,r in enumerate(tasks)]
    tasks.sort( key = lambda t: t['runtime'])

    '''
    for i in reversed(range(len(machines))):
        if i == 0:
            machines[i]['tasks'] = tasks
            machines[i]['runtime'] = sum(t['runtime'] for t in tasks)
        else:
            while machines[i]['runtime'] < machines[i]['max_runtime']:
                if not tasks:
                    return machines

                t_task = tasks.pop()
                machines[i]['tasks'].append(t_task)
                machines[i]['runtime'] += t_task['runtime']
    '''
    for i in reversed(range(len(machines))):
        if tasks:
            next_task = tasks.pop()
            machines[i]['tasks'].append( next_task )
            machines[i]['runtime'] += next_task['runtime']

        if tasks != []:
            next_task = tasks[-1]
            while machines[i]['runtime'] + next_task['runtime'] < machines[i]['max_runtime']:
                if tasks:
                    next_task = tasks.pop()
                    machines[i]['tasks'].append(next_task)
                    machines[i]['runtime'] += next_task['runtime']
                else:
                    break

    if tasks:
        remainingTasks = [t['runtime'] for t in tasks]
        subMachines = firstPass( remainingTasks, machSpeeds )
        for i in range( len( machines ) ):
            machines[i]['tasks'] += subMachines[i]['tasks']
    
    return machines
