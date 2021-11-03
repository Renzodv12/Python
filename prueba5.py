import os
from time import sleep
from random import randrange
import sqlite3
from shutil import copyfile
from pathlib import Path
import re
import glob

def delay():
    n_horas = randrange(1, 4)
    print("Durmiento {} horas".format(n_horas))
    sleep(n_horas)


def history(path):
    url = None
    while not url:
        try:
            history_path = path + "AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC limit 10")
            url = cursor.fetchall()
            connection.close()
            print(url)
            return url
        except sqlite3.OperationalError:
            print("La base de datos is open esperando 3 segundos")
            sleep(3)


def file(path):
    txt = open(path + "Desktop\\" + "PARA TI.TXT", "w", encoding='utf-8')
    txt.write("Hola soy yo : \n")
    return txt


def check_history(url, txt):
    visit_pagine = []
    for item in url[:10]:
        visit_pagine.append(item[0])

    txt.write("Hi visitaste {} ? \n".format(", \n".join(visit_pagine)))


def main():
    delay()
    path = "c:\\Users\\" + os.getlogin() + "\\"
    url = history(path)
    print(url[9])
    txt = file(path)
    check_history(url, txt)


if __name__ == "__main__":
    main()
