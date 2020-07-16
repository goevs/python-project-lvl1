"""Doc str."""


import prompt


def welcome_user():
    """Doc str."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
