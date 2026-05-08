import Py_07_Cuadrados_Minimos as cm
import Py_07_Interpolacion as inp

while True:
    print("1. Estimación de distintos tiempos e Interpolación")
    print("2. Ajuste por cuadrados mínimos")
    print("3. Terminar programa")
    eleccion = input("Elegir opción (1-3): ")
    if eleccion == '1':
        inp.inp_main()
    elif eleccion == '2':
        cm.cm_main()
    elif eleccion == '3':
        break
    else:
        print("Reingresar valor")
