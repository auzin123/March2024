'''
ООП - Стиль Программирования
Класс - Фабрика Экземпляров, 
Экземпляр
класс Weapon
Дать каждому игроку оружие
Это оружие должно учавствовать в расчете атаки
'''


class Weapon:
    def __init__(self, name: str, weapon_attack: int, attack_power) -> None:
        self.name = name
        self.weapon_attack = weapon_attack * attack_power # влияет на атаку игрока
        print(self.weapon_attack)

Weapon('меч', 2 , 4)
        



class Player:
    '''
    Класс - это атрибуты + методы
    '''
    hp = 100

    def __init__(self, name: str, hp: int, attack_power: int, weapon=None) -> None:
        '''
        Конструктор Класса
        Экземплярный метод
        Вызываеться Сам сразу после созданеия экземпляра
        self - ссылка на сам экземпляр
        Все атрибуты определяються тут!
        '''
        self.attack_power = Weapon(self.attack_power)
        self.weapon = weapon
        self.name = name
        self.hp = 100  #  экземплярный атрибут
        



    def __str__(self) -> str:
        return f'Экземпляр Игрока, имя {self.name}, жизни {self.hp}'
    

    def show(self) -> None:
        print('имя:', self.name)
        print('жизни:', self.hp)
        print('-' * 10)


    def attack(self, enemy) -> None:
        '''Игрок атакует противника'''
        if self.hp <= 0:
            return
        damage = self.attack_power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name, 'на', damage)



class Game:
    def __init__(self) -> None:
        self.player = Player('Петя', 100, 4)
        self.enemy = Player('Вася', 100, 4)
        self.is_running = True
        self.fight()

    def fight(self) -> None:
        '''сражение'''
        while self.is_running:
            self.player.attack(self.enemy)
            print(self.player)
            self.player.attack(self.enemy)
            print(self.player)
            self.check_winner()

        
    def check_winner(self):
        if self.player.hp <= 0:
            print(self.enemy.name, 'победил')
            self.is_running = False
        elif self.enemy.hp <= 0:
            print(self.player.name, 'победил')
            self.is_running = False

