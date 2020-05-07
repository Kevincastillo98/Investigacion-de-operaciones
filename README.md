# Investigacion de operaciones
Este repositorio contiene la implementación de 3 algoritmos
usados en problemas de transporte, transborde y asignación de tareas.

Dentro de los algoritmos a implementar se encuentran:

## Transporte

El modelo de transporte es una clase especial de programación lineal que tiene que 
ver con transportar un artículo desde sus fuentes hasta sus destinos.
El objetivo es determinar el programa de transporte que minimice el costo total de transporte 
y que al mismo tiempo satisfaga los limites de la oferta. 

- **Algoritmo de esquina noroeste:** El método comienza en la celdade la esquina noroeste, o
 superior izquierda de la tabla variable <img src="https://render.githubusercontent.com/render/math?math=X_{11}">
- **Paso1:** Asignar todo lo más que se pueda a la celda seleccionada y ajustar las cantidades
  asociadas de oferta y demanda restando la cantidad asignada.
- **Paso 2:** Salir del renglón o la columna cuando se alcance oferta o deanda cero, y tacharlo,
  para indicar que no se puede hacer más asignaciones a ese renglón o columna.Si un renglón y una columna 
 dan cero al mismo tiempo, tachar solo uno y dejar una oferta cero en el renglón que no se tachó.
- **Paso 3:** Si quedan exactamente un renglón o columna sin tachar, detenerse.En caso contrario, 
 avanzar a la celda de la derecha si se acaba de tachar una columna, o a la de abajo si se tachó un renglón.
 `Seguir con el paso 1`.


## Transbordo

- **Algoritmo de costo mínimo**

## Programación entera 

- **Ramificación y acotamiento**
