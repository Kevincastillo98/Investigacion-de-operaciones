import numpy as np


def EsqNor(oferta, demanda, costos):
    # Verificamos que el problema sea balanceado
    if sum(oferta) != sum(demanda):
        print("Problema no balanceado\n")
        if sum(oferta) > sum(demanda):
            demanda = np.append(demanda, (sum(oferta)-sum(demanda)))
            # Se agrega  la variable artificial como columna
            var_artificial = np.zeros(costos.shape[0])
            costos = np.column_stack((costos, var_artificial))
            print("Se balanceara\n")
        else:
            oferta = np.append(oferta, (sum(demanda)-sum(oferta)))
            # Se agrega la variable artificial como fila
            var_artificial = np.zeros(costos.shape[1])
            costos = np.row_stack((costos, var_artificial))
            print("Se balanceara\n")
    else:
        print("Problema balanceado\n")

    print("Oferta:", oferta)
    print("Demanda: ", demanda)
    print("Costos:\n", costos)

    # Primero tomamos como pivote al elemento X_{00}
    matriz_asigna = costos
    matriz_asigna = np.zeros(costos.shape)
    # Numero de filas
    filas = matriz_asigna.shape[1]
    # Numero de columnas
    columnas = matriz_asigna.shape[0]
    # X_{ij} -> matriz de costos
    # a_{i}  -> matriz de demanda
    # b_{j}  -> matriz de ofertas
    i = 0
    j = 0

    matriz_asigna[0][0] = np.minimum(oferta[0], demanda[0])
    oferta[0] = oferta[0] - matriz_asigna[0][0]
    demanda[0] = demanda[0] - matriz_asigna[0][0]

    while i <= filas and j <= columnas:
        if oferta[i] == 0:
            i = i+1
            matriz_asigna[i][j] = np.minimum(oferta[i], demanda[j])
            oferta[i] = oferta[i] - matriz_asigna[i][j]
            demanda[j] = demanda[j] - matriz_asigna[i][j]

        elif demanda[j] == 0:
            j = j+1
            matriz_asigna[i][j] = np.minimum(oferta[i], demanda[j])
            oferta[i] = oferta[i] - matriz_asigna[i][j]
            demanda[j] = demanda[j] - matriz_asigna[i][j]

    print("Asignada:\n", matriz_asigna)
    print("Demanda:\n", demanda)
    print("Oferta:\n" ,oferta)
    #Contando número de asignasiones n+m-1
    asignasiones = (filas+columnas-1)
    print("Numero de asignasiones:" ,asignasiones)



oferta = np.array([250, 250, 100])
demanda = np.array([100, 200, 150, 100])

costos = np.array([[50, 78, 85, 20.],
                   [40, 35, 100, 90],
                   [55, 25, 60, 80]])

EsqNor(oferta, demanda, costos)
