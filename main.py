from goodness_of_fit.chi_square.ChiSquareTest import ChiSquareTest
from utils.export.Excel import Excel


ACCURACY = 4
# # tests
# files = ['PruebaUniforme.txt',
#          'PruebaNormal.txt'
#          'PruebaExponencial.txt'
#          'PruebaPoisson.txt'
#          ]
# files_folder = 'test_files/'


url_main_folder = './'
url_tests_files_folder = f'{url_main_folder}test_files/'
url_export_files_folder = f'{url_main_folder}exports_files/'
filename = f'{url_tests_files_folder}dataU.txt'
# filename = f'{url_tests_files_folder}dataN.txt'
# filename = f'{url_tests_files_folder}dataE.txt'
# filename = f'{url_tests_files_folder}dataP.txt'
xls_name = f'{url_export_files_folder}test_chi2_asd'

with open(filename, 'r') as f:
    line = f.readline().split(';')
    random_numbers = [float(i) for i in line]
    _type = int(f.readline())
    intervals = int(f.readline())

test = ChiSquareTest(random_numbers, ACCURACY)
if _type == 3:
    test.do_test_poisson()
else:
    test.do_test(intervals, _type)

xls = Excel(xls_name)
xls.do_chi_square(_type, test.labels, test.observed_frequency, test.expected_frequency, test.chi_2, test.chi_2_ac)

