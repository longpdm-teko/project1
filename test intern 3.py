class BangDiem:
    def __init__(self, toan, ly, hoa):
        self.__toan = toan
        self.__ly = ly
        self.__hoa = hoa

    def get_diem_toan(self):
        return self.__toan

    def get_diem_ly(self):
        return self.__ly

    def get_diem_hoa(self):
        return self.__hoa

    def get_diem_tb(self):
        return (self.get_diem_toan() + self.get_diem_ly() + self.get_diem_hoa()) / 3


class SinhVien:
    def __init__(self, id_num, name, age, bang_diem):
        self.id_num = id_num
        self.name = name
        self.age = age
        self.bang_diem = bang_diem

    def get_age(self):
        return self.age

    def __get_id_num(self):
        return self.id_num

    def trung_binh(self):
        return self.bang_diem.get_diem_tb()

    def __repr__(self):
        return "Ma so: {0}, " \
               "Ho va Ten: {1}, " \
               "Tuoi: {2}, " \
               "Toan: {3} diem, " \
               "Ly: {4} diem, " \
               "Hoa: {5} diem, " \
               "Diem trung binh: {6}/////".format(self.id_num, self.name, self.age, self.bang_diem.get_diem_toan(),
                                                  self.bang_diem.get_diem_ly(), self.bang_diem.get_diem_hoa(),
                                                  self.trung_binh())


class LopHoc:
    def __init__(self, name, list_sinh_vien=[]):
        self.name = name
        self.list_sinh_vien = list_sinh_vien

    def add_sinh_vien(self, item):
        if not self.list_sinh_vien:
            self.list_sinh_vien = []
        self.list_sinh_vien.append(item)

    def get_avg_age(self):
        total = 0
        for item in self.list_sinh_vien:
            total += item.get_age()  # => total = total + item
        total /= len(self.list_sinh_vien)  # => total = total / item
        return total

    def get_hs_gioi(self):
        hsg = []
        for item in self.list_sinh_vien:
            if item.trung_binh() >= 8.0:
                hsg.append(item)
        return hsg

    def __repr__(self):
        return "Ten lop: {0}, " \
               "Danh sach lop: {1}, " \
               "Do tuoi trung binh: {2}, " \
               "Danh sach hoc sinh gioi: {3}".format(self.name, self.list_sinh_vien, self.get_avg_age(),
                                                     self.get_hs_gioi())


bang_diem1 = BangDiem(6, 7, 8)  # 7.0
bang_diem2 = BangDiem(7, 9, 8)  # 8.0
bang_diem3 = BangDiem(5, 9, 5)  # 6.333
bang_diem4 = BangDiem(8, 7, 10)  # 8.3
bang_diem5 = BangDiem(7, 6, 10)  # 7.67

sv1 = SinhVien("HS01", "Nguyen Van A", 16, bang_diem1)
sv2 = SinhVien("HS02", "Nguyen Van B", 18, bang_diem2)
sv3 = SinhVien("HS03", "Nguyen Van C", 15, bang_diem3)
sv4 = SinhVien("HS04", "Nguyen Van D", 29, bang_diem4)


# _list = [
#     LopHoc("12A", [SinhVien("HS01", "Nguyen Van A", 16, 8, 6, 7), SinhVien("HS02", "Nguyen Van B", 17, 9, 9, 10),
#                    SinhVien("HS03", "Nguyen Van C", 16, 5, 6, 2), SinhVien("HS04", "Nguyen Van D", 18, 4, 9, 6),
#                    SinhVien("HS05", "Nguyen Van E", 17, 8, 10, 10), SinhVien("HS06", "Nguyen Van F", 18, 9, 7, 10),
#                    SinhVien("HS07", "Nguyen Van G", 17, 5, 10, 8), SinhVien("HS08", "Nguyen Van H", 17, 10, 9, 10)])
# ]

lop_hoc = LopHoc("12A8", [sv1, sv2, sv3, sv4])

for hsg in lop_hoc.get_hs_gioi():
    print(hsg)

print(lop_hoc.get_avg_age())