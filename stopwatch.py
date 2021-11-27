from tkinter import *
from datetime import datetime

temp = 0
after_id = ''

# функція таймеру:
def tick():
    global temp, after_id
    after_id = root.after(100, tick)  # оновлення функції кожну секунду(1000мс)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')  # форматування вигляду хв.сек.
    label1.configure(text=str(f_temp))  # вивід тексту з f_temp на label1 (наше табло)
    temp += 1

# функція старту:
def start_tick():
    btnstart.pack_forget()  # після натискання на кнопку START вона зникає, натомість..
    btnstop.pack()  # ..з'являється кнопка STOP
    tick()  # функція продовжує відлік

# функція зупинки:
def stop_tick():
    btnstop.pack_forget()  # після натискання на кнопку STOP вона зникає, натомість..
    btncontinue.pack()  # ..з'являється кнопка CONTINUE..
    btnreset.pack()  # ..і з'являється кнопка RESET
    root.after_cancel(after_id)  # секундомір зупиняється

def continue_tick():
    btncontinue.pack_forget()  # зникає CONTINUE
    btnreset.pack_forget()  # зникає RESET
    btnstop.pack()  # з'являється START
    tick()  # функція продовжує відлік

def reset_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btncontinue.pack_forget()
    btnreset.pack_forget()
    btnstart.pack()

root = Tk()  # створення головного вікна
root.title('Stopwatch')  # заголовок вікна
root.resizable(width=False, height=False)  # заборона зміни розміру головного вікна
root.geometry('300x230')  # розмір вікна
root.iconbitmap('stopwatch_icon.ico')
#root.config(bg='black')  # колір фону
#root['bg'] = 'black'  # колір фону(варіант 2)

label1 = Label(root, width=10, font=('UniDreamLED', 60), text='00:00')
label1.pack()

# кнопки(розмір кнопки залежить від розміру шрифту):
btnstart = Button(root, text='START', font=('Arial', 20), activebackground='red', width=15, command=start_tick)
btnstop = Button(root, text='STOP', font=('Arial', 20), width=15, command=stop_tick)
btnreset = Button(root, text='RESET', font=('Arial', 20), width=15, command=reset_tick)
btncontinue = Button(root, text='CONTINUE', font=('Arial', 20), width=15, command=continue_tick)
btnstart.pack()  # вивід кнопок
# activebackground='red' - колір кнопки при натисканні
# activeforeground='white' - колір кнопки після натискання
# fg='green'- колір тексту кнопки

root.mainloop()  # запуск