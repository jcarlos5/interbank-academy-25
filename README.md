# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## :clipboard: Introducción:

El propósito de este reto es generar un reporte que indique el balance final, la transacción de mayor monto y la cantidad de operaciones por tipo.

## :computer: Instrucciones de Ejecución:

El programa utiliza el lenguaje Python, específicamente fue construido con la versión 3.13, no se requiere la instalación de dependencias.

Para ejecutar el programa utilice el comando 
```bash
python main.py
```


## :mag: Enfoque y Solución:

El programa fue desarrollado con un enfoque en simplicidad y eficiencia, la lógica se presenta a continuación:
1. Se definen constantes útiles para la ejecución del programa. Esto permitirá actualizar rápidamente valores utilizados para la gestión del archivo `CSV`.
2. Se definen las variables que se utilizarán para almacenar los resultados que se incluirán en el reporte.
3. El programa inicia con la apertura del archivo `CSV` que contiene los datos de entrada, así mismo, se invoca a una función que validará los tipos de datos que se requieren para la elaboración del reporte.
4. Dependiendo del tipo de transacción se sumará o restará el monto al balance y se aumentará en una unidad la cantidad de transacciones según el tipo (Débito o Crédito).
5. Se realiza una comparación del monto de la fila que se está leyendo con la última transacción más alta que se almacenó.
6. Se imprimen los resultados.

## :hammer: Estructura del Proyecto:

El proyecto tiene una estructura simple en la cuál el programa y el archivo con los datos de entrada se encuentran en la raíz, a continuación se muestra el esquema de archivos que encontrará:

```
  /interbank-academy-25
   │── data.csv               # Archivo de datos
   │── main.py                # Programa
   │── README.md              # Presentación
```
