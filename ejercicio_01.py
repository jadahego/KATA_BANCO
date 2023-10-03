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


def main(numeros):

    if not isinstance(n, int) or not (1 <= n <= 9):
        raise ValueError("n debe ser un número entero en el rango de 1 a 9")

    numeros_final = []

    for k in numeros:
        k_str = str(k)
        numeros_c= ''.join([i for i in k_str if int(i) < n])
        if numeros_c:
            numeros_final.append(int(numeros_c))

    for i in range(len(numeros)):
        for j in range(0, n-i-1):
            if numeros_final[j] < numeros_final[j+1]:
                numeros_final[j], numeros_final[j+1] = numeros_final[j+1], numeros_final[j]


    return numeros_final
  
print(main(numeros))



