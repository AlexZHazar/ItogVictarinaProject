import services
import tkinter 

points = 0
def clicked():  
    lbl.configure(text = str(question[0]), font=("Arial Bold", 25))



window = tkinter.Tk()
window.title("Викторина:)")
window.geometry('1080x500')

question = services.take_question()

lbl = tkinter.Label(window)
lbl.pack()


btn = tkinter.Button(window, text="Начать", command=clicked)
btn.pack()
window.mainloop()


print(question[0], '\n')

n = 0
for elem in list(question[1].keys())[:-1]:
    n += 1
    print(n,':', elem)


ans = str(input())

try:
    if question[1][ans] == True:
        print('Правильно')
    else:
        print('Не правильно')
except KeyError:
    print('Неправильно')
