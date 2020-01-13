import random
from brain_games.constants import MINIMAL_RANDOM
from brain_games.constants import MAXIMAL_RANDOM


def greeting():
    return 'Answer "yes" if number even otherwise answer "no".'


def main_action():
    cnt = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    correct_ans = 'no'
    if cnt % 2 == 0:
        correct_ans = 'yes'

    str_to_question = str(cnt)

    return str_to_question, correct_ans
