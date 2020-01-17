import random
from brain_games.constants import MINIMAL_RANDOM, MAXIMAL_RANDOM, PROGRESSION_LENGTH


def greeting():
    return 'What number is missing in the progression?'


def main_action():
    # номер скрытой позиции
    hidden_item_number = random.randint(1, PROGRESSION_LENGTH)
    # величина итерации данного ряда
    row_iteration_size = random.randint(1, PROGRESSION_LENGTH)
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    prog = [str(first_el), ]
    correct_ans = 0
    for ii in range(1, PROGRESSION_LENGTH + 1):
        item_element = first_el + row_iteration_size * ii
        if ii == hidden_item_number:
            prog.append('..')
            correct_ans = item_element
        else:
            prog.append(str(item_element))

    str_to_question = ' '.join(prog)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
