import datetime


class Dialogs:
    greeting = """Привет! 🤖\nЯ Telegram-бот для столовой ЮФМЛ.
Я здесь, чтобы помочь вам получить информацию о меню на сегодня.
Вам не нужно беспокоиться о загрузке PDF-файла 📎 , так как у меня есть последняя и обновленная информация о меню.
    
если что-то непонятно, используйте /help"""
    support = """Я Telegram-бот для столовой ЮФМЛ.
Всё что я делаю, это  вывожу данные c сайта в удобном формате, Вам нужно всего лишь нажимать на кнопочки внизу экрана.

Что делать если конопки не появились?
- введите еще раз /start

По поводу вопросов и предложений обращаться @bsaveliy
"""

    @staticmethod
    def get_food_list(food_list, nourishment: str, date=None) -> str:
        if not date:
            date = datetime.datetime.today().date()
        text = "\n".join([f"{str(n + 1)}) {food}" for n, food in enumerate(food_list)])
        nourishment = nourishment.lower()
        if nourishment == "ii завтрак":
            nourishment = "II завтрак"
        food_list = f"Меню на {nourishment} {date.strftime(date.strftime('%d.%m.%Y'))}\n{text}\n\nПриятного аппетита!"
        return food_list


# print(Dialogs.get_food_list(["каша рисовая на молоке с маслом", "бутерброд с маслом и сыром", "какао с молоком/чай", "хлеб пшеничный в/с"], "Завтрак", datetime.date(2023, 1, 30)))

