# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B
# три попытки tries = 3, while tries: ...
from ast import arguments
import random
from turtle import right

ans_yes = 'yes'
ans_no = 'no'

def number():
    generate_start = 1
    generate_finish = 99
    return random.randint(generate_start, generate_finish)

print('Welcome to the Brain Games!')
name = input ('May I have your name? ')

def welcome_user ():
    return (f'Hello, {name}!')
    
def even (num):
    if num % 2 == 0:
        correct_answer = ans_yes
        return correct_answer
    else: 
        correct_answer = ans_no
        return correct_answer

def brain_even ():
    # number = random.randint(1, 99)
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    tries=3 
    while tries:
        this_number = number()
        ask_answer = input (f'Question:{this_number}\nYour answer: ')
        if even(this_number) == ask_answer: #or odd() == ask_answer:
            print ('Correct!')
            tries-=1
        else: 
            return (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{(even(this_number))}'.\nLet's try again, {name}!")
    else:
        return (f'Congratulations, {name}!')


print (welcome_user())
print (brain_even())

#def main():
#    number()
#    welcome_user()
#    even (num)
#    brain_even ()

#if __name__ == '__main__':
#    main()


