import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM
from brain_games.const import ANSWER_STRING


def prime():
    cnt = random.randint(BEGIN_RANDOM, END_RANDOM)
    correct_ans = 'yes'
    for ii in range(2, cnt):
        if cnt % ii == 0:
            correct_ans = 'no'
            break
    ANSWER_STRING['games']['question'] = str(cnt)
    ANSWER_STRING['games']['answer_correct'] = correct_ans
