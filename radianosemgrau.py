import math

def radianos_em_grau(radiano):
    pi = math.pi
    radiano_convertido = radiano * 180 / pi
    return radiano_convertido

resultado = radianos_em_grau(89)
print(resultado)