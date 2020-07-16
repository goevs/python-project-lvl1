#!/usr/bin/env python3


"""My first programm."""


from brain_games.cli import welcome_user


def greet():
    """Doc str."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    welcome_user()


def main():
    """Doc str."""
    greet()


if __name__ == '__main__':
    main()
