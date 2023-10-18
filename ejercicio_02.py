#numbers = [5, 4, 11, 6, 7, -2, 8, 9, -10, 0]
lista_requerida = input("Ingrese una lista de números separados por comas: ")

lista_requerida_strings = lista_requerida.split(',')

try:
    numbers = [int(num) for num in lista_requerida_strings]
except ValueError:
    print("Error: Asegúrese de ingresar números válidos separados por comas.")
    exit()

S = input('Ingrese el valor de n: ')
n = int(S)

def ordenar(lista):
    h=len(lista)
    for i in range(h):
        for j in range(0, h-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def main(numbers):

    if not isinstance(n, int) or not (1 <= n <= 9):
        raise ValueError("n debe ser un número entero en el rango de 1 a 9")

    numbers_v2 = [i*i for i in numbers if i*i <= (n*11)]
  
    ordenar(numbers_v2)
    
    return numbers_v2

print(main(numbers))