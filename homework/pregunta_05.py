"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_05():
       # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Agrupar por c1 y calcular el valor máximo de c2 para cada grupo
    resultado = tbl0.groupby('c1')['c2'].max()

    # Imprimir el resultado
    return resultado

