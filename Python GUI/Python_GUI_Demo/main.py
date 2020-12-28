from tkinter import *

root = Tk()

root.title('Simple Calculator')
root.geometry('400x500')

button = Button(root, text='My Button', width=10, height=1, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')

button.pack()

root.mainloop()