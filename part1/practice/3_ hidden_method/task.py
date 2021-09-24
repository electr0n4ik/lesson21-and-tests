#### Блок кода для перехвата вывода в консоль ####
import sys

output_data = []


def print(s):
    sys.stdout.write(s)
    sys.stdout.write('\n')
    output_data.append(s)


#### /Блок кода для перехвата вывода в консоль ####

# Стартовый код
class Company:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone


class Discount:
    def __init__(self):
        self.discounts = {}

    def add_discount(self, title: str, discount: float):
        pass

    def check_discount(self, title: str) -> float:
        pass


class Item:
    def __init__(self, title: str, unit: str, price_for_unit: float, quantity: float, discount: Discount):
        self.title = title
        self.unit = unit
        self.price_for_unit = price_for_unit
        self.quantity = quantity
        self.discount = discount

    def get_price(self) -> float:
        price = float(self.price_for_unit * self.quantity)
        return self._calculate_discount(price)

    def _calculate_discount(self, price: float):
        pass


class Receipt:
    def __init__(self):
        self.company = None
        self.items = []
        self.discount = Discount()

    def set_company(self, company: Company):
        self.company = company

    def set_discount(self, discount: Discount):
        self.discount = discount

    def add_item(self, title: str, unit: str, price_for_unit: float, quantity: float):
        item = Item(title=title,
                    unit=unit,
                    price_for_unit=price_for_unit,
                    quantity=quantity,
                    discount=self.discount)
        self.items.append(item)

    def print(self):
        total_price = 0

        for item in self.items:
            title_with_unit = f'{item.title}, {item.unit}'
            print(f'{title_with_unit} - {item.quantity} - {item.get_price()}')
            total_price += item.get_price()
        print(f'Всего: {total_price}')


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_disc = 0.8
test_discount = Discount()
test_discount.add_discount(title='котики', discount=test_disc)

test_assert(
    output_data == ['Сушеные питоны, упаковка. - 5 - 450.0',
                    'Книги про PHP, шт. - 10 - 11.0',
                    'Кофе плохорастворенный, л. - 0.2 - 200.0',
                    'Всего: 661.0'], correct='Вывод в консоль верный', incorrect='Вывод в консоль НЕ верный')

test_item = Item(title='котики',
                 unit='шт.',
                 price_for_unit=100,
                 quantity=1,
                 discount=test_discount)
test_value = test_discount.check_discount(title='котики')

test_assert(test_value == test_disc, correct='Функции класса Discount реализованы верно',
            incorrect='Функции класса Discount реализованы НЕ верно')
test_assert(test_item.get_price() >19.999 and test_item.get_price() <=20, correct='Функиця "_calculate_discount" класса Item реализована верно',
            incorrect='Функиця "_calculate_discount" класса Item реализована НЕ верно')
