#nominaciones = [1,1,1,1,1]

lista_requerida = input("Ingrese una lista de números separados por comas: ")

lista_requerida_strings = lista_requerida.split(',')

try:
    nominaciones = [int(num) for num in lista_requerida_strings]
except ValueError:
    print("Error: Asegúrese de ingresar números válidos separados por comas.")
    exit()


for i in range(len(nominaciones)):
        for j in range(0, (len(nominaciones))-i-1):
            if nominaciones[j] > nominaciones[j+1]:
                nominaciones[j], nominaciones[j+1] = nominaciones[j+1], nominaciones[j]


def minimadecambio(nominaciones):

    monedas = 0

    for i in nominaciones: 
        if (i > monedas + 1):
            return monedas +1
        monedas += i

    return monedas + 1

print('')
print('La minima de cambio que no se puede dar es:', minimadecambio(nominaciones))

