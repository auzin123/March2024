import os

'''
ООП - Стиль Программирования
Класс - Фабрика Экземпляров, 
Экземпляр
класс Weapon
Дать каждому игроку оружие
Это оружие должно учавствовать в расчете атаки



добавления;

деньги

торговец

инвентарь:
оружие, зелья, броня

уровень сложности

оружие:
критическая атака

снаряжение:
предметы улучшающие или ухудшающие характеристики персонажа

бой:
применить предмет

игрок:
классы игрока:
лучник, маг, мечник
уровень
нагрда
отряд напарников

противник: 
босс

сюжет:
    события: (метеорит)
    квесты (простые, сложные)

'''
class Potion:
    def __init__(self) -> None:
        pass

class Weapon:
    def __init__(self, name: str, weapon_attack: int, attack_power) -> None:
        self.name = name
        self.weapon_attack = weapon_attack * attack_power  # влияет на атаку игрока

    def __str__(self) -> str:
        return f'{self.name} ({self.weapon_attack})'


class Player:
    '''
    Класс - это атрибуты + методы
    '''
    def __init__(self, name: str, hp: int, attack_power: int, weapon=None) -> None:
        '''
        Конструктор Класса
        Экземплярный метод
        Вызываеться Сам сразу после созданеия экземпляра
        self - ссылка на сам экземпляр
        Все атрибуты определяються тут!
        '''
        self.hp = 100
        self.attack_power = 1
        self.default_weapon = Weapon('кулаки', 1, 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.default_weapon
        self.name = name
        self.inventory = []

    def show(self) -> None:
        print(self.name.center(20, '_'))
        print('жизни:', self.hp)
        print('оружие:', self.weapon)
        print('инвентарь:', self.inventory)
        return f'Экземпляр Игрока, имя {self.name}, жизни {self.hp}'

    def attack(self, enemy) -> None:
        '''Игрок атакует противника'''
        if self.hp <= 0:
            return
        damage = self.attack_power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name, 'на', damage)


class Game:
    def __init__(self) -> None:
        self.player = Player('Петя', 100, 4, Weapon('Меч', 10, 1))
        self.is_running = False
        self.visit_hub()
        self.visit_shop()


    def visit_shop(self):
        while True:
            self.player.show()
            print('0 - Купить')
            option = input('Введите номер варианта: ')
            if option == '0':
                print('Вот разделы всех товаров:')
                print('1 - Оружие')
                print('2 - Броня')
                print('3 - Снаряжение')
                print('4 - Зелья')
                print('5 - Нанять напарника')
                print('6 - Обратно')
                option_1 = input('Какой раздел надо выбрать?')
                if option_1 == '1':
                    print('1 - меч холодец')
                    option_2 = input('Введите номер варианта: ')
                    if option_2 == '1':
                        self.player.inventory.append('меч холодец')
                        self.visit_hub()
                    elif option_2 == '0':
                        break

    def visit_hub(self):
            self.player.show()
            print('0 - Выйти из игры')
            print('1 - Сражаться')
            print('2 - Торговать')
            option = input('Введите номер варианта и нажмите ENTER: ')
            if option == '1':
                self.visit_arena()
            elif option == '2':
                self.visit.shop()
            else:
                pass

    def visit_arena(self) -> None:
        '''сражение'''
        self.enemy = Player('Вася', 100, 4)
        self.is_running = True
        while self.is_running:
            os.system('cls')
            self.player.show()
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


Game()
