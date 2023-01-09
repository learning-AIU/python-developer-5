"""Консольный файловый менеджер.

Основной модуль: точка входа."""

import data
import files
import functions


def main():
    print(f'\n{functions.draw_title(data.TITLE, upper=True, accent=True)}')
    while True:
        functions.show_menu()
        choice = functions.get_menu_entry()

        if choice is data.MainMenu.ADD:
            files.create_dir()

        elif choice is data.MainMenu.COPY:
            files.copy_file_or_dir()

        elif choice is data.MainMenu.DEL:
            files.delete_file_or_dir()

        elif choice is data.MainMenu.DIR:
            files.list_dir()

        elif choice is data.MainMenu.DIR_D:
            files.list_dir(only_dirs=True)

        elif choice is data.MainMenu.DIR_F:
            files.list_dir(only_files=True)

        elif choice is data.MainMenu.CD:
            files.change_cwd()

        elif choice is data.MainMenu.OS:
            functions.os_platform()

        elif choice is data.MainMenu.AUTHOR:
            functions.show_credits()

        elif choice is data.MainMenu.BANK:
            pass

        elif choice is data.MainMenu.QUIZ:
            pass

        elif choice is data.MainMenu.QUIT:
            break


# точка входа
if __name__ == '__main__':
    main()
