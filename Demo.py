import datetime

now = datetime.datetime.now()
print("Welcome to car sorting program!")


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

    def get_ownership(self):
        if self.__owners <= 2:
            return "Qualified"
        else:
            return "Disqualified"

    def get_start_time(self):
        return "Car start time depends on their model"

    def get_depreciation_rate(self):
        return int(100 / (now.year - self.year)) * 2


class Toyota(Car):
    def __init__(self, model, year, mileage, title, price, distance, color, owners, hot_chairs):
        super(Toyota, self).__init__(model, year, mileage, title, price, distance, color, owners)
        self.hot_chairs = hot_chairs

    def get_start_time(self):
        return "Toyota car starts in 3 seconds"

    def __repr__(self):
        return "Model: {0}, " \
               "Year: {1}, " \
               "Mileage: {2} miles, " \
               "Title: {3}, " \
               "Price: $ {4}, " \
               "Distance from home: {5} miles, " \
               "Color: {6}, " \
               "Ownership: {7}, " \
               "Hot chairs: {8}, " \
               "Start time: {9}, " \
               "Depreciation rate: {10}%".format(self.model, self.year, self.mileage, self.title, self.price,
                                                 self.distance, self.color, self.get_ownership(), self.hot_chairs,
                                                 self.get_start_time(), self.get_depreciation_rate())


class Ford(Car):
    def __init__(self, model, year, mileage, title, price, distance, color, owners, black_lights):
        super(Ford, self).__init__(model, year, mileage, title, price, distance, color, owners)
        self.black_lights = black_lights

    def get_start_time(self):
        return "Ford car starts in 2 seconds"

    def __repr__(self):
        return "Model: {0}, " \
               "Year: {1}, " \
               "Mileage: {2} miles, " \
               "Title: {3}, " \
               "Price: $ {4}, " \
               "Distance from home: {5} miles, " \
               "Color: {6}, " \
               "Ownership: {7}, " \
               "Black lights: {8}, " \
               "Start time: {9}, " \
               "Depreciation rate: {10}%".format(self.model, self.year, self.mileage, self.title, self.price,
                                                 self.distance, self.color, self.get_ownership(), self.black_lights,
                                                 self.get_start_time(), self.get_depreciation_rate())


def integer_input(title):
    while True:
        try:
            result = int(input(title))
            return result
        except ValueError:
            print("Enter numbers for this value!")
            continue


def user_input():
    while True:
        _input_brand = input("Enter Brand: ").upper()
        a = "Toyota".upper()
        b = "Ford".upper()
        if _input_brand == a or _input_brand == b:
            _input_model = input("Enter Model: ")
            _input_year = integer_input("Enter Year: ")
            _input_mileage = integer_input("Enter Mileage: ")
            _input_title = input("Enter Title: ")
            _input_price = integer_input("Enter Price: ")
            _input_distance = integer_input("Enter Distance from home: ")
            _input_color = input("Enter Color: ")
            _input_owners = integer_input("Enter Owners: ")
            if _input_brand == a:
                _input_hot_chairs = integer_input("Enter Hot Chairs: ")
                _Toyota_input = Toyota(_input_model, _input_year, _input_mileage, _input_title, _input_price,
                                       _input_distance, _input_color, _input_owners, _input_hot_chairs)
                return _Toyota_input
            elif _input_brand == b:
                _input_black_lights = integer_input("Enter Black Lights: ")
                _Ford_input = Ford(_input_model, _input_year, _input_mileage, _input_title, _input_price,
                                   _input_distance, _input_color, _input_owners, _input_black_lights)
                return _Ford_input
        else:
            print("Enter a different brand!")
            TypeError()


def print_cars():
    _list_cars = []
    while True:
        _input = input("Do you want to put in some cars? Y/N : ").upper()
        if _input == "Y".upper():
            _car = user_input()
            _list_cars.append(_car)
        elif _input == "N".upper():
            return _list_cars
        else:
            print("Enter Y or N!")
            TypeError()


def list_cars(list_car):
    num = 1
    for car in list_car:
        print("%s) " % num, car)
        num += 1


def sort(list_car, key):
    n = len(list_car)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if getattr(list_car[j], key) > getattr(list_car[j + 1], key):
                a = list_car[j]
                list_car[j] = list_car[j + 1]
                list_car[j + 1] = a
    return list_car


def export(list_car, key):
    while True:
        _export = input("Do you want to export this sorting to another file? Y/N: ").upper()
        if _export == "Y".upper():
            file = open(input("Enter file name: "), "w")
            file.write(str(sort(list_car, key)))
            file.close()
            print("%s exported successful!" % file.name)
            break
        elif _export == "N".upper():
            return _key
        else:
            print("Enter Y or N!")
            TypeError()


if __name__ == '__main__':
    p = print_cars()
    while True:
        _key = input("Enter price, mileage, or year to sort/ end to stop program: ")
        if _key == "price" or _key == "mileage" or _key == "year":
            sort(p, _key)
            list_cars(p)
            export(p, _key)
        elif _key == "end":
            print("Thanks for using this program!")
            break
        else:
            print("Enter request!")
            TypeError()





