import random
from brain_games.constants import MINIMAL_RANDOM, MAXIMAL_RANDOM


def greeting():
    return 'Find the greatest common divisor of given numbers.'


def main_action():
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    second_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    correct_ans = gcd(first_el, second_el)

    str_to_question = '{} {}'.format(first_el, second_el)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans


def gcd(a, b):
    # остаток от деления
    remainder_of_division = a % b
    if remainder_of_division == 0:
        return b
    return gcd(b, remainder_of_division)
