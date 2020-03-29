from tp1.MethodCongruencialesMixto import MethodCongrualesMixto
from tp1.MethodCongruencialesMultiplicativo import MethodCongrualesMultiplicativo

# initialization
STARTING_QUANTITY = 20
ACCURACY = 4
random_numbers = []
method = None

# method choice
method_choice = int(input('''Métodos: 
    0.Congruenciales mixto
    1.Congruenciales multiplicativo
Seleccione método (0, 1):'''))


while method_choice not in range(2):
    method_choice = int(input('Seleccione una opción válida:'))

root_number = int(input('Ingrese número raíz: '))

if method_choice == 0:
    k = int(input('Ingrese k: '))
    g = int(input('Ingrese g: '))
    c = int(input('Ingrese c: '))
    method = MethodCongrualesMixto(root_number, k, g, c, ACCURACY)
elif method_choice == 1:
    k = int(input('Ingrese k: '))
    g = int(input('Ingrese g: '))
    method = MethodCongrualesMultiplicativo(root_number, k, g, ACCURACY)


for x in range(STARTING_QUANTITY):
    random_numbers.append(method.get_random())

print(random_numbers)


go = input('¿Generar otro? (y/n)')
while go != 'n':
    random_numbers.append(method.get_random())

    print(random_numbers)
    go = input('¿Siguiente? (y/n)')
