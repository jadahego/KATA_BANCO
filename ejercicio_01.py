#ejercicio 1
#numeros=[8, 20, 3, 45, 66, 75, 65, 55, 86, 88, 80, 83, 80, 18 ]
lista_requerida = input("Ingrese una lista de números separados por comas: ")

lista_requerida_strings = lista_requerida.split(',')

try:
    numeros = [int(num) for num in lista_requerida_strings]
except ValueError:
    print("Error: Asegúrese de ingresar números válidos separados por comas.")
    exit()

S = input('Ingrese el valor de n: ')
n = int(S)

def ordenar(lista):
    h=len(lista)
    for i in range(h):
        for j in range(0, h-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


def main(numeros):

    if not isinstance(n, int) or not (1 <= n <= 9):
        raise ValueError("n debe ser un número entero en el rango de 1 a 9")

    numeros_final = []

    for k in numeros:
        k_str = str(k)
        numeros_c= ''.join([i for i in k_str if int(i) < n])
        if numeros_c:
            numeros_final.append(int(numeros_c))

    ordenar(numeros_final)

    return numeros_final
  
print(main(numeros))



