from brain_games.scripts.structure_of_all_games import welcome_user, wrong_answer, congrats, random_number
import random

def random_calc():
    plus_minus_mult = ('+', '-', '*')
    rand_calc_str =(random.choice(plus_minus_mult))
    return rand_calc_str

def right_ans(number1, number2, sign):
    if sign == '+':
        right_answer = str(number1 + number2)
        return right_answer
    elif sign == '-':
        right_answer = str(number1 - number2)
        return right_answer
    else: #sign == '*'
        right_answer = str(number1 * number2)
        return right_answer

def brain_calc(user_name):
    print('What is the result of the expression?')
    tries = 3 
    while tries:
        number1 = random_number()
        number2 = random_number() 
        sign = random_calc()
        ask_answer = input(f'Question: {number1} {sign} {number2}\nYour answer: ')
        right_answer = right_ans (number1, number2, sign)

        if ask_answer == right_answer:
            print('Correct!')
            tries-=1
        else:
            wrong_answer(ask_answer, right_answer, user_name)
    else:
        congrats(user_name)


def main():
    user_name = welcome_user()
    brain_calc(user_name)

if __name__ == '__main__':
    main()
