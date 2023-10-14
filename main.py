import services
import random  
import tkinter
import copy

class Quiz:
    def __init__(self):
        self.points = 0
        self.init_window()

    def init_window(self):
        self.window = tkinter.Tk()
        self.window.title("Викторина:)")
        self.window.geometry('1024x768')

        self.lbl = tkinter.Label(self.window)
        self.lbl.pack()


        self.btn = tkinter.Button(self.window, text="Начать", command=self.start_quiz)
        self.btn.pack()
        self.window.mainloop()

    def checking(self, elem):
        print(elem)
        print(self.question[1])

        if self.question[1][elem] == True:
            self.answer_label.config(text='Правильно')
        else:
            self.answer_label.config(text='Неправильно')


    def start_quiz(self):
        self.question = services.take_question()

        self.btn.config(state=["disabled"])

        self.lbl.config(text=str(self.question[0]), font=("Arial Bold", 25))

        self.answer_label = tkinter.Label(self.window)
        self.answer_label.pack()

        for elem in list(self.question[1].keys())[:-1]:
            tkinter.Button(self.window, text=str(elem), command=lambda cur = elem: self.checking(cur)).pack()
    

quiz = Quiz()



# print(question[0], '\n')

# n = 0
# for elem in list(question[1].keys())[:-1]:
#     n += 1
#     print(n,':', elem)


# ans = str(input())

# try:
#     if question[1][ans] == True:
#         print('Правильно')
#     else:
#         print('Не правильно')
# except KeyError:
#     print('Неправильно')
# try:
#     if question[1][ans] == True:
#         print('Правильно')
#     else:
#         print('Не правильно')
# except KeyError:
#     print('Неправильно')
