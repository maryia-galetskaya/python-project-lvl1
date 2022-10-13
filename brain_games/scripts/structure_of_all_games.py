import random


def random_number():
    generate_start = 1
    generate_finish = 30
    return random.randint(generate_start, generate_finish)


def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')
    return name


def wrong_answer(ask_answer, right_answer, user_name):
    wrong_answer = (f"'{ask_answer}' is wrong answer ;(. Correct answer "
                    f"was '{right_answer}'.\nLet's try again, {user_name}!")
    print(wrong_answer)


def congrats(user_name):
    congratulations = (f'Congratulations, {user_name}!')
    print(congratulations)


def main():  
    random_number()
    user_name = welcome_user()
    congrats(user_name)


if __name__ == '__main__':
    main()
