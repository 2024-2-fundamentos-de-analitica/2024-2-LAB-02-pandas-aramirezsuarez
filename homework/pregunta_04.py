"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_04():
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    mean_c2_by_c1 = tbl0.groupby('c1')['c2'].mean()
    return mean_c2_by_c1

print(pregunta_04())