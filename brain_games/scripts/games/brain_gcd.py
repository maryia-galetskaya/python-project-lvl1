from brain_games.scripts.structure_of_all_games import welcome_user, wrong_answer, congrats, random_number


def to_know_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def brain_gcd(user_name):
    print('Find the greatest common divisor of given numbers.')
    tries = 3 
    while tries:
        number1, number2 = random_number(), random_number() 
        #number2 = random_number() 
        ask_answer = input(f'Question:{number1} {number2}\nYour answer: ')
        right_answer = to_know_gcd(number1, number2)
        if ask_answer == str(right_answer):
            print('Correct!')
            tries-=1
        else:
            wrong_answer(ask_answer, right_answer, user_name)
            break
    else:
        congrats(user_name)


def main():
    user_name = welcome_user()
    brain_gcd(user_name)


if __name__ == '__main__':
    main()
