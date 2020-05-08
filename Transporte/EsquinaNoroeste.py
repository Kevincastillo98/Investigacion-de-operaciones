import numpy as np

def EsqNor(oferta,demanda,costos):
    #Verificamos que el problema sea balanceado
    if sum(oferta) != sum(demanda):
        if sum(oferta) > sum(demanda):
            ## Se agrega una nueva columna con ceros
            demanda = np.append(demanda,(sum(oferta)-sum(demanda)))
        else:
            ## Se agraga nueva fila de ceros
            oferta = np.append(oferta,(sum(demanda)-sum(oferta)))
        
        print(oferta)
        print(demanda)





oferta= np.array([105, 125, 70,20,102])
demanda = np.array([80, 65, 70, 85])

costos = np.array([[9., 10., 13., 17.],
                          [7., 8., 14., 16.],
                          [20., 14., 8., 14.]])

EsqNor(oferta,demanda,costos)




