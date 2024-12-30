"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_06():
# Leer el archivo tbl1.tsv
    tbl1 = pd.read_csv('files/input/tbl1.tsv', sep='\t')

    # Obtener los valores únicos de la columna c4, 
    # convertir a mayúsculas y ordenar alfabéticamente
    resultado = sorted(tbl1['c4'].str.upper().unique())

    # Imprimir el resultado
    print(resultado)

pregunta_06()
