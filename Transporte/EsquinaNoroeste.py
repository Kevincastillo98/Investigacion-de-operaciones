import numpy as np

def EsqNor(oferta,demanda,costos):
    #Verificamos que el problema sea balanceado
    assert sum(oferta) == sum(demanda)


print(EsqNor([10,2],[12,0],10))






