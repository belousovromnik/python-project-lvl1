import random
from brain_games.constants import MINIMAL_RANDOM
from brain_games.constants import MAXIMAL_RANDOM


def greeting():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main_action():
    cnt = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    correct_ans = 'yes'
    for ii in range(2, cnt):
        if cnt % ii == 0:
            correct_ans = 'no'
            break

    str_to_question = str(cnt)

    return str_to_question, correct_ans
