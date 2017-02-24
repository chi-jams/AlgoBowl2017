
def firstPass( tasks, machSpeeds ):
    avgWeight = sum( tasks ) / sum( machSpeeds )

    idealMachWeights = [w * avgWeight for w in machSpeeds]

    machines = [{'max_runtime' : w, 'tasks' : [], 'runtime' : 0} for w in idealMachWeights]

    for i in reversed(range(len(machSpeeds))):
        if i == 0:
            machines[i]['tasks'] = tasks
        else:
            while machines[i]['runtime'] + tasks[-1] < machines[i]['max_runtime']:
                t_task = tasks.pop()
                machines[i]['tasks'].append(t_task)
                machines[i]['runtime'] += t_task

    return machines