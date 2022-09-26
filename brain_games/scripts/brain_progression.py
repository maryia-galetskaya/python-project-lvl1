from structure_of_all_games import random_number, welcome_user, congrats, wrong_answer
import random


def brain_progression(user_name):
    print('What number is missing in the progression?')
    tries=3 
    while tries:
        length_of_pr = random.randint(7,11)
        difference_in_raw = random.randint(1,12)
        start_number = random_number()

        raw = []
        i = start_number
        while len(raw) != length_of_pr:
            raw.append(i)
            i +=difference_in_raw

        hidden_index = random.randint(0, len(raw)-1)
        right_answer = raw [hidden_index]
        raw[hidden_index] = '..'
        raw.insert(0, 'Question:')
        print(*raw)
        ask_answer = input('Your answer: ')

        if ask_answer == str(right_answer): 
            print ('Correct!')
        else:
            return wrong_answer(ask_answer, right_answer, user_name)
        tries-=1
    else:
        print(congrats(user_name))


def main():
    user_name = welcome_user()
    brain_progression(user_name)


if __name__ == '__main__':
    main()