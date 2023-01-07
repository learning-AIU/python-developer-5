"""Консольный файловый менеджер.

Основной модуль: точка входа."""

import data
import functions


def main():
    print(f'\n{data.TITLE}')
    while True:
        functions.show_menu()
        choice = functions.get_menu_entry()

        if choice is data.MainMenu.ADD:
            pass

        elif choice is data.MainMenu.COPY:
            pass

        elif choice is data.MainMenu.DEL:
            pass

        elif choice is data.MainMenu.DIR:
            pass

        elif choice is data.MainMenu.DIR_D:
            pass

        elif choice is data.MainMenu.DIR_F:
            pass

        elif choice is data.MainMenu.CD:
            pass

        elif choice is data.MainMenu.OS:
            pass

        elif choice is data.MainMenu.AUTHOR:
            pass

        elif choice is data.MainMenu.BANK:
            pass

        elif choice is data.MainMenu.QUIZ:
            pass

        elif choice is data.MainMenu.QUIT:
            break


# точка входа
if __name__ == '__main__':
    main()
