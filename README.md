# Proyecto Calculadora con Validación y Pruebas Unitarias

Este proyecto implementa un conjunto de funciones básicas para realizar operaciones matemáticas como suma, resta, multiplicación y división. También incluye validaciones para manejar entradas incorrectas y pruebas unitarias automatizadas con GitHub Actions.

## Funciones implementadas
Las siguientes operaciones están disponibles:

- `sumar(a, b)`: Realiza la suma de dos números.
- `restar(a, b)`: Realiza la resta de dos números.
- `multiplicar(a, b)`: Realiza la multiplicación de dos números.
- `dividir(a, b)`: Realiza la división de dos números, manejando el caso de división entre cero.

## Validaciones
El programa valida que las entradas:
1. Sean números (`int` o `float`).
2. No sean valores nulos (`None`).
3. No sean tipos de datos no numéricos (listas, diccionarios, cadenas, etc.).

Si las entradas no cumplen estas condiciones, se lanza una excepción `TypeError`.

En el caso de la división, si el divisor es 0, se lanza una excepción `ValueError`.


