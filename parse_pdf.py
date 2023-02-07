import PyPDF2
from fuzzywuzzy import process
import config


# def read(name, pg):
#     lst = PyPDF2.PdfFileReader(name).getPage(pg).extractText().lower().split()
#     lst = lst[lst.index("завтрак"):]
#
#     ans = list()
#
#     t_list = []
#     spec = ["завтрак", "обед", "ужин"]
#     for _ in lst:
#         _ = _.replace(",", "", 1)
#         if _.replace("/", "").isdigit() and t_list:
#             ans.append(" ".join(t_list))
#             t_list.clear()
#         if _ in spec:
#             ans.append(_)
#         elif _.count("i") == len(_):
#             ans[-1] = " ".join([ans[-1], _.upper()])
#         elif not (_.replace("/", "").isdigit()):
#             t_list.append(_)
#     return ans
#
#
# lst = []
#
#
# for i in range(7):
#     a = (read("03.pdf", i))
#     # with open("result.txt", "r") as file_read:
#     #     print(file_read.read().split("\n"))
#     with open("result.txt", "a+") as file_append:
#         for j in a:
#         # file.write(str(j) + "\n")
#             with open("result.txt", "r") as file_read:
#                 print(str(j) not in file_read.read().split("\n"), str(j), file_read.read().split("\n"))
#                 # if str(j) not in file_read.read().split("\n"):
#                 if str(j) not in lst:
#                     file_append.write(str(j) + "\n")
#                     lst.append(str(j))
#     # for j in a:
#
# print(lst)


class Pdf_Parser:
    def __init__(self):
        self.spec = ["завтрак", "обед", "ужин"]
        self.file_name = config.file_name
        self.all_food = self.__get_food_list()

    def __read(self, pg):
        lst = PyPDF2.PdfFileReader(self.file_name).getPage(pg).extractText().lower().split()
        lst = lst[lst.index("завтрак"):]

        ans = list()
        t_list = list()

        for elem in lst:
            elem: str = elem.replace(",", "", 1)
            if elem.replace("/", "").isdigit() and t_list:
                ans.append(" ".join(t_list))
                t_list.clear()
            if elem in self.spec:
                ans.append(elem)
            elif elem.count("i") == len(elem):
                ans[-1] = " ".join([ans[-1], elem.upper()])
            elif not(elem.replace("/", "").isdigit()):
                t_list.append(elem)
        return ans

    @staticmethod
    def __get_food_list():
        with open(config.file_all_food_list, "r") as file:
            return [elem.strip() for elem in file]

    def __levenstein_distance(self, food):
        return process.extractOne(food, self.all_food)[0]

    def get_file_menu(self):
        for i in range(7):  # 7 days in week
            data = (self.__read(i))
            with open(config.file_temp, "a+") as file_append:
                for elem in data:
                    file_append.write(self.__levenstein_distance(elem) + "\n")
        return True


# print(Pdf_Parser().levenstein_distance("итого"))