#from brain_games.scripts.brain_even import number
from structure_of_all_games import welcome_user, number, congrats
import random

def random_calc():
    plus_minus_mult= ('+', '-', '*')
    rand_calc_str = (random.choice(plus_minus_mult))
    return rand_calc_str


#def calc (num1, num2):
    if random_calc() == '+':
        return num1 + num2
    if random_calc() == '-':
        return num1 - num2 
    if random_calc() == '*':
        return num1 * num2

def brain_calc (user_name):
    #welcome_user()
    print ('What is the result of the expression?')
    tries=3 
    while tries:
        number1 = number()
        number2 = number() #and <number1
        #result_sum = number1 + number2
        #result_minus = number1 - number2
        #result_mult = number1 * number2
        sign = random_calc()
        if sign == '+':
            ask_answer = input (f'Question:{number1} + {number2}\nYour answer: ')
            result_sum = number1 + number2
            if ask_answer == str (result_sum):
                print ('Correct!')

            else:
                print (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{result_sum}'.\nLet's try again, {user_name}!")

            #return ask_answer
        if random_calc() == '-':
            ask_answer = input (f'Question:{number1} - {number2}\nYour answer: ')
            result_minus = number1 - number2
            if ask_answer == str (result_minus):
                print ('Correct!')
               
            else: 
                print (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{result_minus}'.\nLet's try again, {user_name}!")
                
            #return ask_answer
        if random_calc() == '*':
            ask_answer = input (f'Question:{number1} * {number2}\nYour answer: ')
            result_mult = number1 * number2
            if ask_answer == str (result_mult):
                print ('Correct!')
                
            else: 
                print (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{result_mult}'.\nLet's try again, {user_name}!")
                
            #return ask_answer
        tries-=1
    else:
        print (f'Congratulations, {user_name}!')

    
    

def main():  
    user_name = welcome_user()
    brain_calc(user_name)

if __name__ == '__main__':
    main()
