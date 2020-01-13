import random
from brain_games.constants import MINIMAL_RANDOM
from brain_games.constants import MAXIMAL_RANDOM


def greeting():
    return 'What number is missing in the progression?'


def main_action():
    # длина ряда, не стал выносить в файл с константами
    # тк данная переменная используется только в этой функции
    progression_length = 10
    # номер скрытой позиции
    hidden_item_number = random.randint(1, progression_length)
    # величина итерации данного ряда
    row_iteration_size = random.randint(1, progression_length)
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    prog = [str(first_el), ]
    correct_ans = 0
    for ii in range(1, progression_length + 1):
        if ii == hidden_item_number:
            prog.append('..')
            correct_ans = first_el + row_iteration_size * ii
        else:
            prog.append(str(first_el + row_iteration_size * ii))

    str_to_question = ' '.join(prog)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
