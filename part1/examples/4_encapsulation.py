class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 5
        self.hungry = 5
        self.mood = 5

    def _meow(self):
        print('Мяу!')

    @staticmethod
    def _check_attr(attr):
        """Быстренько проверяем что мы не вышли за допустимые диапазоны """
        if attr < 0:
            attr = 0
        if attr > 10:
            attr = 10
        return attr

    def _check_attrs(self):
        """Проверяем диапазоны для наших значений"""
        self.energy = self._check_attr(self.energy)
        self.hungry = self._check_attr(self.hungry)
        self.mood = self._check_attr(self.mood)

    def _check_state(self):
        """ Внутренняя реализация мяучела/мурчала кота.
        Внешний пользователь не должен догадываться о нашем алгоритме"""
        self._check_attrs()
        if self.hungry > 8:
            self._meow()
        if self.energy < 2:
            self._meow()

    def feed(self):
        """Основная фукнция человеков - кормить своего пушистого господина """
        print('===Покормили===')
        self.hungry -= 2
        self.mood += 1
        self._check_state()

    def play(self):
        """ Развлекать пушистого господина"""
        print('===Поиграли===')
        self.hungry += 1
        self.energy -= 3
        self.mood += 2
        self._check_state()

    def pet(self):
        """Погладить"""
        print('===Погладили===')
        self.hungry += 1
        self.mood += 1
        self._check_state()

    def put_to_sleep(self):
        """ Пушистый господин, возможно, желает почивать"""
        print('===Попробовали уложить спать===')
        self.hungry += 4
        self.mood = 5
        self.energy += 4

    def slipper(self):
        """ Иногда в пушистого господина надо бросить тапком"""
        print('===Меткий бросок===')
        self.mood -= 9
        self._check_state()


print('\nвзаимосвязь взаимодействия с классом через публичные методы с приватными это и есть инкапсуляция\n')

cat = Cat(name='Барсик')
cat.pet()
cat.play()
cat.play()
cat.slipper()
cat.put_to_sleep()
cat.pet()
cat.feed()
cat.pet()
