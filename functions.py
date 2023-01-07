"""Консольный файловый менеджер.

Дополнительный модуль: вспомогательные функции."""

import data


def show_menu():
    print('\n____ Главное Меню ____')
    for i, entry in enumerate(data.MainMenu, 1):
        print(f' {i}. {entry.value}')


def get_menu_entry() -> data.MainMenu:
    while True:
        inp = input(data.PROMPT)
        if inp.isdecimal():
            inp = int(inp)
            if inp in range(1, len(data.MainMenu)+1):
                return list(data.MainMenu)[inp-1]
            else:
                print(data.ERROR_MESSAGES['RANGE'])
        else:
            print(data.ERROR_MESSAGES['DIGITS'])


# тесты
if __name__ == '__main__':
    show_menu()
    print(get_menu_entry())