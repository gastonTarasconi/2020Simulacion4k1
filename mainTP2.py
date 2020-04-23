from tp2.exports.ToExcel import ToExcel
from tp2.TestChiCuadrado import TestChiCuadradoTp2


ACCURACY = 4
# tests
# filename = 'PruebaUniforme.txt'
# filename = 'PruebaNormal.txt'
# filename = 'PruebaExponencial.txt'
# filename = 'PruebaPoisson.txt'

filename = 'data.txt'
xls_name = 'test_chi2_' + filename

with open(filename, 'r') as f:
    random_numbers = f.readline().split(';')
    _type = int(f.readline())
    intervals = int(f.readline())
    lim_inf = float(min(random_numbers))
    lim_sup = float(max(random_numbers))

t = TestChiCuadradoTp2(random_numbers, ACCURACY)
t.do_test(lim_inf, lim_sup, _type, intervals)

ToExcel.create_excel(t, xls_name)
