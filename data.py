"""Консольный файловый менеджер.

Дополнительный модуль: глобальные переменные."""

from enum import Enum
from pathlib import Path
from sys import path


PROJECT_DIR = Path(path[0])
CWD = PROJECT_DIR


TITLE = "Консольный файловый менеджер"

PROMPT = ' > '
ERROR = ' _ '

class MainMenu(Enum):
    ADD = 'создать каталог'
    COPY = 'копировать файл/каталог'
    DEL = 'удалить файл/каталог'
    DIR = 'показать содержимое рабочего каталога'
    DIR_D = 'показать только каталоги в рабочем каталоге'
    DIR_F = 'показать только файлы в рабочем каталоге'
    CD = 'сменить рабочий каталог'
    OS = 'показать информацию об операционной системе'
    AUTHOR = 'показать информацию о создателе программы'
    QUIZ = 'викторина...'
    BANK = 'операции с банковским счётом...'
    QUIT = 'выйти'

MESSAGES = {
    'MAIN_MENU_TITLE': 'главное меню',
    'ASK_DIR_NAME': f'{PROMPT}введите имя каталога{PROMPT}',
    'ASK_FILE_OR_DIR_NAME': f'{PROMPT}введите имя файла или каталога{PROMPT}',
    'ASK_TARGET_NAME': f'{PROMPT}введите новое имя{PROMPT}',
    'ASK_PATH': f'{PROMPT}введите путь{PROMPT}',
}
ERROR_MESSAGES = {
    'DIGITS': f'{ERROR}требуются символы цифр{ERROR}',
    'RANGE': f'{ERROR}требуется число из диапазона{ERROR}',
    'DIR_NOT_FOUND': f'{ERROR}каталог не найден{ERROR}',
}


# тесты
if __name__ == '__main__':
    print(TITLE)
