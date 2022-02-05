entradas = [1, 1 , -5]
pesos = [0.1, 0.4, 0.4]

def soma(inputs, wights) : 
    soma = 0;
    for i in range(3) : 
        soma += inputs[i] * wights[i]
    return soma       

def stepFunction(sinapse) :
    if sinapse >= 1 :
        return 1
    return 0

stepFunction(soma(entradas, pesos))
