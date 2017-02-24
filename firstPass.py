
def firstPass( tasks, machSpeeds ):
    avgWeight = sum( tasks ) / sum( machSpeeds )

    idealMachWeights = [w * avgWeight for w in machSpeeds]

    machSpeeds2 = [{"max_runtime" : w, "tasks" : []} for w in idealMachWeights]

    for i in reversed(range(len(machSpeeds))):
        if i == 0:
            machSpeeds2[i]['tasks'] = tasks
        else:
            while sum( machSpeeds2[i]['tasks'] ) + tasks[-1] < machSpeeds2[i]['max_runtime']:
                machSpeeds2[i]['tasks'].append(tasks.pop())

    print(machSpeeds2)