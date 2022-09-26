import random

ans_yes = 'yes'
ans_no = 'no'

def random_number():
    generate_start = 1
    generate_finish = 30
    return random.randint(generate_start, generate_finish)

#print('Welcome to the Brain Games!')
#name = input ('May I have your name? ')

def welcome_user ():
    print('Welcome to the Brain Games!')
    name = input ('May I have your name?')
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print (f'Hello, {name}!')
    return name

    
def even (num):
    if num % 2 == 0:
        correct_answer = ans_yes
        return correct_answer
    else: 
        correct_answer = ans_no
        return correct_answer

def check_answer (ask_answer, right_answer, user_name):
    if ask_answer == str (right_answer):
        print ('Correct!')
    else:
        print (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {user_name}!")
    

def wrong_answer (ask_answer, right_answer, user_name):
    wrong_answer = (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {user_name}!")
    print (wrong_answer)
    #return wrong_answer

def congrats (user_name):
    congr = (f'Congratulations, {user_name}!')
    return congr

#def wrong_asnwer (user_name):
#    return  (f"'{ask_answer}' is wrong answer ;(. Correct answer was '{(even(this_number))}'.\nLet's try again, {user_name}!")





#print (welcome_user())
#print (brain_even())

def main():  
    random_number ()
    user_name = welcome_user()
    #brain_even(user_name)

if __name__ == '__main__':
    main()