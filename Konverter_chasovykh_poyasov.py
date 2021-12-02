tz = ("(UTC-06:00) о.Пасхи", "(UTC-06:00) Центральная Америка", "(UTC-03:00) Бразилия",
      "(UTC-03:00) Гренландия", "(UTC-03:00) Сальвадор", "(UTC-00:00) Лондон",
      "(UTC-00:00) Рейкьявик", "(UTC+01:00) Амстердам", "(UTC+01:00) Берлин", "(UTC+01:00) Вена", "(UTC+01:00) Рим",
      "(UTC+01:00) Стокгольм", "(UTC+01:00) Белград", "(UTC+01:00) Будапешт", "(UTC+01:00) Прага",
      "(UTC+01:00) Брюссель", "(UTC+01:00) Мадрид", "(UTC+01:00) Париж", "(UTC+01:00) Варшава", "(UTC+02:00) Афины",
      "(UTC+02:00) Вильнюс", "(UTC+02:00) Киев", "(UTC+02:00) Рига", "(UTC+02:00) Таллин", "(UTC+02:00) Хельсинки",
      "(UTC+02:00) Иерусалим", "(UTC+02:00) Каир", "(UTC+02:00) Калиненград", "(UTC+03:00) Багдад",
      "(UTC+03:00) Волгоград", "(UTC+03:00) Минск", "(UTC+03:00) Москва", "(UTC+03:00) Санкт-Петербург",
      "(UTC+03:00) Стамбул", "(UTC+04:00) Астрахань", "(UTC+04:00) Ульяновск", "(UTC+04:00) Баку", "(UTC+04:00) Ереван",
      "(UTC+04:00) Ижевск", "(UTC+04:00) Саара", "(UTC+04:00) Саратов", "(UTC+04:00) Тбилиси", "(UTC+05:00) Ташкент",
      "(UTC+05:00) Екатеринбург", "(UTC+06:00) Астана", "(UTC+06:00) Омск", "(UTC+07:00) Барнаул",
      "(UTC+07:00) Красноярск", "(UTC+07:00) Новосибирск", "(UTC+07:00) Томск", "(UTC+08:00) Гонконг",
      "(UTC+08:00) Пекин", "(UTC+08:00) Иркутск", "(UTC+08:00) Сингапур", "(UTC+08:00) Улан-Батор", "(UTC+09:00) Токио",
      "(UTC+09:00) Пхеньян", "(UTC+09:00) Сеул", "(UTC+09:00) Чита", "(UTC+09:00) Якутск", "(UTC+10:00) Владивосток",
      "(UTC+10:00) Сидней", "(UTC+11:00) Магадан", "(UTC+11:00) Сахалин", "(UTC+12:00) Анадырь",
      "(UTC+12:00) Петропавловск-Камчатский")
entry = ""

def start():
    btn_start.pack_forget()
    lbl_now_strftime = Label(window, text="Текущая дата и время: " + current_time + ".")
    lbl_now_strftime.pack()
    frm_entry.pack()

def check():
    ctz = combo_tz.get()
    if ctz == "":
        messagebox.showinfo('Fatal ERROR', "Вы не выбрали часовой пояс!")
    else:
        entry()

def entry():
    frm_entry.pack_forget()
    ctz = combo_tz.get()
    if ctz[4:7] == "-06":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('America/New_York')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "-03":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Brazil')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "-00":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/London')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+01":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Amsterdam')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+02":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Vilnius')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+03":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+04":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Volgograd')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+05":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Ekaterinburg')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+06":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Omsk')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+07":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Novosibirsk')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+08":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Asia/Beijing')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+09":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+10":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Vladivostok')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+11":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Asia/Sakhalin')).strftime("%d.%m.%Y %H:%M"))
    elif ctz[4:7] == "+12":
        entry = ctz + ": " + str(datetime.now(pytz.timezone('Europe/Anadyr')).strftime("%d.%m.%Y %H:%M"))
    else:
        entry = "Произошла какая-то ошибка."
    lbl_entry = Label(master=window, text=entry)
    lbl_entry.pack()

    try:
        fail = open('История конертера часовых поясов.txt', 'w')
        try:
            fail.write("\n" + now.strftime("%d.%m.%Y %H:%M") + " : " + entry)
        except Exception as e:
            print(e)
        finally:
            fail.close()
    except Exception as ex:
        print(ex)

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import *
import pytz

now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M")

window = Tk()
window.title("Конвертер часовых поясов")
window.geometry('400x250')
btn_start = Button(window, text = 'Начать', command=start)
btn_start.pack(expand=True, fill=BOTH)

frm_entry = Frame(master=window)
lbl_tz = Label(master=frm_entry, text="Выберите часовой пояс:")
lbl_tz.grid(row=0, column=0)
combo_tz = Combobox(master=frm_entry, values=tz)
combo_tz.grid(row=0, column=1)
btn_entry = Button(master=frm_entry, text = 'Начать', command=check)
btn_entry.grid(row=1, column=0, columnspan=2)

window.mainloop()