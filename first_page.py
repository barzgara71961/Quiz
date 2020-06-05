from tkinter import *
import csv
from functools import partial   # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "#8FF7A7"

        # Converter Main Screen GUT...
        self.quiz_frame = Frame(width=500, height=500,bg=background_color)
        self.quiz_frame.grid()

        self.heading_frame = Frame(self.quiz_frame,bg=background_color)
        self.heading_frame.grid(row=0)

        # Quiz (row 0)
        self.Quiz_label = Label(self.heading_frame,text="QUIZ",
                                font=("arial 20 bold"),
                                fg="#757761",bg=background_color)
        self.Quiz_label.grid(row=0)

        # Quiz (row 1)
        self.Quiz_instruction_label = Label(self.heading_frame,text="Pick a topic you want to have a quiz on ",
                                font=("arial 10 bold"),
                                fg="#757761",bg=background_color)
        self.Quiz_instruction_label.grid(row=1)

        self.math_frame = Frame(self.quiz_frame,bg=background_color)
        self.math_frame.grid(row=1)

        # math_button button (row 0 column 1 )
        self.math_button = Button(self.math_frame,
                                  text="Math level 1", font="arial 20 bold", fg="#757761",
                                  bg="#51BBFE")
        self.math_button.grid(row=0)

        self.math_label = Label(self.math_frame,
                                text="Math level 1 will give will give you a quiz\n"
                                     "about addtion and subcration",
                                font="arial 10 bold", fg="#757761",bg="#F7FE72")
        self.math_label.grid(row=0,column=1)

        self.math_two_button = Button(self.math_frame,
                                  text="Math level 2", font="arial 20 bold", fg="#757761",
                                  bg="#51BBFE")
        self.math_two_button.grid(row=2)

        self.math_label = Label(self.math_frame,
                                text="Math level 2 will give will give you a quiz\n"
                                     "about your time tables and division",
                                font="arial 10 bold", fg="#757761",bg="#F7FE72")
        self.math_label.grid(row=2,column=1)

        self.math_three_button = Button(self.math_frame,
                                  text="Math level 3", font="arial 20 bold", fg="#757761",
                                  bg="#51BBFE")
        self.math_three_button.grid(row=3)

        self.math_label = Label(self.math_frame,
                                text="Math level 3 will give will give you a quiz\n"
                                     "about i dont what will go here ",
                                font="arial 10 bold", fg="#757761",bg="#F7FE72")
        self.math_label.grid(row=3,column=1)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=2)

        # Help Button (row 2)
        self.help_button = Button(self.help_frame,
                                  text="Help", font="arial 20 bold", fg="#757761",
                                  bg="#51BBFE")
        self.help_button.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
