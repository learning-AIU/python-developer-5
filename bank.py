"""Консольный файловый менеджер.

Дополнительный модуль: операции с банковским счётом."""

from datetime import datetime as dt
from decimal import Decimal as dec

import functions

balance: dec = dec(0)
history: dict[dt, tuple[str, dec]] = {}


def get_menu_element() -> str:
    print(f"""\n{functions.draw_title('меню банка')}
  1. проверка баланса
  2. пополнение счета
  3. покупка
  4. история покупок
  5. выход""")
    while True:
        inp = input(' > введите номер > ')
        if inp in set('12345'):
            return inp
        else:
            print(' _ неверный пункт меню _ ')


def get_balance() -> None:
    print(f'\n = текущий баланс: {balance:.2f} ₽ = ')


def deposit() -> None:
    global balance
    balance += dec(input(' > введите сумму пополнения > '))


def buy() -> None:
    global balance, history
    amount = dec(input(' > введите сумму покупки > '))
    if amount <= balance:
        balance -= amount
        title = input(' > введите название покупки > ')
        history |= {dt.now(): (title, amount)}
    else:
        print(' _ недостаточно средств _ ')


def show_history() -> None:
    print('\n = история покупок = ')
    for timestamp, action in history.items():
        print(f'  {timestamp:%H:%M %d.%m.%y} — {action[0]}: {action[1]:.2f} ₽')


def start():
    while True:
        choice = get_menu_element()

        if choice == '1':
            get_balance()

        elif choice == '2':
            deposit()

        elif choice == '3':
            buy()

        elif choice == '4':
            show_history()

        elif choice == '5':
            break
