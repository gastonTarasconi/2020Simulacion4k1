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
    method = MethodCongrualesMixto(root_number, ACCURACY)
elif method_choice == 1:
    method = MethodCongrualesMultiplicativo(root_number, ACCURACY)


for x in range(STARTING_QUANTITY):
    random_numbers.append(method.get_random())

print(random_numbers)


go = input('¿Generar otro? (y/n)')
while go != 'n':
    random_numbers.append(method.get_random())

    print(random_numbers)
    go = input('¿Siguiente? (y/n)')
