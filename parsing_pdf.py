import datetime
import json

import PyPDF2
from fuzzywuzzy import process

import config


class ParserPDF:
    def __init__(self):
        self.file_name = config.file_name

        self.weekday = datetime.date.weekday(datetime.datetime.today())
        # self.weekday = 0
        self.__get_food_list()

    def __get_food_list(self):
        import chardet

        with open("food_list.txt", "rb") as file:
            result = chardet.detect(file.read())
            file.seek(0)  # Reset the file pointer to the beginning of the file
            data = file.read().decode(result["encoding"])
            self.food_list = data.split("\r\n")
            # print(self.food_list)

        # with open("food_list.txt", "rb") as file:
        #     self.food_list = file.read().decode("UTF-8").split("\n")

    def __read(self, n: int = None):
        spec = ["завтрак", "обед", "ужин", "завт"]
        if n:
            lst = PyPDF2.PdfFileReader(self.file_name).getPage(n).extractText().lower().split()
        else:
            lst = PyPDF2.PdfFileReader(self.file_name).getPage(self.weekday).extractText().lower().split()
        lst = lst[lst.index("завтрак"):]
        ans = list()
        t_list = []
        for _ in lst:
            if _ in ["итого", "зав.", "производства", "зав.производства","зав. производства"]:
                continue
            _ = _.replace(",", "", 1)
            if _.replace("/", "").isdigit() and t_list:
                ans.append(process.extractOne(" ".join(t_list), self.food_list)[0])
                t_list.clear()
            if process.extractOne(_, spec)[1] > 65 and not t_list:
                ans.append(process.extractOne(_, self.food_list)[0])
            elif not (_.replace("/", "").isdigit()):
                t_list.append(_)
                if _ == "5д": #  костыль
                    t_list.clear()

        ans[0] = "завтрак I"
        ans[ans.index("завтрак")] = "завтрак II"
        # print(ans)
        return ans

    def __get_food_dict(self, n: int = None):
        lst = self.__read(n)
        dct = dict()
        spec = ["завтрак I", "завтрак II", "обед", "полдник", "ужин"]
        for i in lst:
            if i in spec:
                key = i
                dct[i] = list()
            else:
                dct[key].append(i)
        return dct

    # def get_file_name(self, name):
    #     self.file_name = name

    def __get_all_food_dict(self):
        dct = dict()
        for i in range(7):
            dct[i] = self.__get_food_dict(i)
        return dct

    def save_in_txt(self):
        with open(config.menu_file_name, "w") as file:
            file.write(json.dumps(self.__get_all_food_dict(), ensure_ascii=False))

# a = Parser()
# a.get_file_name("01.pdf")
# with open("food_today.txt", "w") as file:
#     file.write(json.dumps(a.get_all_food_dict(), ensure_ascii=False))
# pprint(a.get_food_dict())

# ParserPDF().save_in_txt()