#!/usr/bin/env python3


def welcome_user():
    name = input('May I have your name? ')
    print(f'Hello, {name}!')


def brain_games():
    print('Welcome to the Brain Games!')
    # cli.welcome_user()
    welcome_user()


def main():
    brain_games()


if __name__ == '__main__':
    main()
