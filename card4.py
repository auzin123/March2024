from random import shuffle

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
        'счет': 10
    }
    player_2 = {
        'человек': True,
        'имя': 'Ася',
        'карты': [],
        'счет': 10
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

deck = get_deck()
shuffle(deck)
players = get_players()
deals_card(2)
max_cards_per_turn = len(deck) // len(players)

for player in players:
    while True:
        print(player['имя'])
        show_cards()
        print('Сумма очков:', get_total_cards_values(player))
        player_option = input('Взять карту? y/n: ')
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

total_values = []
for player in players:
    total_values.append(get_total_cards_values(player))

# узнать самый большрй индекс самого большого счета, но без перебора (< 21)
condidates = []
for value in total_values:
    if value < 21:
        condidates.append(value)

for value in total_values:
        index = total_values.index(max(total_values))
        player = players(index)
        if value > 21:
            print(player['имя'], value,' - перебор!')
        elif value == 21:
            print(player['имя'], value, 'выиграл')
        else:
            pass
            

# печатать победителя