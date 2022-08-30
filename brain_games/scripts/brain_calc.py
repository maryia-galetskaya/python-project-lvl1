#from brain_games.scripts.brain_even import number
from brain_games.scripts.structure_of_all_games import welcome_user, number
#import structure_of_all_games
import random

def random_calc():
    plus_minus_mult= ('+', '-')
    rand_calc_str = (random.choice(plus_minus_mult))
    return rand_calc_str

def right_ans (number1, number2, sign):
    if sign == '+':
        right_answer = str (number1 + number2)
        return right_answer
    elif sign == '-':
        right_answer = str (number1 - number2)
        return right_answer
    else: #sign == '*':
        right_answer = str (number1 * number2)
        return right_answer

def brain_calc (user_name):
    #welcome_user()
    print ('What is the result of the expression?')
    tries=3 
    while tries:
        number1 = number()
        number2 = number() 
        sign = random_calc()
        
        ask_answer = input (f'Question:{number1} {sign} {number2}\nYour answer: ')
        right_answer = right_ans (number1, number2, sign)
        if ask_answer == right_answer:
            print ('Correct!')
            #tries-=1
        else:
            wrong_answer = (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {user_name}!")
            print (wrong_answer)
            return wrong_answer
        tries-=1
    else:
        print (f'Congratulations, {user_name}!')

    
    

def main():  
    user_name = welcome_user()
    brain_calc(user_name)

if __name__ == '__main__':
    main()
