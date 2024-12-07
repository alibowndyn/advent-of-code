import re
import itertools as it



def is_equation_correct(equation: list[int]) -> bool | None:
    operator_combinations =  list(it.product('+*|', repeat=len(equation)-2))

    for op_combo in operator_combinations:
        res = equ[1]

        for (operator, operand) in zip(op_combo, equ[2:]):
            if operator == '*':
                res *= operand
            elif operator == '+':
                res += operand
            else:
                res = int(str(res) + str(operand))

        if res == equ[0]:
            return True


inp = open('../input.txt').read().splitlines()

equations = [list(map(int, re.findall(r'\d+', line))) for line in inp]
total_calibration_result = 0

for equ in equations:
    if is_equation_correct(equ):
        total_calibration_result += equ[0]


print(total_calibration_result)
