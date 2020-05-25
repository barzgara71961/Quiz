from tkinter import *
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
                                  bg="#51BBFE",command=self.math)
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
                                  bg="#51BBFE", command=self.help,)
        self.help_button.grid(row=1)

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure(text="You have to pick a top and you will be getting tested on in")

    def math(self):
        math_L1 = Math(self)
        math_L1.math_text.configure(text="Fill the boxes")

class Math:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable button
        partner.math_button.config(state=DISABLED)

        # Set up math game one
        self.math_box = Toplevel()

        # Set up GUI Frame
        self.math_frame = Frame(self.math_box, width=300, bg=background_color)
        self.math_frame.grid()
        # Set up math Instruction heading (row 0)
        self.how_heading = Label(self.math_frame,
                                 text="Math",
                                 font="arial 20 bold",bg=background_color)
        self.how_heading.grid(row=0)
        # Math text (label, row 1)
        self.math_text = Label(self.math_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.math_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.math_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_math, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_math(self, partner):
        # Put help button back to normal
        partner.math_button.config(state=NORMAL)
        self.math_box.destroy()

class Help:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_color)
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help / Instruction",
                                 font="arial 20 bold",bg=background_color)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="i have no idea where this is going to be",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.help_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
