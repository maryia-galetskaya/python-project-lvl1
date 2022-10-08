import random
from structure_of_all_games import welcome_user, wrong_answer, congrats, random_number

ans_yes = 'yes'
ans_no = 'no'

#print('Welcome to the Brain Games!')
#name = input ('May I have your name? ')


def even(num):
    if num % 2 == 0:
        correct_answer = ans_yes
        return correct_answer
    else: 
        correct_answer = ans_no
        return correct_answer

def brain_even(user_name):
    # number = random.randint(1, 99)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries = 3 
    while tries:
        this_number = random_number()
        ask_answer = input(f'Question:{this_number}\nYour answer: ')
        if even(this_number) == ask_answer: #or odd() == ask_answer:
            print('Correct!')
            tries-=1
        else: 
            wrong_answer(ask_answer, even(this_number), user_name )
            break
    else:
        congrats(user_name)



def main():
    user_name = welcome_user()
    brain_even(user_name)

if __name__ == '__main__':
    main()


