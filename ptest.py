# виджет = wingow + gadget
# типы виджетов: контейнеры и контент
import tkinter
click = 0


window = tkinter.Tk()  # создаем экземпляр окна
window.geometry('960x440')  # задаем размеры окна
window.title('моя игра')  # задает заголовок\


label_1 = tkinter.Label(window, text='Текст метки')  # создаем экземпляр метки

def on_click(*event) -> None:
    print('кнопка нажата')
    print('счетчик: ', click)
    label_1['text'] = 'кнопка нажата'
    label_1['text'] = 'кнопка не нажата'


def cgange_window_color(*event) -> None:
    window['bg'] = 'salmon'


button = tkinter.Button(window, text='не нажимать', borderwidth=20, command=on_click)
label_1.bind('<Button-1>', on_click)

window['padx'] = 50
label_1['bg'] = 'red'
window['bg'] = 'green'
window.bind('<Key>', cgange_window_color)

label_1.pack(side='bottom', expand=True, )  # позиционируем виджет в контейнере


button.pack()
window.mainloop()  # всегда последний
