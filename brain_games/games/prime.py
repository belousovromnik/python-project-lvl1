import random
import math
from brain_games.constants import MINIMAL_RANDOM, MAXIMAL_RANDOM


def greeting():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main_action():
    cnt = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    str_to_question = str(cnt)

    correct_ans = 'no'
    if is_prime(cnt) is True:
        correct_ans = 'yes'

    return str_to_question, correct_ans


def is_prime(number):
    if number in {1, 2}:
        return True
    if number % 2 == 0:
        return False
    sqrt_number = math.floor(math.sqrt(number))
    for i in range(3, sqrt_number + 1, 2):
        if number % i == 0:
            return False
    return True
