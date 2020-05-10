import  numpy as np

# Primero balanceamos nuestro problema, verificando que la suma de las
# demandaas sea igual a al suma de las ofertas

def get_balanceado_tp(oferta, demanda, costos):
    
    if sum(oferta) != sum(demanda):
        print("Problema no balanceado")
        if sum(oferta) > sum(demanda):
            demanda.append(sum(oferta)-sum(demanda))
            # Se agrega  la variable artificial como columna
            for i in range(len(costos)):
                costos[i].append(0)
            print("Se balanceara\n")
        else:
            oferta.append(sum(demanda)-sum(oferta))
            # Se agrega la variable artificial como fila
            costos.append([0]*len(costos[0]))
            print("Se balanceara\n")
    #else:
        #print("Problema balanceado\n")
    return(oferta,demanda,costos)



def esquina_noroeste(oferta, demanda):
    oferta_copy = oferta.copy()
    demanda_copy = demanda.copy()
    i = 0
    j = 0
    bfs = []
    # Asignasiones n+m-1 
    while len(bfs) < len(oferta) + len(demanda) - 1:
        s = oferta_copy[i]
        d = demanda_copy[j]
        v = min(s, d)
        oferta_copy[i] -= v
        demanda_copy[j] -= v
        bfs.append(((i, j), v))
        if oferta_copy[i] == 0 and i < len(oferta) - 1:
            i += 1
        elif demanda_copy[j] == 0 and j < len(demanda) - 1:
            j += 1
    return(bfs)

def Z_totales(bfs,costos):
    Z_total = 0
    for i in range(len(bfs)):
        Z_total += (costos[bfs[i][0][0]][bfs[i][0][1]])*(bfs[i][1])
    return(Z_total)


## Calculamos los vectores u y v 
## sabemos que u[i] + v[j] = c[i][j]
def get_us_y_vs(bfs, costos):
    us = [None] * len(costos)
    vs = [None] * len(costos[0])
    # Al primer elemento u[0] = 0
    us[0] = 0
    bfs_copy = bfs.copy()
    while len(bfs_copy) > 0:
        for index, bv in enumerate(bfs_copy):
            i, j = bv[0]
            if us[i] is None and vs[j] is None: continue
                
            cost = costos[i][j]
            if us[i] is None:
                us[i] = cost - vs[j]
            else: 
                vs[j] = cost - us[i]
            bfs_copy.pop(index)
            break
            
    return(us, vs)

def get_ws(bfs, costos, us, vs):
    ws = []
    for i, fila in enumerate(costos):
        for j, cost in enumerate(fila):
            no_basica = all([p[0] != i or p[1] != j for p, v in bfs])
            if no_basica:
                ws.append(((i, j), us[i] + vs[j] - cost))
    
    return(ws)


def puede_mejorar(ws):
    for p, v in ws:
        if v > 0:return True
    return False


def get_posicion_variable_entrante(ws):
    ws_copy = ws.copy()
    ws_copy.sort(key=lambda w: w[1])
    return(ws_copy[-1][0])


def get_possible_next_nodes(loop, sin_visitar):
    ultimo_nodo = loop[-1]
    nodos_en_fila = [n for n in sin_visitar if n[0] == ultimo_nodo[0]]
    nodos_en_columna = [n for n in sin_visitar if n[1] == ultimo_nodo[1]]
    if len(loop) < 2:
        return(nodos_en_fila + nodos_en_columna)
    else:
        prev_node = loop[-2]
        fila_move = prev_node[0] == ultimo_nodo[0]
        if fila_move: return nodos_en_columna
        return(nodos_en_fila)




def get_loop(bv_positions, ev_position):
    def inner(loop):
        if len(loop) > 3:
            pueden_estar_cerca = len(get_possible_next_nodes(loop, [ev_position])) == 1
            if pueden_estar_cerca: return loop
        
        sin_visitar = list(set(bv_positions) - set(loop))
        possible_next_nodes = get_possible_next_nodes(loop, sin_visitar)
        for next_node in possible_next_nodes:
            new_loop = inner(loop + [next_node])
            if new_loop: return new_loop
    
    return inner([ev_position])


def loop_pivoting(bfs, loop):
    even_cells = loop[0::2]
    odd_cells = loop[1::2]
    get_bv = lambda pos: next(v for p, v in bfs if p == pos)
    leaving_position = sorted(odd_cells, key=get_bv)[0]
    leaving_value = get_bv(leaving_position)
    
    new_bfs = []
    for p, v in [bv for bv in bfs if bv[0] != leaving_position] + [(loop[0], 0)]:
        if p in even_cells:
            v += leaving_value
        elif p in odd_cells:
            v -= leaving_value
        new_bfs.append((p, v))
        
    return new_bfs




def metodo_transporte(oferta, demanda, costos, penalties = None):
    balanceado_oferta, balanceado_demanda, balanceado_costos = get_balanceado_tp(oferta, demanda, costos)
    print("Balance:\n")
    print("Oferta:",balanceado_oferta)
    print("demandaa:",balanceado_demanda)
    print("Costos:",balanceado_costos,'\n')
    def inner(bfs):
        #soluciones = esquina_noroeste(balanceado_oferta, balanceado_demanda)
        print("Variables basicas:",bfs)
        us, vs = get_us_y_vs(bfs, balanceado_costos)
        Z = Z_totales(bfs,balanceado_costos)
        print('Z:',Z)
        print("u[i]:",us)
        print("v[j]:",vs)
        ws = get_ws(bfs, balanceado_costos, us, vs)
        print("ws[i][j]:",ws)
        mejora = puede_mejorar(ws)
        print("¿Puede mejorar?",mejora,'\n')
        if puede_mejorar(ws):
            ev_position = get_posicion_variable_entrante(ws)
            loop = get_loop([p for p, v in bfs], ev_position)
            return inner(loop_pivoting(bfs, loop))
        return bfs
    
    variables_basicas = inner(esquina_noroeste(balanceado_oferta, balanceado_demanda))
    print("Variables basicas:",variables_basicas)
    solucion = np.zeros((len(costos), len(costos[0])))
    for (i, j), v in variables_basicas:
        solucion[i][j] = v
    return(solucion)




def get_costo_total(costos, solucion):
    costo_total = 0
    for i, fila in enumerate(costos):
        for j, cost in enumerate(fila):
            costo_total += cost * solucion[i][j]
    return(costo_total)




#costos = [[5,8,6,6,3],
#         [4,7,7,6,5],
#         [8,4,6,6,4]]
#oferta = [8,5,9]
#demanda = [4,4,5,4,8]
oferta = [float(x) for x in input('Introduce  las ofertas separadas por una coma: ').split(',')]
demanda = [float(y) for y in input('Introduce las demandas separadas por una coma: ').split(',')]

filas = int(input("Numero de filas:"))
columnas = int(input("Numero de columnas:"))
costos=[]
for i in range(1, filas+1):
     costos.append(list(map(lambda j: int(input('valor:')), [ j for j in range(columnas)] )))
solucion = metodo_transporte(oferta, demanda, costos)
print("Solucion:\n",solucion)
print('Z:', get_costo_total(costos, solucion))
