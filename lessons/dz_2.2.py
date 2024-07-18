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


# Пример использования
hero1 = SuperHero("Макс", "СуперМакс", "Невидимость", 100, "Вперёд, к победе!")
print(f"Здоровье до: {hero1.health_points}")
hero1.double_health()
print(f"Здоровье после: {hero1.health_points}")
print(hero1)
print(len(hero1))