class Chitietdon:
    def __init__(self, name_don, weight, price):
        self.name_don = name_don
        self.weight = weight
        self.price = price

    def __repr__(self):
        return "Ma chi tiet don: {0}, "\
               "Trong luong: {1}, "\
               "Gia thanh: {2}". format(self.name_don, self.weight, self.price)


class Chitietphuc(Chitietdon):
    def __init__(self, name_phuc, name_don, weight, price):
        Chitietdon.__init__(self, name_don, weight, price)
        self.name_phuc = name_phuc

    def __repr__(self):
        return "Ma chi tiet phuc: {0}".format(self.name_phuc)


_list = {
    "Co may A1": [Chitietdon("CT001", 56, 47000), Chitietdon("CT002", 74, 75000), Chitietdon("CT003", 83, 56000)],
    "Co may B1": [Chitietdon("CT004", 73, 46000), Chitietphuc("PT2000", Chitietdon("CT005", 47, 94000),
                                                              Chitietdon("CT006", 84, 37000),
                                                              Chitietdon("CT007", 32, 36000))]
}

print(_list)







