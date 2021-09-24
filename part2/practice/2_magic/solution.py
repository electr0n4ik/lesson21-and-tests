# Решение
class Item:
    def __init__(self, title: str, unit: str, price_for_unit: float, quantity: float):
        self.title = title
        self.unit = unit
        self.price_for_unit = price_for_unit
        self.quantity = quantity

    def get_price(self) -> float:
        price = float(self.price_for_unit * self.quantity)
        return price

    def __repr__(self):
        return f'{self.title}, {self.unit}, {self.quantity}{self.unit}, {self.get_price()} руб.'

    def __eq__(self, other):
        return self.get_price() == other.get_price()

    def __ne__(self, other):
        return self.get_price() != other.get_price()

    def __gt__(self, other):
        return self.get_price() > other.get_price()

    def __ge__(self, other):
        return self.get_price() <= other.get_price()

    def __lt__(self, other):
        return self.get_price() < other.get_price()

    def __le__(self, other):
        return self.get_price() <= other.get_price()


pythons = Item(title='Сушеные питоны',
               unit='г.',
               price_for_unit=1000,
               quantity=0.3)

pythons2 = Item(title='Сушеные питоны',
                unit='г.',
                price_for_unit=1000,
                quantity=0.3)

pythons3 = Item(title='Сушеные питоны',
                unit='г.',
                price_for_unit=1000,
                quantity=0.4)

print(pythons)  # Результат должен быть таким - Сушеные питоны, г., 0.3г., 300.0 руб.
assert pythons == pythons2, 'Ошибка в реализации __eq__'
assert pythons != pythons3, 'Ошибка в реализации __ne__'
assert pythons3 > pythons2, 'Ошибка в реализации __gt__'
assert pythons < pythons3, 'Ошибка в реализации __lt__'
assert pythons >= pythons2, 'Ошибка в реализации __ge__'
assert pythons <= pythons2, 'Ошибка в реализации __le__'


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert(pythons.__repr__() == 'Сушеные питоны, г., 0.3г., 300.0 руб.',
            correct='Функция __repr__ реализована правильно', incorrect='Функция __repr__ реализована  НЕ правильно')
test_assert(all((pythons == pythons2,
                 (pythons == pythons3) == False)), correct='Функция __eq__ реализована правильно',
            incorrect='Функция __eq__ реализована  НЕ правильно')
test_assert(all((pythons != pythons3,
                 (pythons != pythons2) == False)), correct='Функция __ne__ реализована правильно',
            incorrect='Функция __ne__ реализована  НЕ правильно')
test_assert(all((pythons3 > pythons2,
                 (pythons > pythons2) == False)), correct='Функция __gt__ реализована правильно',
            incorrect='Функция __gt__ реализована  НЕ правильно')
test_assert(all((pythons < pythons3,
                 (pythons3 < pythons2) == False)), correct='Функция __lt__ реализована правильно',
            incorrect='Функция __lt__ реализована  НЕ правильно')
test_assert(all((pythons >= pythons2,
                 (pythons3 >= pythons) == False)), correct='Функция __ge__ реализована правильно',
            incorrect='Функция __ge__ реализована  НЕ правильно')
test_assert(all((pythons <= pythons2,
                 (pythons3 <= pythons) == False)), correct='Функция __le__ реализована правильно',
            incorrect='Функция __le__ реализована  НЕ правильно')
