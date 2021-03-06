from tkinter import *
from functools import partial   # To prevent unwanted windows

import random

class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "#8FF7A7"
        btn_color = "#51BBFE"
        font_color = "black"

        self.quiz_frame = Frame(width=500, height=500,bg=background_color)
        self.quiz_frame.grid()

        self.starting_questoin = IntVar()
        self.starting_questoin.set(0)

        self.heading_frame = Frame(self.quiz_frame,bg=background_color)
        self.heading_frame.grid(row=0)

        # Quiz (row 0)
        self.Quiz_label = Label(self.heading_frame,text="MATH QUIZ",
                                font=("arial 20 bold"),
                                fg=font_color,bg=background_color)
        self.Quiz_label.grid(row=0)

        # Quiz (row 1)
        self.choicing_frame = Frame(self.quiz_frame,bg=background_color)
        self.choicing_frame.grid(row=1)

        self.amount_error_label = Label(self.choicing_frame, font="arial 10 italic",
                                        text="", bg=background_color)
        self.amount_error_label.grid(row=0)

        self.cho_num_label = Label(self.choicing_frame,text="How many question would you like",
                                   font=("arial 10 bold"),
                                   fg=font_color,bg=background_color)
        self.cho_num_label.grid(row=1)

        self.cho_num_entry = Entry(self.choicing_frame,
                                   font="arial 10 bold", width=5)
        self.cho_num_entry.grid(row=1,column=1)

        self.low_num_label = Label(self.choicing_frame,text="low number amout",
                                   font="arial 10 bold",
                                   fg=font_color,bg=background_color)
        self.low_num_label.grid(row=2)

        self.low_num_entry = Entry(self.choicing_frame,
                                   font="arial 10 bold", width=5)
        self.low_num_entry.grid(row=2,column=1)

        self.high_num_label = Label(self.choicing_frame,text="high number amout",
                                   font="arial 10 bold",
                                   fg=font_color,bg=background_color)
        self.high_num_label.grid(row=3)

        self.high_num_entry = Entry(self.choicing_frame,
                                   font="arial 10 bold", width=5)
        self.high_num_entry.grid(row=3,column=1)

        self.question_amount_btn = Button(self.choicing_frame,text="Enter",bg=btn_color,
                                         font="arial 14 bold",command=self.check_question)
        self.question_amount_btn.grid(row=4,)

        self.cho_btn__frame = Frame(self.quiz_frame, width=300, bg=background_color)
        self.cho_btn__frame.grid(row=2)

        self.addition_btn = Button(self.cho_btn__frame,text="Addition", font="arial 20 bold", fg=font_color,
                                   bg=btn_color,padx=35,command=self.addition)
        self.addition_btn.grid(row=1)

        self.addition_label = Label(self.cho_btn__frame,
                                text="this is a place holder",
                                font="arial 10 bold", fg=font_color,bg="#F7FE72")
        self.addition_label.grid(row=1,column=1)

        self.division_btn = Button(self.cho_btn__frame,
                                   text="Division", font="arial 20 bold", fg=font_color,
                                   bg=btn_color,padx=36,command=self.division)
        self.division_btn.grid(row=2)

        self.division_label = Label(self.cho_btn__frame,
                                text="this is a place holder",
                                font="arial 10 bold", fg=font_color,bg="#F7FE72")
        self.division_label.grid(row=2,column=1)

        self.multiplication_btn = Button(self.cho_btn__frame,
                                  text="Multiplication", font="arial 20 bold", fg=font_color,
                                  bg=btn_color,command=self.multiplication)
        self.multiplication_btn.grid(row=3)

        self.multiplication = Label(self.cho_btn__frame,
                                text="this is a place holder ",
                                font="arial 10 bold", fg=font_color,bg="#F7FE72")
        self.multiplication.grid(row=3,column=1)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=3)

        self.addition_btn.config(state=DISABLED)
        self.division_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        # Help Button (row 2)
        self.help_button = Button(self.help_frame,
                                  text="Help", font="arial 14 bold", fg="black",
                                  bg="green", command=self.help)
        self.help_button.grid(row=2)

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure(text="You have to pick a top and you will be getting tested on in")

    def multiplication(self):
        get_multiplication = Multiplication(self)
        get_multiplication.multiplication_text.configure(text="Fill in the boxes")

    def addition(self):
        get_addition = Addition(self)
        get_addition.addition_text.configure(text="Fill in the boxes")

    def division(self):
        get_division = Division(self,)
        get_division.division_text.configure(text="Fill in the boxes")


    def check_question(self):
        starting_questoin = self.cho_num_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.cho_num_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.addition_btn.config(state=DISABLED)
        self.division_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        def division(self, stakes):
            starting_questoin = self.question_amount.get()
            Division(self, stakes, starting_questoin)

    def check_question(self):
        starting_questoin = self.cho_num_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.cho_num_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.addition_btn.config(state=DISABLED)
        self.division_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        try:
            starting_questoin = int(starting_questoin)

            if starting_questoin < 0:
                has_error = "yes"
                error_feedback = "You need to enter a number"
            elif starting_questoin > 20:
                has_error = "yes"
                error_feedback = "unfortunately thats to high"
            elif starting_questoin >= 1:
                self.addition_btn.config(state=NORMAL)
                self.division_btn.config(state=NORMAL)
                self.multiplication_btn.config(state=NORMAL)
                error_feedback = "sorry you need a number a bit bigger"

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        if has_error == "yes":
            self.cho_num_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_questoin.set(starting_questoin)

    def division(self):
        starting_questoin = self.cho_num_entry.get()
        print(starting_questoin)

        Division(self, starting_questoin,)

        # hide start up window
        root.withdraw()



class Division:
    def __init__(self, partner,starting_questoin):
        starting_questoin = int(starting_questoin)
        background_color = "#8FF7A7"
        low_number = 1
        high_number = 10
        number_enter = [low_number,high_number]

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

        self.questions_lable = Label(self.division_frame,
                                text=starting_questoin,
                                font="arial 10 bold", fg="black",bg=background_color)
        self.questions_lable.grid(row=1)

        # Geo text (label, row 1)
        self.division_text = Label(self.division_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.division_text.grid(row=2)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.division_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_division, partner))
        self.dismiss_btn.grid(row=3)

    def close_division(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.division_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.division_box.destroy()


class Addition:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.division_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.addition_box = Toplevel()

        # Set up GUI Frame
        self.addition_frame = Frame(self.addition_box, width=300, bg=background_color)
        self.addition_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.addition_frame,
                                 text="Addition",
                                 font="arial 20 bold",bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.addition_text = Label(self.addition_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.addition_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.addition_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_addition, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_addition(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.division_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.addition_box.destroy()
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
