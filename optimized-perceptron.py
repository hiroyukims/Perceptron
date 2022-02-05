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

#todo: implement train function
def train() : 
    return 0
