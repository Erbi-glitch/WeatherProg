import pyowm
import time
from time import sleep
from tkinter import *
import requests
from pyowm import owm
import csv

master = Tk()

master.title('Сбор данных погоды')

master.geometry('400x450')


def on_clicked():
    # global sto  # (выход из приложения)
    # sto = False

    seconds_left = int(time_entry.get())
    with open(f'{exe_entry.get()}.csv', mode='w', errors='replace', encoding="cp1251") as csvfile:
        csvfile.write(
            'Город - ' + town_entry.get() + '\n' + 'Дата' + ';' + 'Время' + ';' + 'Погода' + ';' + "Температура (°C)"
            + ';' + "Ощущаестся как (°C)" + ';' + "Скорость ветра (М/С)" + ';' + "На солько % облака (%)" + ';'
            + "Давление (мм.рт.ст)" + ';' + "Влажность (%)" + ';' + '\n')
        csvfile.close()
    while True:
        # if sto:  # (выход из приложения)
        #     break
        key = '5d98c4d8f29fc19ec18313b219fdb489'

        url = 'http://api.openweathermap.org/data/2.5/weather'
        # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
        params = {'APPID': key, 'q': town_entry.get(), 'units': 'metric'}
        # Отправляем запрос по определенному URL
        result = requests.get(url, params=params)
        # Получаем JSON ответ по этому URL
        weather = result.json()
        # print(weather)
        # Полученные данные добавляем в текстовую надпись для отображения пользователю
        obs = [i.get('description') for i in weather["weather"]]
        # print(
        #     f'{"Погода"}: {obs[0]}')
        # print(
        #     f'{"Температура"}: {str(weather["main"]["temp"]) + "°C"}')
        # print(
        #     f'{"Ощущаестся как"}: {str(weather["main"]["feels_like"]) + "°C"}')
        # print(
        #     f'{"Скорость ветра"}: {str(weather["wind"]["speed"]) + " М/С"}')
        # print(
        #     f'{"На солько % облака"}: {str(weather["clouds"]["all"]) + "%"}')
        # print(
        #     f'{"Давление"}: {str(weather["main"]["pressure"]) + "мм.рт.ст"}')
        # print(
        #     f'{"Влажность"}: {str(weather["main"]["humidity"]) + "%"}')

        CurrentTime = time.strftime("%d/%m/%Y", time.localtime())
        CurrentData = time.strftime("%H:%M:%S", time.localtime())
        print(CurrentTime)
        print(CurrentData)

        f = open(f'{exe_entry.get()}.csv', mode='a', encoding="cp1251")
        f.write(str(CurrentData) + ';' + str(CurrentTime) + ';' + str(obs[0]) + ';' +
                str(weather["main"]["temp"]) + "°C" + ';' + str(weather["main"]["feels_like"]) + ';' + str(
            str(weather["wind"]["speed"])) + ';' + str(weather["clouds"]["all"]) + ';' + str(
            weather["main"]["pressure"]) + ';' + str(weather["main"]["humidity"]) + ';' + '\n')
        f.close()
        sleep(seconds_left)


# создание дизайна приложения


master.resizable(width=False, height=False)

bg = PhotoImage(file="background.png")

canvas = Canvas(master, height=450, width=400)

canvas.create_image(0, 0, image=bg, anchor="nw")

frame_top = Frame(master, bg='black', bd=5)
frame_top.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

frame_center = Frame(master, bg='black', bd=5)
frame_center.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.2)

frame_center2 = Frame(master, bg='black', bd=5)
frame_center2.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.2)

frame_bottom = Frame(master, bg='black', bd=5)
frame_bottom.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.1)
# frame_bottom.bind('<Enter>', on_clicked())

town_entry = Entry(frame_top, justify=LEFT, selectbackground='gray')
town_entry.place(relx=0, rely=0.28, relwidth=1, relheight=0.5)

time_entry = Entry(frame_center, justify=LEFT, selectbackground='gray')
time_entry.place(relx=0, rely=0.28, relwidth=1, relheight=0.5)

exe_entry = Entry(frame_center2, justify=LEFT, selectbackground='gray')
exe_entry.place(relx=0, rely=0.28, relwidth=1, relheight=0.5)

label_top = Label(frame_top, text="Введите название города:", bg='black', fg='white', padx=0.25, pady=0.25)

label_center = Label(frame_center, text="Введите периодичность опроса (мин):", bg='black', fg='white',
                     padx=0.25,
                     pady=0.25)

label_center2 = Label(frame_center2, text="Имя файла данных: (CSV)", bg='black', fg='white', padx=0.25,
                      pady=0.25)

btn = Button(frame_bottom, text='СТАРТ', command=on_clicked, width=12, height=5).pack(side=LEFT)
btn2 = Button(frame_bottom, text='СТОП', width=12, height=5).pack(side=RIGHT)

label_top.pack()
label_center.pack()
label_center2.pack()
canvas.pack()
master.mainloop()
