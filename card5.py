from random import shuffle
from os import system 
system('cls')
'''
Карты:
    имя
    цена
    масть

Колода: всего карт = цены * масти
    в 1 масти: 6, 7, 8, 9, 10, валет, дама, король, туз

Игроки - от 2 штук

Колода перемешивается

Кажому игроку выдается по 2 карты из колоды

Игрок види только свои карты

Задача - цены всех карт игрока = 21

Ход игрока:
    оставить свои карты и больше не набирать
    или взять еще карту (сколько угодно раз)

Все игроки должны закончить ход

Если у игрока сумма цен всех карт > 21, он проиграл
Если у всех игроков проигрыш, то это ничья

Выигрывает тот, у кого больше очков и тот, кто не проиграл
'''


def get_deck() -> list[dict]:
    suits = ['бубны', 'черви', 'пики', 'крести'] # создаем масти карт
    names = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'] #создаем имена для карт
    deck = []  # создаем пустую колоду

    for suit in suits: 
        for name in names:
            if name in ('валет', 'дама', 'король'):
                value = 10
            elif name == 'туз':
                value = 11
            else:
                value = int(name) 
            card = {
                'имя': name,
                'цена': value,
                'масть': suit
            }
            deck.append(card)
    return deck


def get_players():
    '''
    возвращает список игроков
    '''
    player_1 = {
        'человек': True,
        'имя': 'Вася',
        'карты': [],
        'счет': 10,
        'сумма': 0
    }
    player_2 = {
        'человек': False,
        'имя': 'Ася',
        'карты': [],
        'счет': 10,
        'сумма': 0
    }
    return [player_1, player_2]


def deals_card(num: int) -> None:
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop(-1))


def get_total_cards_values(player: dict) -> int:             
    total = 0
    for card in player['карты']:
        total += card['цена']
    return total

def show_cards() -> None:
    '''
    показывает карты игрока
    '''
    for card in player['карты']:
        print(card['имя'], card['масть'])


def show_statistic() -> None:
    for player in players:
        if player['сумма'] < 22:
            print(f"{player['имя']} - {player['сумма']} - перебор")
        else:
            print(f"{player['имя']} - {player['сумма']} - перебор")


def show_result() -> None:
    totals_values = []
    for player in players:
        totals_values.append(player['сумма'])

    # Если у всех перебор    
    if all(num > 21 for num in totals_values):
        print('Ничья')

    # Если у всех одинаковaя сумма
    elif all(num == totals_values[0] for num in totals_values):
        print('Ничья')

    # Иначе - взять игрока с самой большой суммой
    for player in players:
        if player 
        print('Победил  игрок')


deck = get_deck()
shuffle(deck)
players = get_players()
deals_card(2)
max_cards_per_turn = len(deck) // len(players)
system('cls')
for player in players:
    while True:
        print(player['имя'])
        show_cards()
        player['сумма'] = get_total_cards_values(player)
        print('Сумма очков:', player['сумма'])
        if player['человек']:
            player_option = input('Взять карту? y/n: ')
        else: 
            if player['сумма'] < 17:
                player_option = 'y'
            else:
                player_option = 'n'

        if player_option == 'y':
            if len(player['карты']) > max_cards_per_turn:
                player['карты'].append(deck.pop(-1))
            else:
                print('Невозможно взять еще карту!')
                break
        else:
            break
    input('ENTER - ход следующего игрока ')
print('партия закончена')



show_cards()
show_result()
show_statistic()