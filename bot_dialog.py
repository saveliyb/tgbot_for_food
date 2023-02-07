import datetime


class Dialogs:
    greeting = "Привет, бла бла бла"
    support = "{описание функционала и куда тыкать}"

    @staticmethod
    def get_food_list(food_list, nourishment: str, date=datetime.datetime.today().date()) -> str:
        text = "\n".join([f"{str(n + 1)}) {food}" for n, food in enumerate(food_list)])
        food_list = f"Меню на {nourishment.lower()} {date.strftime(date.strftime('%d.%m.%Y'))}\n{text}\n\nПриятного аппетита!"
        return food_list


# print(Dialogs.get_food_list(["каша рисовая на молоке с маслом", "бутерброд с маслом и сыром", "какао с молоком/чай", "хлеб пшеничный в/с"], "Завтрак", datetime.date(2023, 1, 30)))

