from structure_of_all_games import random_number, welcome_user, congrats, wrong_answer
import random


def length_of_pr ():
    min_len_of_row = 7
    max_len_of_row = 11
    return random.randint(min_len_of_row, max_len_of_row)


def difference_in_row_():
    min_diff_in_row = 1
    max_diff_in_row = 12
    return random.randint(min_diff_in_row, max_diff_in_row)


def start_of_row():
    return random_number()

#def hide_index(row):
#    first_rows_index = 0
#    last_rows_index = len(row) - 1
#    return random.randint(first_rows_index, last_rows_index)


def brain_progression(user_name):
    print ('What number is missing in the progression?')
    tries=3 
    while tries:
        len_of_pr = length_of_pr()
        difference_in_row = difference_in_row_()
        start_number = start_of_row()

        row = []
        while len(row) != len_of_pr:
            row.append(start_number)
            start_number += difference_in_row
        hidden_index = random.randint(0, len(row)-1)
        right_answer = row [hidden_index]
        row[hidden_index] = '..'
        row.insert(0, 'Question:')

        print (*row)
        ask_answer = input('Your answer: ')  # 8) ask answer
        if ask_answer == str (right_answer): # 9) got answer and compare to right one
            print ('Correct!')
        else:
            return wrong_answer (ask_answer, right_answer, user_name)
        tries-=1
    else:
        return (congrats(user_name))


def main():
    user_name = welcome_user()
    brain_progression(user_name)

if __name__ == '__main__':
    main()