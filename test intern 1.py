class ChiTiet:
    def __init__(self, name):
        self.name = name

    def get_price(self):
        pass

    def get_weight(self):
        pass

    def __repr__(self):
        return "name: {0}, price: {1}, weight: {2} ".format(self.name, self.get_price(), self.get_weight())


class Chitietdon(ChiTiet):
    def __init__(self, name, weight, price):
        super(Chitietdon, self).__init__(name)
        self.weight = weight
        self.price = price

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight


class Chitietphuc(ChiTiet):
    def __init__(self, name, list_items=[]):
        super(Chitietphuc, self).__init__(name)
        self.list_items = list_items

    def get_price(self):
        total = 0
        for item in self.list_items:
            total += item.get_price()
        return total

    def get_weight(self):
        total = 0
        for item in self.list_items:
            total += item.get_weight()
        return total

    def add_items(self, item):
        if not self.list_items:
            self.list_items = []
        self.list_items.append(item)


# class Comaydon:
#     def __init__(self, ten_may, list_may_don=[]):
#         self.ten_may = ten_may
#         self.list_may_don = list_may_don
#
#     def add_items(self, item):
#         if not self.list_may_don:
#             self.list_may_don = []
#         self.list_may_don.append(item)
#
#     def __repr__(self):
#         return "Ten may: {0}, " \
#                "Cac chi tiet trong may: {1}".format(self.ten_may, self.list_may_don)
#
#
# class Comayphuc:
#     def __init__(self, ten_may, list_may_phuc=[]):
#         self.ten_may = ten_may
#         self.list_may_phuc = list_may_phuc
#
#     def add_items(self, item):
#         if not self.list_may_phuc:
#             self.list_may_phuc = []
#         self.list_may_phuc.append(item)
#
#     def __repr__(self):
#         return "Ten may: {0}, " \
#                "Cac chi tiet trong may: {1}".format(self.ten_may, self.list_may_phuc)


# _list_may_don = [
#     Comaydon("A1", [Chitietdon("CT001", 56, 47000), Chitietdon("CT002", 74, 75000), Chitietdon("CT003", 83, 56000)]),
#     Comaydon("A2", [Chitietdon("CT004", 76, 88000), Chitietdon("CT005", 27, 38000), Chitietdon("CT006", 83, 93000)])
# ]
#
# num = 1
# print("List cac may toan chi tiet don: ")
# for i in range(0, len(_list_may_don)):
#     print("%s)" % num, _list_may_don[i])
#     num = num + 1
#     if num <= len(_list_may_don):
#         continue
#     else:
#         break
#
# b = 0
# for i in _list_may_don:
#     for j in i.list_may_don:
#         a = j.price
#         b = a + b
#     print("Tong gia tri cua may {0}: {1} vnd".format(i.ten_may, b))
#
# c = 0
# for i in _list_may_don:
#     for j in i.list_may_don:
#         d = j.weight
#         c = c + d
#     print("Tong trong luong cua may {0}: {1} kg".format(i.ten_may, c))
#
# _list_may_phuc = [
#     Comayphuc("B1", [Chitietdon("CT004", 73, 46000), Chitietphuc("PT2000", [Chitietdon("CT005", 47, 94000),
#                                                                             Chitietdon("CT006", 85, 35000)])]),
#     Comayphuc("B2", [Chitietphuc("PT3000", [Chitietdon("CT005", 83, 47000), Chitietdon("CT009", 73, 36000)]),
#                      Chitietphuc("PT2000", [Chitietdon("CT005", 47, 94000), Chitietdon("CT006", 85, 35000)])])
# ]
#
# print("")
#
# num = 1
# print("List cac may gom chi tiet don va chi tiet phuc: ")
# for i in range(0, len(_list_may_phuc)):
#     print("%s)" % num, _list_may_phuc[i])
#     num = num + 1
#     if num <= len(_list_may_phuc):
#         continue
#     else:
#         break

d1 = Chitietdon("CT001", 73, 1000)
d2 = Chitietdon("CT002", 73, 2000)
d3 = Chitietdon("CT003", 73, 3000)
d4 = Chitietdon("CT004", 73, 4000)

p1 = Chitietphuc("B1", [d1, d2])
p2 = Chitietphuc("B2", [d3, p1])
p3 = Chitietphuc("B3", [p2, d4])

print(p3)

# n = Chitietphuc("B1", [, Chitietphuc("PT2000", [Chitietdon("CT005", 47, 94000),
#                                                                               Chitietdon("CT006", 85, 35000)])])
# print(n.get_price())
