class Car:
    def __init__(self, model, year, mileage, title, price, distance, color, owners):
        self.model = model
        self.year = year
        self.mileage = mileage
        self.title = title
        self.price = price
        self.distance = distance
        self.color = color
        self.__owners = owners

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_distance(self):
        return self.distance

    def get_color(self):
        return self.color

    def __get_owners(self):
        return self.__owners

    def get_ownership(self):
        if self.__get_owners() <= 2:
            return "Qualified"
        else:
            return "Disqualified"

    def get_gas_per_mile(self):
        pass

    def start_time(self):
        return "Car start time depends on their model"


class Toyota(Car):
    def __init__(self, model, year, mileage, title, price, distance, color, owners, hot_chairs):
        super(Toyota, self).__init__(model, year, mileage, title, price, distance, color, owners)
        self.hot_chairs = hot_chairs

    def get_gas_per_mile(self):
        return (self.mileage / 100000) * 5

    def start_time(self):
        return "Toyota car starts in 3 seconds"

    def __repr__(self):
        return "Model: {0}, " \
               "Year: {1}, " \
               "Mileage: {2} miles, " \
               "Title: {3}, " \
               "Price: $ {4}, " \
               "Distance from home: {5} miles, " \
               "Color: {6}, " \
               "Ownership: {7}, "\
               "Hot chairs: {8}".format(self.model, self.year, self.mileage, self.title, self.price, self.distance,
                                        self.color, self.get_ownership(), self.hot_chairs)


class Ford(Car):
    def __init__(self, model, year, mileage, title, price, distance, color, owners, black_lights):
        super(Ford, self).__init__(model, year, mileage, title, price, distance, color, owners)
        self.black_lights = black_lights

    def get_gas_per_mile(self):
        return (self.mileage / 80000) * 6

    def start_time(self):
        return "Ford car starts in 2 seconds"

    def __repr__(self):
        return "Model: {0}, " \
               "Year: {1}, " \
               "Mileage: {2} miles, " \
               "Title: {3}, " \
               "Price: $ {4}, " \
               "Distance from home: {5} miles, " \
               "Color: {6}, " \
               "Ownership: {7}, "\
               "Black lights: {8}".format(self.model, self.year, self.mileage, self.title, self.price, self.distance,
                                          self.color, self.get_ownership(), self.black_lights)


class Title:
    def __init__(self, condition, seq):
        self.condition = condition
        self.seq = seq

    def __repr__(self):
        return "{}".format(self.condition)


class Year:
    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return "{}".format(self.year)


class Color:
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq

    def __repr__(self):
        return "{}".format(self.name)


_condition1 = Title("clean", 0)
_condition2 = Title("damaged", 1)

_year1 = Year(2014)
_year2 = Year(2015)
_year3 = Year(2016)
_year4 = Year(2017)

_color1 = Color('black', 0)
_color2 = Color('silver', 1)
_color3 = Color('gray', 2)
_color4 = Color('gold', 3)
_color5 = Color('white', 4)
_color6 = Color('cream', 5)

_car1 = Toyota("T1", _year2, 92441, _condition1, 10991, 5, _color3, 1, 3)
_car2 = Ford("F1", _year1, 78150, _condition2, 10800, 6, _color1, 2, 4)
_car3 = Toyota("T2", _year2, 44656, _condition1, 13791, 10, _color3, 4, 3)
_car4 = Ford("F2", _year3, 88648, _condition2, 11650, 12, _color1, 3, 4)
_car5 = Toyota("T3", _year3, 79857, _condition1, 11993, 20, _color2, 2, 3)
_car6 = Ford("F3", _year2, 70533, _condition2, 12995, 39, _color2, 3, 4)
_car7 = Toyota("T4", _year2, 58195, _condition1, 12495, 3, _color4, 1, 3)
_car8 = Ford("F4", _year2, 86834, _condition2, 10691, 16, _color5, 2, 4)
_car9 = Toyota("T5", _year4, 96541, _condition1, 11359, 18, _color6, 4, 3)
_car10 = Ford("F5", _year1, 33452, _condition2, 12998, 22, _color6, 5, 4)

_list = [_car1, _car2, _car3, _car4, _car5, _car6, _car7, _car8, _car9, _car10]


def print_list():
    num = 1
    for i in range(0, len(_list)):
        print("%s)" % num, _list[i])
        num = num + 1
        if num <= len(_list):
            continue
        else:
            break


def sort_price():
    for i in range(len(_list) - 1, 0, -1):
        for j in range(i):
            if _list[j].price > _list[j + 1].price:
                a = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = a
    print_list()


def sort_year():
    for i in range(len(_list) - 1, 0, -1):
        for j in range(i):
            if _list[j].year.year > _list[j + 1].year.year:
                a = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = a
    print_list()


def sort_mileage():
    for i in range(len(_list) - 1, 0, -1):
        for j in range(i):
            if _list[j].mileage > _list[j + 1].mileage:
                a = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = a
    print_list()


def sort_color():
    for i in range(len(_list) - 1, 0, -1):
        for j in range(i):
            if _list[j].color.seq > _list[j + 1].color.seq:
                a = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = a
    print_list()


def sort_title():
    for i in range(len(_list) - 1, 0, -1):
        for j in range(i):
            if _list[j].title.seq > _list[j + 1].title.seq:
                a = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = a
    print_list()


def sort_distance():
    for i in range(len(_list) - 1, 0, -1):
        for j in range(i):
            if _list[j].distance > _list[j + 1].distance:
                a = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = a
    print_list()

