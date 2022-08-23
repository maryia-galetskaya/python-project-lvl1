#!/usr/bin/env python3
#import cli 
import prompt

def welcome_user ():
    name = prompt.string('May I have your name? ')
    print (f'Hello, {name}!')

def brain_games():
    print('Welcome to the Brain Games!')
    #cli.welcome_user()
    welcome_user()


def main():
    brain_games()

if __name__ == '__main__':


    main()
