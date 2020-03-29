import random
import math
from utils.tools import truncate
from tp1.TestChiCuadrado import TestChiCuadrado

ACCURACY = 4
# quantity_numbers = int(input('Ingrese cantidad de números a generar:'))
# subintervals = int(input('Ingrese cantidad de subintervalos:'))
random_numbers = []

# for i in range(quantity_numbers):
#     random_numbers.append(truncate(random.random(), ACCURACY))

random_numbers = [0.15, 0.22, 0.41, 0.65, 0.84,
                  0.81, 0.62, 0.45, 0.32, 0.07,
                  0.11, 0.29, 0.58, 0.73, 0.93,
                  0.97, 0.79, 0.55, 0.35, 0.09,
                  0.99, 0.51, 0.35, 0.02, 0.19,
                  0.24, 0.98, 0.10, 0.31, 0.17]
subintervals = int(math.sqrt(len(random_numbers)))

t = TestChiCuadrado(random_numbers, subintervals, ACCURACY)
t.do_test()

print(t.labels)
print(t.freq_observ)
print(t.freq_esperadas)
print(t.chi_2)
print(truncate(sum(t.chi_2), ACCURACY))
