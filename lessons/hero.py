class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero1 = SuperHero("Макс", "СуперМакс", "Невидимость", 100, "Вперёд, к победе!")
print(hero1)
print(f"Здоровье до: {hero1.health_points}")
hero1.double_health()
print(f"Здоровье после: {hero1.health_points}")
print(hero1)
print(len(hero1))

class Air_Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def fraza(self):
        print('True in the True_phrase')

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.superpower}, {self.health_points}, {self.fly}'

hero3 = Air_Hero("Брюс", "Бэтмен", "Богатство", 1000, "Я Бэтмен :| !", 1000, fly=False)
print(hero3)
print(f"fly : {hero3.fly}")
print(f"Здоровье до: {hero3.health_points}")
hero3.double_health()
print(f"Здоровье после: {hero3.health_points}")
print(hero3)
print(f'fly = {hero3.fly}')

class Space_Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def fraza(self):
        print('True in the True_phrase')

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.superpower}, {self.health_points}, {self.fly}'

hero2 = Space_Hero("Кларк", "Супермен", "Криптонец", 1000000, "Никого не убивать!", 100000, fly=False)
print(hero2)
print(f"fly : {hero2.fly}")
print(f"Здоровье до: {hero2.health_points}")
hero2.double_health()
print(f"Здоровье после: {hero2.health_points}")
print(hero2)
print(f'fly = {hero2.fly}')
hero2.fraza()

class villain(Air_Hero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        Air_Hero.__init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly)

    def gen_(self):
        pass

    def crit(self):
        self.damage **= 2
        print(self.damage)

the_villain = villain("Думсдэй", "Разрушитель", "Доисторический криптонец", 1100000, "Я Бэтмен :| !", 110000, fly=False)
print(the_villain)
print(f"fly : {the_villain.fly}")
print(f"Здоровье до: {the_villain.health_points}")
the_villain.double_health()
print(f"Здоровье после: {the_villain.health_points}")
print(the_villain)
print(f'fly = {the_villain.fly}')
the_villain.fraza()
the_villain.crit()





