import Py_07_Modulo_Constantes as mc

def obtener_altura(t): # Ecuación (1)
    altura = mc.H0 * ((1 - t / mc.TF_TEORICO) ** 2)
    return altura

def obtener_error_altura(t): # Ecuación (3) con error absoluto despejado
    error = ((mc.E_H0 / mc.H0) + 2 * ((t * mc.E_TF_TEORICO) / mc.TF_TEORICO ** 2)) * obtener_altura(t)
    return error