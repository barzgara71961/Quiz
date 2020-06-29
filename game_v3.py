from tkinter import *
from functools import partial  # To prevent unwanted windows

import random

class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "#8FF7A7"
        btn_color = "#51BBFE"
        font_color = "black"

        self.quiz_frame = Frame(width=500, height=500, bg=background_color)
        self.quiz_frame.grid()

        self.starting_question = IntVar()
        self.starting_question.set(0)

        self.low_amount = IntVar()
        self.low_amount.set(0)

        self.high_amount = IntVar()
        self.high_amount.set(0)

        self.heading_frame = Frame(self.quiz_frame, bg=background_color)
        self.heading_frame.grid(row=0)

        # Quiz (row 0)
        self.Quiz_label = Label(self.heading_frame, text="MATH QUIZ",
                                font="arial 20 bold",
                                fg=font_color, bg=background_color)
        self.Quiz_label.grid(row=0)

        # Quiz (row 1)
        self.choicing_frame = Frame(self.quiz_frame, bg=background_color)
        self.choicing_frame.grid(row=1)

        self.amount_error_label = Label(self.choicing_frame, font="arial 10 italic",
                                        text="", bg=background_color)
        self.amount_error_label.grid(row=0)

        self.cho_num_label = Label(self.choicing_frame, text="How many question would you like",
                                   font="arial 10 bold",
                                   fg=font_color, bg=background_color)
        self.cho_num_label.grid(row=1)

        self.cho_num_entry = Entry(self.choicing_frame,
                                   font="arial 10 bold", width=5)
        self.cho_num_entry.grid(row=1, column=1)

        self.low_num_label = Label(self.choicing_frame, text="low number amout",
                                   font="arial 10 bold",
                                   fg=font_color, bg=background_color)
        self.low_num_label.grid(row=2)

        self.low_num_entry = Entry(self.choicing_frame,
                                   font="arial 10 bold", width=5)
        self.low_num_entry.grid(row=2, column=1)

        self.high_num_label = Label(self.choicing_frame, text="high number amout",
                                    font="arial 10 bold",
                                    fg=font_color, bg=background_color)
        self.high_num_label.grid(row=3)

        self.high_num_entry = Entry(self.choicing_frame,
                                    font="arial 10 bold", width=5)
        self.high_num_entry.grid(row=3, column=1)

        self.question_amount_btn = Button(self.choicing_frame, text="Enter", bg=btn_color,
                                          font="arial 14 bold", command=self.check_question)
        self.question_amount_btn.grid(row=4, )

        self.cho_btn__frame = Frame(self.quiz_frame, width=300, bg=background_color)
        self.cho_btn__frame.grid(row=2)

        self.addition_btn = Button(self.cho_btn__frame, text="Addition", font="arial 20 bold", fg=font_color,
                                   bg=btn_color,padx=10,width=10, command=lambda: self.to_game(1))
        self.addition_btn.grid(row=1)

        self.addition_label = Label(self.cho_btn__frame,
                                    text="this is a place holder",
                                    font="arial 10 bold", fg=font_color, bg="#F7FE72")
        self.addition_label.grid(row=1, column=1)

        self.subtraction_btn = Button(self.cho_btn__frame,
                                   text="Subtraction", font="arial 20 bold", fg=font_color,
                                   bg=btn_color, padx=10,width=10, command=lambda: self.to_game(2))
        self.subtraction_btn.grid(row=2)

        self.subtraction_label = Label(self.cho_btn__frame,
                                    text="this is a place holder",
                                    font="arial 10 bold", fg=font_color, bg="#F7FE72")
        self.subtraction_label.grid(row=2, column=1)

        self.multiplication_btn = Button(self.cho_btn__frame,
                                         text="Multiplication", font="arial 20 bold", fg=font_color,
                                         bg=btn_color,padx=10,width=10, command=lambda: self.to_game(3))
        self.multiplication_btn.grid(row=3)

        self.multiplication = Label(self.cho_btn__frame,
                                    text="this is a place holder ",
                                    font="arial 10 bold", fg=font_color, bg="#F7FE72")
        self.multiplication.grid(row=3, column=1)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=3)

        self.addition_btn.config(state=DISABLED)
        self.subtraction_btn.config(state=DISABLED)
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

    def check_question(self):
        starting_question = self.cho_num_entry.get()
        low_amount = self.low_num_entry.get()
        high_amount = self.high_num_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.cho_num_entry.config(bg="white")
        self.amount_error_label.config(text="")
        self.low_num_entry.config(bg="white")
        self.low_num_entry.config(text="")
        self.high_num_entry.config(bg="white")
        self.high_num_entry.config(text="")

        self.addition_btn.config(state=DISABLED)
        self.subtraction_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        try:
            starting_question = int(starting_question)

            if starting_question <5:
                has_error = "yes"
                error_feedback = "You need to enter a number"
            elif starting_question > 20:
                has_error = "yes"
                error_feedback = "unfortunately that's to high"
            elif starting_question >=5:
                error_feedback = "You need a minimum of 5 questions "

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        try:
            low_amount = int(low_amount)

            if low_amount < -10000:
                has_error = "yes"
                error_feedback = "this number is to low"
            elif low_amount > 9999999999:
                has_error = "yes"
                error_feedback = "unfortunately thats to high"
            elif low_amount >= 1:
                error_feedback = "sorry you need a number a bit bigger"

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        try:
            high_amount = int(high_amount)

            if high_amount < -10000:
                has_error = "yes"
                error_feedback = "this number is to low"
            elif high_amount > 9999999999:
                has_error = "yes"
                error_feedback = "unfortunately thats to high"
            elif high_amount >= 1:
                self.addition_btn.config(state=NORMAL)
                self.subtraction_btn.config(state=NORMAL)
                self.multiplication_btn.config(state=NORMAL)
                error_feedback = "sorry you need a number a bit bigger"

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        if has_error == "yes":
            self.cho_num_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
            self.high_num_entry.config(bg=error_back)
            # self.high_num_entry.config(text=error_feedback)
            self.low_num_entry.config(bg=error_back)
            # self.low_num_entry.config(text=error_feedback)

        else:
            self.starting_question.set(starting_question)
            self.low_amount.set(low_amount)
            self.high_amount.set(high_amount)

    def to_game(self, op):
        starting_question = self.cho_num_entry.get()
        low_amount = self.low_num_entry.get()
        high_amount = self.high_num_entry.get()
        print(starting_question, low_amount, high_amount)

        Game(self, op,starting_question, low_amount, high_amount)


class Game:
    def __init__(self, partner, op, starting_question, low_amount, high_amount):
        starting_question = int(starting_question)
        low_amount = int(low_amount)
        high_amount = int(high_amount)
        background_color = "#8FF7A7"
        op = int(op)


        if op == 1:
            for item in range(starting_question):
                hi_lo_num = random.randrange(low_amount, high_amount)
                hi_lo_num2 = random.randrange(low_amount, high_amount)
                questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
                correct = hi_lo_num + hi_lo_num2
        elif op == 2:
            for item in range(starting_question):
                hi_lo_num = random.randrange(low_amount, high_amount)
                hi_lo_num2 = random.randrange(low_amount, high_amount)
                questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
                correct = hi_lo_num - hi_lo_num2
        elif op == 3:
            for item in range(starting_question):
                hi_lo_num = random.randrange(low_amount, high_amount)
                hi_lo_num2 = random.randrange(low_amount, high_amount)
                questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
                correct = hi_lo_num * hi_lo_num2

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.subtraction_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.addition_box = Toplevel()

        # Set up GUI Frame
        self.addition_frame = Frame(self.addition_box, width=300, bg=background_color)
        self.addition_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.addition_frame, text="Addition",
                             font="arial 20 bold", bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.game = Label(self.addition_frame,
                                   text="Fill the boxes",
                                   justify=LEFT, width=50, bg=background_color, wrap=200)
        self.game.grid(row=1)

        self.ask_questions_frame = Frame(self.addition_frame, bg=background_color)
        self.ask_questions_frame.grid(row=1)

        self.get1_label = Label(self.ask_questions_frame,
                                text=questions,
                                font="arial 10 bold", fg="black", bg=background_color)
        self.get1_label.grid(row=1)

        self.checking_ans_btn = Entry(self.ask_questions_frame, font="arial 15 bold")
        self.checking_ans_btn.grid(row=2)

        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#95E06C", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount,correct,op))
        self.check_ans_btn.grid(row=2, column=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.ask_questions_frame, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_addition, partner))
        self.dismiss_btn.grid(row=3)

    def check_ans(self,low_amount, high_amount,correct,op):
        answer = self.checking_ans_btn.get()

        # Set error background colour (and assum that there are no)
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.check_ans_btn.config(bg="white")
        self.check_ans_btn.config(text="")

        try:
            answer = int(answer)
            correct = int(correct)

            if answer != correct:
                has_error = "yes"
                self.wrong_label = Label(self.ask_questions_frame, text=" opp's wrong answer",
                                         font="arial 10 bold",fg="black",bg="#95E06C", pady=7,)
                self.wrong_label.grid(row=3)
            elif answer == correct:
                has_error = "no"
                self.right_label = Label(self.ask_questions_frame, text=" that's the right answer",
                                         font="arial 10 bold", fg="black", bg="#95E06C", pady=7, )
                self.right_label.grid(row=3)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes"

        if has_error == "yes":
            self.check_ans_btn.config(bg=error_back)
            self.check_ans_btn.config(text=error_feedback)

        self.check_ans_btn = Button(self.ask_questions_frame, text="Next", font="arial 10 bold", fg="black",
                                    bg="#95E06C", pady=7,
                                    command=lambda: self.next(low_amount, high_amount,op))
        self.check_ans_btn.grid(row=2, column=1)

    def next(self,low_amount, high_amount,op):

        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            correct = hi_lo_num + hi_lo_num2
        elif op == 2:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            correct = hi_lo_num - hi_lo_num2
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            correct = hi_lo_num * hi_lo_num2

        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#95E06C", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount,correct,op))
        self.check_ans_btn.grid(row=2, column=1)


    def close_addition(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.subtraction_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.addition_box.destroy()

class Help:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable help button
        partner.addition_btn.config(state=DISABLED)
        partner.subtraction_btn.config(state=DISABLED)
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
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="i have no idea where this is going to be",
                               justify=LEFT, width=50, bg=background_color, wrap=200)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.subtraction_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
