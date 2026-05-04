import numpy as np
import matplotlib.pyplot as plt
import Py_07_Modulo_Constantes as mc

def calcular_y_graficar(t_med, h_med, liquido):
    # Altura normalizada
    y_exp = h_med / mc.H0
    
    # Mediciones con error relativo < 10%
    y_ref = (1 - t_med / mc.TF_TEORICO)**2
    error_rel = np.abs((y_exp - y_ref) / np.where(y_ref == 0, 1e-10, y_ref))
    
    filtro_error = error_rel < 0.10
    t_mejor, y_mejor = t_med[filtro_error], y_exp[filtro_error]
    
    # Puntos mínimos para el ajuste
    if len(t_mejor) < 4:
        t_mejor, y_mejor = t_med[:10], y_exp[:10]

    # Ajustes
    # Cuadrático (línea azul)
    c_cuad = np.polyfit(t_mejor, y_mejor, 2)
    print(f"Coeficientes Cuadrático: {c_cuad}")
    # Cúbico (línea violeta punteada)
    c_cubi = np.polyfit(t_mejor, y_mejor, 3)
    print(f"Coeficientes Cúbico: {c_cubi}")
    # Exponencial (línea verde de guiones)
    m_exp = y_mejor > 0
    c_expo = np.polyfit(t_mejor[m_exp], np.log(y_mejor[m_exp]), 1)
    print(f"Coeficientes Exponencial: {c_expo}")

    # Error cuadrático medio
    def ecm(y_r, y_p): return np.mean((y_r - y_p)**2)
    
    print(f"--- {liquido} (Error Exp: {mc.E_H_EXPERIMENTAL} cm) ---")
    print(f"ECM Cuadrático: {ecm(y_exp, np.polyval(c_cuad, t_med)):.6f}")
    print(f"ECM Cúbico:     {ecm(y_exp, np.polyval(c_cubi, t_med)):.6f}")
    print(f"ECM Exponencial: {ecm(y_exp, np.exp(np.polyval(c_expo, t_med))):.6f}\n")

    # Gráficos
    t_linea = np.linspace(0, t_med.max(), 100)
    plt.figure(figsize=(10, 5))
    
    plt.plot(t_med, y_exp, 'rx', markersize=4, label=f'Datos {liquido}')
    plt.plot(t_linea, np.polyval(c_cuad, t_linea), 'b-', label='Ajuste Cuadrático')
    plt.plot(t_linea, np.polyval(c_cubi, t_linea), color='darkviolet', linestyle=':', label='Ajuste Cúbico')
    plt.plot(t_linea, np.exp(np.polyval(c_expo, t_linea)), 'g--', label='Ajuste Exponencial')

    plt.xlabel('Segundos (s)')
    plt.ylabel('h(t)/h0')
    plt.title(f'Ajuste por Cuadrados Mínimos - {liquido}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def cm_main():
    # Jugo
    calcular_y_graficar(mc.T_JUGO, mc.H_JUGO, "Jugo")
    
    # Aceite
    calcular_y_graficar(mc.T_ACEITE, mc.H_ACEITE, "Aceite")