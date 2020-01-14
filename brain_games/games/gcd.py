import random
from brain_games.constants import MINIMAL_RANDOM
from brain_games.constants import MAXIMAL_RANDOM


def greeting():
    return 'Find the greatest common divisor of given numbers.'


def main_action():
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    second_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    min_el = first_el if first_el < second_el else second_el
    max_el = first_el if first_el > second_el else second_el
    correct_ans = euclidean_algorithm(max_el, min_el)

    str_to_question = '{} {}'.format(first_el, second_el)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans


def euclidean_algorithm(a, b):
    # остаток от деления
    remainder_of_division = a % b
    if remainder_of_division == 0:
        return b
    return euclidean_algorithm(b, remainder_of_division)
