from math import sqrt
import sys


def get_coefficients(string):
    try:
        a, b, c = string.split()

        if a == '0':
        	print('Введите коэффициенты "a", "b" и "c" квадратного уравнения, где "а" ≠ 0 (три числа через пробел): ')
        	return get_coefficients(input())

        return [float(a), float(b), float(c)]
    except ValueError:
        print('Введите коэффициенты "a", "b" и "c" квадратного уравнения, где "а" ≠ 0 (три числа через пробел): ')
        return get_coefficients(input())


def get_coefficients_from_argv(argv_list):
	try:
		return str(argv_list[1]) +   ' ' +str(argv_list[2]) + ' ' + str(argv_list[3])
	except IndexError:
		return None


def get_roots(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant < 0:
    	return None, None

    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2


def start_script(argv_list):
    if len(argv_list) < 2:
        print('\nВас привествует программа вычисления корней квадратичного уравнения\n'
              'Для того чтоб узнать как работает программа введите: python quadratic_equation.py --help или python3 quadratic_equation.py --help\n')
        return None

    if argv_list[1] == '--help':
        print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <коэффициент a> <коэффициент b> <коэффициент c>\n'
              'Наример: python3 quadratic_equation.py 1 2 -3\n')
        return None

    coefficients = get_coefficients( get_coefficients_from_argv(argv_list) )
    a, b, c = coefficients[0], coefficients[1], coefficients[2]
    solution = get_roots(a, b, c)

    if solution.count(None) == 2:
    	print('Уравнение не имеет решений на множестве действительных чисел')
    elif solution.count(None) ==1:
    	print('Квадратное уравнение имеет один действительный корень: ', solution[0])
    elif solution.count(None) == 0:
    	print('Уравнение имеет два решения: ', solution[0], solution[1])


if __name__ == '__main__':
	argv_list = sys.argv
	start_script(argv_list)