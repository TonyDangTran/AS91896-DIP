# importing tkinter for gui
from tkinter import *
import tkinter as tk
 
# creating window
window = tk.Tk()
window.config(bg="skyblue")
class quiz(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        master.title("The Quiz 2022")



        label = tk.Label(window, text="Quiz 2022", width=20, height=20)
        label.config(bg="red")
        label.pack()
        window.state('zoomed')
        window.title("Quiz 2022")

        photo = tk.PhotoImage(file="start_quiz.png")
        self.greet_button = Button(master, text="Start Quiz", width=40, height=40, command=self.greet, image=photo)
        self.greet_button.pack(side=RIGHT)
    
        
                        

        self.help_button = Button(master, text="Instructions", width=40, height=40, command=self.instructions)
        self.help_button.pack(side=LEFT)

        self.close_button = Button(master, text="Close Quiz", width=40, height=40, command=master.quit)
        self.close_button.pack(side=RIGHT)

        self.credits_button = Button(master, text="Credits", width=40, height = 40, command=self.credits)
        self.credits_button.pack(side=RIGHT)

    def greet(quiz):
        print("Welcome to the Quiz") 
    
    def instructions(quiz):
        print("How To Play:")

    def credits(quiz):
        print("Credits")

 
my_gui = quiz(window)
window.mainloop()