from brain_games.scripts.structure_of_all_games import welcome_user, wrong_answer, congrats, random_number


def isPrime(number):
    if number == 1:
        return 'yes'
    if number <1:
        return 'Number is negative'
    i = 2
    while i < number:
        if number % i == 0:
            return 'no'
        i += 1
    else:
        return 'yes'


def brain_prime(user_name):
    print ('Answer "yes" if given number is prime. Otherwise answer "no".')
    tries = 3
    while tries:
        asked_number = random_number()
        right_answer = isPrime(asked_number)
        ask_answer = input(f'Question: {asked_number}\nYour answer: ')
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
    brain_prime(user_name)

if __name__ == '__main__':
    main()
