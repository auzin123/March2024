'''
ООП - Стиль Программирования
Класс - Фабрика Экземпляров, 
Экземпляр
'''


class Player:
    '''
    Класс - это атрибуты + методы
    '''
    hp = 100

    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        '''
        Конструктор Класса
        Экземплярный метод
        Вызываеться Сам сразу после созданеия экземпляра
        self - ссылка на сам экземпляр
        Все атрибуты определяються тут!
        '''
        self.attack_power = 10
        self.name = name
        self.hp = 100  #  экземплярный атрибут
        

    def __str__(self) -> str:
        return f'Экземпляр Игрока, имя {self.name}, жизни {self.hp}'
    

    def show(self) -> None:
        print('имя:', self.name)
        print('жизни:', self.hp)
        print('-' * 10)


    def attack(self, enemy) -> None:
        while True:
            self.enemy.hp -= self.player.attack_power
            self.player.show()
            print(
                self.enemy.name,
                'атаковал',
                self.enemy.name,
                'на',
                self.player.attack_power
        )



class Game:
    def __init__(self) -> None:
        self.player = Player('Петя', 100, 10)
        self.enemy = Player('Вася', 10, 10)
        self.is_runninh = True
        self.fight()

    def fight(self) -> None:
        self.is_running = True
        while self.is_running:
            self.player.attack(self.enemy)
            self.player.attack(self.enemy)

# TODO: завершить бой при проигрыше одного из соперников

Game()