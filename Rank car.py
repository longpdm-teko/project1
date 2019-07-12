class Car:
    def __init__(self, model, year, mileage, title, price, distance, color, owners):
        self.model = model
        self.year = year
        self.mileage = mileage
        self.title = title
        self.price = price
        self.distance = distance
        self.color = color
        self.owners = owners

    def __get_title(self):
        return self.title

    def __repr__(self):
        return "Model: {0}, " \
               "Year: {1}, " \
               "Mileage: {2} miles, " \
               "Title: {3}, " \
               "Price: $ {4}, " \
               "Distance from Aunt Tien: {5} miles, " \
               "Color: {6}, " \
               "Owners: {7} /////".format(self.model, self.year, self.mileage, self.title,
                                          self.price, self.distance, self.color, self.owners)



class Title:
    def __init__(self, condition, seq):
        self.condition = condition
        self.seq = seq

    def __repr__(self):
        return "{}".format(self.condition)


class Owners:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "{}".format(self.number)


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

_owners1 = Owners(1)
_owners2 = Owners(2)

_year1 = Year(2014)
_year2 = Year(2015)
_year3 = Year(2016)
_year4 = Year(2017)

_color1 = Color('black', 0)
_color2 = Color('silver', 0)
_color3 = Color('gray', 0)
_color4 = Color('gold', 1)
_color5 = Color('white', 1)
_color6 = Color('cream', 1)


_list = [
    Car("Toyota Camry SE", _year2, 92441, _condition1, 10991, 5, _color3, _owners1),
    Car("Toyota Camry SE", _year1, 78150, _condition1, 10800, 6, _color1, _owners2),
    Car("Toyota Camry Hybrid LE", _year2, _condition1, "clean", 13791, 10, _color3, _owners1),
    Car("Toyota Camry LE", _year3, 88648, _condition1, 11650, 12, _color1, _owners2),
    Car("Toyota Camry SE", _year3, 79857, _condition1, 11993, 20, _color2, _owners1),
    Car("Toyota Camry XLE V6", _year2, 70533, _condition1, 12995, 39, _color2, _owners2),
    Car("Toyota Camry LE", _year2, 58195, _condition1, 12495, 3, _color4, _owners2),
    Car("Toyota Camry LE", _year2, 86834, _condition1, 10691, 16, _color5, _owners2),
    Car("Toyota Camry LE", _year4, 96541, _condition1, 11359, 18, _color6, _owners2),
    Car("Toyota Camry LE", _year1, 33452, _condition1, 12998, 22, _color6, _owners2),
]

for i in range(len(_list) - 1, 0, -1):
    for j in range(i):
        if _list[j].owners > _list[j + 1].owners:
            a = _list[j]
            _list[j] = _list[j + 1]
            _list[j + 1] = a

for i in range(len(_list) - 1, 0, -1):
    for j in range(i):
        if _list[j].distance > _list[j + 1].distance:
            a = _list[j]
            _list[j] = _list[j + 1]
            _list[j + 1] = a

for i in range(len(_list) - 1, 0, -1):
    for j in range(i):
        if _list[j].year < _list[j + 1].year:
            a = _list[j]
            _list[j] = _list[j + 1]
            _list[j + 1] = a

for i in range(len(_list) - 1, 0, -1):
    for j in range(i):
        if _list[j].price > _list[j + 1].price:
            a = _list[j]
            _list[j] = _list[j + 1]
            _list[j + 1] = a

for i in range(len(_list) - 1, 0, -1):
    for j in range(i):
        if _list[j].mileage > _list[j + 1].mileage:
            a = _list[j]
            _list[j] = _list[j + 1]
            _list[j + 1] = a

for i in range(len(_list) - 1, 0, -1):
    for j in range(i):
        if _list[j].color.seq > _list[j + 1].color.seq:
            a = _list[j]
            _list[j] = _list[j + 1]
            _list[j + 1] = a

num = 1
for i in range(0, len(_list)):
    print("%s)" % num, _list[i])
    num = num + 1
    if num <= len(_list):
        continue
    else:
        break



