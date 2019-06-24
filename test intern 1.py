class Chitietdon:
    def __init__(self, name_don, weight, price):
        self.name_don = name_don
        self.weight = weight
        self.price = price

    def __repr__(self):
        return "Ma so chi tiet don: {0}, "\
               "Trong luong: {1}, "\
               "Gia thanh: {2}/////". format(self.name_don, self.weight, self.price)


class Chitietphuc:
    def __init__(self, name_phuc, list_items=[]):
        self.name_phuc = name_phuc
        self.list_items = list_items

    def add_items(self, item):
        if not self.list_items:
            self.list_items = []
        self.list_items.append(item)

    def __repr__(self):
        return "Ma so chi tiet phuc: {0}, " \
               "Cac chi tiet trong chi tiet phuc: {1}".format(self.name_phuc, self.list_items)


class Comay:
    def __init__(self, ten_may, list_items=[]):
        self.ten_may = ten_may
        self.list_items = list_items

    def add_items(self, item):
        if not self.list_items:
            self.list_items = []
        self.list_items.append(item)

    def __repr__(self):
        return "Ten may: {0}, " \
               "Cac chi tiet trong may: {1}".format(self.ten_may, self.list_items)


_list = [
    Comay("A1", [Chitietdon("CT001", 56, 47000), Chitietdon("CT002", 74, 75000), Chitietdon("CT003", 83, 56000)]),
    Comay("A2", [Chitietdon("CT004", 76, 88000), Chitietdon("CT005", 27, 38000), Chitietdon("CT006", 83, 93000)]),
    Comay("B1", [Chitietdon("CT004", 73, 46000), Chitietphuc("PT2000", [Chitietdon("CT005", 47, 94000),
                                                                        Chitietdon("CT006", 85, 35000)])]),
    Comay("B2", [Chitietphuc("PT3000", [Chitietdon("CT005", 83, 47000), Chitietdon("CT009", 73, 36000)]),
                 Chitietphuc("PT2000", [Chitietdon("CT005", 47, 94000), Chitietdon("CT006", 85, 35000)])])
]

num = 1
for i in range(0, len(_list)):
    print("%s)" % num, _list[i])
    num = num + 1
    if num <= len(_list):
        continue
    else:
        break




