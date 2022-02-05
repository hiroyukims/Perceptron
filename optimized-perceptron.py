# Supervised Learning
# Classification algorithm

import numpy as np

inputs = np.array([0,0],[0,1],[1,0],[1,1])
outputs = np.array([0, 0, 0, 1])
weights = np.array([0.0, 0.0])
larningRate = 0.1

def stepFunction(sum) : 
    if(sum >= 1) :
        return 1
    return 0

def calcOutput(register) :
    sum = register.dot(weights)
    return stepFunction(sum)

def train() : 
    totalErrors = 1
    while(totalErrors != 0) : 
        totalErrors = 0
        for i in range(len(outputs)) :
            calculetedOutput = calcOutput(np.asarray(inputs[i]))
            error = abs(outputs[i] - calculetedOutput)
            totalErrors +=  error
            # update weights
            for j in range(len(weights)) : 
                weights[j] = weights[j] + (larningRate * inputs[i][j] * error) 
    return 0

train()
