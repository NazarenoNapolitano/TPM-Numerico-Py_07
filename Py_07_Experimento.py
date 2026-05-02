import numpy as np

def interpolar_tiempo(tiempos, alturas, h0, objetivo):
    """
    objetivo: fracción restante (ej: 0.5)
    """
    h_norm = np.array(alturas) / h0
    tiempos = np.array(tiempos)

    for i in range(len(h_norm) - 1):
        if h_norm[i] >= objetivo and h_norm[i+1] <= objetivo:
            # interpolación lineal
            t1, t2 = tiempos[i], tiempos[i+1]
            h1, h2 = h_norm[i], h_norm[i+1]

            t = t1 + (objetivo - h1) * (t2 - t1) / (h2 - h1)
            return t

    return None

def tiempos_experimentales(tiempos, alturas, h0):
    objetivos = {
        "10%": 0.9,
        "25%": 0.75,
        "50%": 0.5,
        "75%": 0.25,
        "90%": 0.1
    }

    resultados = {}

    for nombre, obj in objetivos.items():
        t = interpolar_tiempo(tiempos, alturas, h0, obj)
        resultados[nombre] = t

    return resultados
