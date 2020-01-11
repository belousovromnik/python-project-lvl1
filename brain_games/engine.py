import prompt
from brain_games.const import COUNT_QUESTIONS


def run(games_obj):

    print('Welcome to the Brain Games!')
    print(games_obj.greeting())

    nam_user = prompt.string('May I have your name? ')
    print("Hello, {}!". format(nam_user))

    i = 1
    while i <= COUNT_QUESTIONS:

        str_to_question, correct_ans = games_obj.main_action()

        print('Question: {}'.format(str_to_question))
        answer = prompt.string('Your answer: ')

        if correct_ans == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer,
                correct_ans))
            print("Let's try again, {}!".format(nam_user))
            break
        i += 1
    else:
        print("Congratulations, {}!".format(nam_user))
