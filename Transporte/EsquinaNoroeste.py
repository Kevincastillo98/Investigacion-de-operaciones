import numpy as np

def EsqNor(oferta,demanda,costos):
    #Verificamos que el problema sea balanceado
    if sum(oferta) != sum(demanda):
        print("Problema no balanceado\n")
        if sum(oferta) > sum(demanda):
            demanda = np.append(demanda,(sum(oferta)-sum(demanda)))
            ## Se agrega  la variable artificial como columna
            var_artificial = np.zeros(costos.shape[0])
            costos = np.column_stack((costos,var_artificial))
            print("Se balanceara\n")

        else:
            oferta = np.append(oferta,(sum(demanda)-sum(oferta)))
            ## Se agrega la variable artificial como fila
            var_artificial = np.zeros(costos.shape[1])
            costos = np.row_stack((costos,var_artificial))
            print("Se balanceara\n")
    else:
        print("Problema balanceado\n")
    

    print("Oferta:" ,oferta)
    print("Demanda: ",demanda)
    print("Costos:\n", costos)




demanda = np.array([250,250,100])
oferta = np.array([100,200,150,100])

costos = np.array([[50, 78, 85, 20.],
                          [40,35, 100, 90],
                          [55, 25, 60, 80]])

EsqNor(oferta,demanda,costos)






