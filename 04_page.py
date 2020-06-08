from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "#8FF7A7"

        self.quiz_frame = Frame(width=500, height=500,bg=background_color)
        self.quiz_frame.grid()

        self.heading_frame = Frame(self.quiz_frame,bg=background_color)
        self.heading_frame.grid(row=0)

        # Quiz (row 0)
        self.Quiz_label = Label(self.heading_frame,text="MATH QUIZ",
                                font=("arial 20 bold"),
                                fg="#757761",bg=background_color)
        self.Quiz_label.grid(row=0)

        # Quiz (row 1)
        self.Quiz_instruction_label = Label(self.heading_frame,text="Pick a topic you want to have a quiz on ",
                                font=("arial 10 bold"),
                                fg="#757761",bg=background_color)
        self.Quiz_instruction_label.grid(row=1)

        self.choicing_frame = Frame(self.quiz_frame,bg=background_color)
        self.choicing_frame.grid(row=1)

        self.cho_num_label = Label(self.choicing_frame,text="How many question would you like",
                                font=("arial 10 bold"),
                                fg="#757761",bg=background_color)
        self.cho_num_label.grid(row=1)

        self.cho_num_entry = Entry(self.choicing_frame,
                                   font=("arial 10 bold"))
        self.cho_num_entry.grid(row=2)

        self.cho_btn__frame = Frame(self.quiz_frame, width=300, bg=background_color)
        self.cho_btn__frame.grid(row=2)

        self.addition_btn = Button(self.cho_btn__frame,text="Addation",bg="#51BBFE",
                                  font="arial 14 bold",command=self.addation)
        self.addition_btn.grid(row=1)

        self.division_btn = Button(self.cho_btn__frame,text="Division ",bg="#51BBFE",
                                  font="arial 14 bold",command=self.division)
        self.division_btn.grid(row=2)

        self.multiplication_btn = Button(self.cho_btn__frame,text="multiplication ",bg="#51BBFE",
                                  font="arial 14 bold",command=self.multiplication)
        self.multiplication_btn.grid(row=3)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=3)

        # Help Button (row 2)
        self.help_button = Button(self.help_frame,
                                  text="Help", font="arial 14 bold", fg="black",
                                  bg="#51BBFE", command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure(text="You have to pick a top and you will be getting tested on in")

    def multiplication(self):
        get_multiplication = Multiplication(self)
        get_multiplication.multiplication_text.configure(text="Fill in the boxes")

    def addation(self):
        get_addation = Addation(self)
        get_addation.addation_text.configure(text="Fill in the boxes")
    def division(self):
        get_division = Division(self)
        get_division.division_text.configure(text="Fill in the boxes")
class Division:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.division_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.division_box = Toplevel()

        # Set up GUI Frame
        self.division_frame = Frame(self.division_box, width=300, bg=background_color)
        self.division_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.division_frame,
                                 text="Division",
                                 font="arial 20 bold",bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.division_text = Label(self.division_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.division_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.division_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_division, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_division(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.division_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.division_box.destroy()
class Addation:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.division_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.addation_box = Toplevel()

        # Set up GUI Frame
        self.addation_frame = Frame(self.addation_box, width=300, bg=background_color)
        self.addation_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.addation_frame,
                                 text="Addation",
                                 font="arial 20 bold",bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.addation_text = Label(self.addation_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.addation_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.addation_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_addation, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_addation(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.division_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.addation_box.destroy()
class Multiplication:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.division_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.Multiplication_box = Toplevel()

        # Set up GUI Frame
        self.Multiplication_frame = Frame(self.Multiplication_box, width=300, bg=background_color)
        self.Multiplication_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.Multiplication_frame,
                                 text="Multiplication",
                                 font="arial 20 bold",bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.multiplication_text = Label(self.Multiplication_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.multiplication_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.Multiplication_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_multiplication, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_multiplication(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.division_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.Multiplication_box.destroy()
class Help:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable help button
        partner.addition_btn.config(state=DISABLED)
        partner.division_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
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
        partner.addition_btn.config(state=NORMAL)
        partner.division_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
