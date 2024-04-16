import tkinter


question = [
    {
        'Вопрос': 'Какой оператор умножает числа в Python?'
        'Ответы': ['', 'x', '*', '**']
        'Правильный индекс': 2
        },{
        'Вопрос': 'Какой из этих типов изменяемый?'
        'Ответы': ['list', 'str', 'tuple', 'int']
        'Правильный индекс': 0}
]
            


class App:
    '''
    Приложение
    TODO: окно во весь экран
    '''
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        screen_width = self.window.winfo_screenwidth
        scrin_height = self.window.winfo_screenheight
        self.window.geometry(f'{screen_width}x{scrin_height}')
        self.window.mainloop()

        self.question_text = tkinter.Label(self.window)
        self.question_answer_1 = tkinter.Label(self.window)
        self.question_answer_2 = tkinter.Label(self.window)
        self.question_answer_3 = tkinter.Label(self.window)
        self.question_answer_4 = tkinter.Label(self.window)
        self.answer_button

        self.question_text.pack()
        self.question_answer_1.pack()
        self.question_answer_2.pack()
        self.question_answer_3.pack()
        self.question_answer_4.pack()

        for question in question:
            self.question_text['text'] = question
            self.question_answer_1['text'] = '1.' + question['ответы'][0]
            self.question_answer_1['text'] = '2.' + question['ответы'][1]
            self.question_answer_1['text'] = '3.' + question['ответы'][2]
            self.question_answer_1['text'] = '4.' + question['ответы'][3]

        def on_click(self) -> None:
            print('1')
App()
