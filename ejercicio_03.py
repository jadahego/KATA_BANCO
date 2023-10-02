nominaciones = [5,7,1,1,2,3,22]

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

print(minimadecambio(nominaciones))

