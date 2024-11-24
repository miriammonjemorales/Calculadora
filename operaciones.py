def validar_entrada(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números")

def sumar(a, b):
    validar_entrada(a, b)
    return a + b

def restar(a, b):
    validar_entrada(a, b)
    return a - b

def multiplicar(a, b):
    validar_entrada(a, b)
    return a * b

def dividir(a, b):
    validar_entrada(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    print(sumar(5, 3))
    print(restar(5, 3))
    print(multiplicar(5, 3))
    print(dividir(5, 3))
