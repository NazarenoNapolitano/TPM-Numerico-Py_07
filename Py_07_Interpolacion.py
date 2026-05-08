import numpy as np
import Py_07_Ecuaciones_Errores as ee
import Py_07_Modulo_Constantes as mc

def obtener_error_tiempo_interpolacion(t1,t2,h1,h2,objetivo):
    error_t_i = (abs(t2-t1)/(abs(h2-h1)**2))*((abs(h2-objetivo))*(ee.obtener_error_altura(t1))+(abs(h1-objetivo))*(ee.obtener_error_altura(t2)))
    return error_t_i

def interpolar_tiempo(tiempos, alturas, h0, objetivo):
    """
    objetivo: fracción restante (ej: 0.5)
    """
    h_normalizada = np.array(alturas) / h0
    tiempos = np.array(tiempos)

    for i in range(len(h_normalizada) - 1):
        if h_normalizada[i] >= objetivo and h_normalizada[i+1] <= objetivo:
            # interpolación lineal
            t1, t2 = tiempos[i], tiempos[i+1]
            h1, h2 = h_normalizada[i], h_normalizada[i+1]

            t = t1 + (objetivo - h1) * (t2 - t1) / (h2 - h1)
            error_t = obtener_error_tiempo_interpolacion(t1,t2,h1,h2,objetivo)
            return [t,error_t]

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
    errores = {}

    for nombre, obj in objetivos.items():
        tiempo_y_error = interpolar_tiempo(tiempos, alturas, h0, obj)
        resultados[nombre] = tiempo_y_error[0]
        errores[nombre] = tiempo_y_error[1]

    return [resultados, errores]

def tiempo_vaciado(tf, porcentaje_vaciado):
    fraccion_restante = 1 - porcentaje_vaciado
    modificador_tf = (1 - np.sqrt(fraccion_restante))
    return [tf * modificador_tf, mc.E_TF_TEORICO * modificador_tf] # El segundo término es el error del tiempo teórico.


def tiempos_teoricos(tf):
    porcentajes = {
        "10%": 0.10,
        "25%": 0.25,
        "50%": 0.50,
        "75%": 0.75,
        "90%": 0.90
    }

    resultados = {}
    errores = {}

    for nombre, p in porcentajes.items():
        resultados[nombre] = tiempo_vaciado(tf, p)[0]
        errores[nombre] = tiempo_vaciado(tf,p)[1]
    return [resultados,errores]


def inp_main():
    print("=== INTERPOLACIÓN ===")

    print("\nJUGO:")
    exp = tiempos_experimentales(mc.T_JUGO, mc.H_JUGO, mc.H0)
    teo = tiempos_teoricos(mc.TF_TEORICO)

    resultados_exp = exp[0]
    errores_exp = exp[1]
    resultados_teo = teo[0]
    errores_teo = teo[1]

    for k,j,l,m in zip(resultados_exp,errores_exp,resultados_teo,errores_teo):
        print(f"{k} -> experimental: {resultados_exp[k]:.2f} s, error: {errores_exp[j]:.2f} | teórico: {resultados_teo[l]:.2f} s, error: {errores_teo[m]:.2f}")

    print("\nACEITE:")
    exp = tiempos_experimentales(mc.T_ACEITE, mc.H_ACEITE, mc.H0)
    teo = tiempos_teoricos(mc.TF_TEORICO)

    resultados_exp = exp[0]
    errores_exp = exp[1]
    resultados_teo = teo[0]
    errores_teo = teo[1]

    for k,j,l,m in zip(resultados_exp,errores_exp,resultados_teo,errores_teo):
        print(f"{k} -> experimental: {resultados_exp[k]:.2f} s, error: {errores_exp[j]:.2f} | teórico: {resultados_teo[l]:.2f} s, error: {errores_teo[m]:.2f}")