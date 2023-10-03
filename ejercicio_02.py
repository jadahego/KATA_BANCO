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

def main(numbers):

    if not isinstance(n, int) or not (1 <= n <= 9):
        raise ValueError("n debe ser un número entero en el rango de 1 a 9")

    numbers_v2 = [i*i for i in numbers if i*i <= (n*11)]
  
    for i in range(len(numbers)):
            for j in range(0, n-i-1):
                if numbers_v2[j] > numbers_v2[j+1]:
                    numbers_v2[j], numbers_v2[j+1] = numbers_v2[j+1], numbers_v2[j]
    
    return numbers_v2

print(main(numbers))