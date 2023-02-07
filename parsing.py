import asyncio
import datetime
import os
from datetime import date
# from pprint import pprint
import json

import config
import aiohttp
import aiofiles
import pickle
import calendar


class Parser:
    def __init__(self):
        self.file = None
        self.file_name = None
        self.url = "https://ugrafmsh.ru/wp-content/uploads/2023/01/menyu-23-01-2023-krugl.pdf"
        self.url_default = "https://ugrafmsh.ru/wp-content/uploads/{year}/{month}/menyu-{date}-krugl.pdf"
        #year, month, date
        self.weekday = 0  # 0 - понедельник

    def set_url(self, url: str):
        self.url = url
        print(url)

    def set_date(self, date=date.today()):
        print(date.day - date.weekday())
        print(calendar.monthcalendar(date.year, date.month))
        # pprint(calendar.Calendar().yeardayscalendar(2023))

    def get_date(self, d=None):
        if not d:
            d = date.today()
        date_string = d.strftime("%d-%m-%Y")
        if d.weekday() == 0:
            self.set_url(self.url_default.format(year=str(d.strftime("%Y")), month=str(d.strftime("%m")), date=date_string))

    async def get_file(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(config.file_name, mode='wb')
                    text = await resp.read()
                    if self.is_pdf(text[1:4].decode("utf-8")):
                        await f.write(text)
                        await f.close()
                        return True
        return False

    def is_pdf(self, suffix):
        if suffix == "PDF":
            return True
        return False

    @staticmethod
    def get_menu(nourishment):
        with open(config.menu_file_name, "r") as file:
            if nourishment == "завтрак":
                nourishment = "завтрак I"
            return json.loads(file.read())[str(date.today().weekday())][nourishment]

    def is_actual_menu(self):
        now = date.today()
        print(now)


if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Parser.get_menu()