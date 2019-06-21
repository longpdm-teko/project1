import datetime
now = datetime.datetime.now()

class Nvsx:
    def __init__(self,full_name, year_of_entry, products_made):
        self.full_name = full_name
        self.year_of_entry = year_of_entry
        self.products_made = products_made

    def check(self):
        return self.pay_check(self.products_made)

    @staticmethod
    def pay_check(p):
        return p * 10000 * 10000

    def years(self):
        return self.count_years(now.year, self.year_of_entry)

    @staticmethod
    def count_years(y, m):
        return y - m

    def luong_phu(self):
        return self.phu_cap(self.count_years(now.year, self.year_of_entry))

    @staticmethod
    def phu_cap(c):
        return 500000 + 50000 * c

    def luong_chinh_thuc(self):
        return self.luong_tong(self.pay_check(self.products_made), self.phu_cap(self.count_years
                                                                                (now.year, self.year_of_entry)))

    @staticmethod
    def luong_tong(p, c):
        return p + c

    def __repr__(self):
        return "Ho va Ten: {0}, "\
               "Nam vao lam: {1}, "\
               "Tong so nam o cong ty: {2}, "\
               "Tong so san pham: {3}, "\
               "Luong nhan vien: {4}, "\
               "Luong tong cong mot thang: {5}".format(self.full_name, self.year_of_entry,
                                                       self.count_years(now.year, self.year_of_entry),
                                                       self.products_made, self.pay_check(self.products_made),
                                                       self.luong_tong(self.pay_check(self.products_made),
                                                                       self.phu_cap(self.count_years
                                                                                   (now.year, self.year_of_entry))))


class Nvvp:
    def __init__(self, full_name, year_of_entry, salary, off_days):
        self.full_name = full_name
        self.year_of_entry = year_of_entry
        self.salary = salary
        self.off_days = off_days

    def check(self):
        return self.pay_check(self.salary, self.off_days)

    @staticmethod
    def pay_check(s, d):
        return s - d

    def years(self):
        return self.count_years(now.year, self.year_of_entry)

    @staticmethod
    def count_years(y, m):
        return y - m

    def luong_phu(self):
        return self.phu_cap(self.count_years(now.year, self.year_of_entry))

    @staticmethod
    def phu_cap(c):
        return 500000 + 50000 * c

    def luong_chinh_thuc(self):
        return self.luong_tong(self.pay_check(self.salary, self.off_days), self.phu_cap(self.count_years
                                                                                       (now.year, self.year_of_entry)))

    @staticmethod
    def luong_tong(p, c):
        return p + c

    def __repr__(self):
        return "Ho va Ten: {0}, "\
               "Nam vao lam: {1}, " \
               "Tong so nam o cong ty: {2}, "\
               "Muc luong: {3}, " \
               "Ngay nghi: {4}, "\
               "Luong nhan vien: {5}, "\
               "Luong tong cong mot thang: {6}".format(self.full_name, self.year_of_entry,
                                                       self.count_years(now.year, self.year_of_entry),
                                                       self.salary, self.off_days,
                                                       self.pay_check(self.salary, self.off_days),
                                                       self.luong_tong(self.pay_check(self.salary, self.off_days),
                                                                       self.phu_cap(self.count_years
                                                                                   (now.year, self.year_of_entry))))


_list_nvsx = [
    Nvsx("Nguyen Van A", 2008, 54),
    Nvsx("Pham Ngoc B", 2011, 34),
    Nvsx("Phan Hai C", 2003, 23),
    Nvsx("Phan Duc D", 2012, 34),
    Nvsx("Phung Quang E", 2006, 35)
]


num = 1
print("Nhan vien san xuat: ")
for i in range(0, len(_list_nvsx)):
    print("%s)" % num, _list_nvsx[i])
    num = num + 1
    if num <= len(_list_nvsx):
        continue
    else:
        break

print("")

_list_nvvp = [
    Nvvp("Pham van A", 2005, 15, 6),
    Nvvp("Phung Ngoc B", 2006, 12, 4),
    Nvvp("Dung Quang C", 2004, 27, 4),
    Nvvp("Ha Ton D", 2007, 12, 2),
    Nvvp("Nguyen Ngoc E", 2008, 13, 2)
]

num = 1
print("Nhan vien van phong: ")
for i in range(0, len(_list_nvvp)):
    print("%s)" % num, _list_nvvp[i])
    num = num + 1
    if num <= len(_list_nvvp):
        continue
    else:
        break

pay_check_nvsx = 0
for i in _list_nvsx:
    pay_check_nvsx = i.luong_tong(i.pay_check(i.products_made), i.phu_cap(i.count_years(now.year, i.year_of_entry)))
    