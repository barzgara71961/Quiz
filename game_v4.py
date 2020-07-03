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
                                    text="This game mode gives you Addition questions ",
                                    font="arial 10 bold",wrap=200, fg=font_color, bg="#F7FE72")
        self.addition_label.grid(row=1, column=1)

        self.subtraction_btn = Button(self.cho_btn__frame,
                                   text="Subtraction", font="arial 20 bold", fg=font_color,
                                   bg=btn_color, padx=10,width=10, command=lambda: self.to_game(2))
        self.subtraction_btn.grid(row=2)

        self.subtraction_label = Label(self.cho_btn__frame,
                                    text="This game mode gives you Subtraction questions",
                                    font="arial 10 bold",wrap=200, fg=font_color, bg="#F7FE72")
        self.subtraction_label.grid(row=2, column=1)

        self.multiplication_btn = Button(self.cho_btn__frame,
                                         text="Multiplication", font="arial 20 bold", fg=font_color,
                                         bg=btn_color,padx=10,width=10, command=lambda: self.to_game(3))
        self.multiplication_btn.grid(row=3)

        self.multiplication = Label(self.cho_btn__frame,
                                    text="This game mode gives you Multiplication questions ",
                                    font="arial 10 bold", wrap=200, fg=font_color, bg="#F7FE72")
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
        get_help.help_text.configure()

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
        questions_played = int(0)

        self.correct = IntVar()
        self.correct.set(0)

        low_amount = int(low_amount)
        high_amount = int(high_amount)
        background_color = "#8FF7A7"

        op = int(op)

        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Addition"
        elif op == 2:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Subtraction"
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Multiplication"

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
        self.heading = Label(self.addition_frame, text=op_text,
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
                                    command=lambda: self.check_ans(low_amount, high_amount, op, starting_question, questions_played))
        self.check_ans_btn.grid(row=2, column=1)

        self.dismiss_export_frame = Frame(self.addition_frame, bg=background_color)
        self.dismiss_export_frame.grid(row=2)

    # Dismiss button (row 4)
        self.dismiss_btn = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg="red",
                                font="arial 10 bold",
                                command=partial(self.close_addition, partner))
        self.dismiss_btn.grid(row=1)

    def check_ans(self, low_amount, high_amount, op, starting_question, questions_played):
        answer = self.checking_ans_btn.get()

        # Set error background colour (and assum that there are no)
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        var_correct = self.correct.get()

        # change background to white (for testing purposes) ...
        self.check_ans_btn.config(bg="white")
        self.check_ans_btn.config(text="")

        try:
            answer = int(answer)
            correct = int(var_correct)

            if answer != correct:
                has_error = "yes"
                self.feedback_label = Label(self.ask_questions_frame, text=" Opp's wrong answer ",
                                         font="arial 10 bold",fg="black",bg="#8FF7A7", pady=7,)
                self.feedback_label.grid(row=3)
            elif answer == correct:
                has_error = "no"
                self.feedback_label = Label(self.ask_questions_frame, text=" That's the right answer",
                                         font="arial 10 bold", fg="black", bg="#8FF7A7", pady=7, )
                self.feedback_label.grid(row=3)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes"

        if questions_played >= starting_question:
            self.game_over_btn = Button(self.ask_questions_frame, text="Game Over", font="arial 10 bold", fg="black",
                                   bg="red", pady=7)
            self.game_over_btn.grid(row=2, column=1)
            self.export_btn = Button(self.dismiss_export_frame, text="Export", font="arial 10 bold", fg="black",
                                     bg="#95E06C", width=8,
                                     command=lambda: self.export(low_amount, high_amount, questions_played))
            self.export_btn.grid(row=1, column=1)
            self.next_btn.config(state=DISABLED)
        else:
            self.checking_ans_btn.config(text="")
            self.next_btn = Button(self.ask_questions_frame, text="Next", font="arial 10 bold", fg="black",
                                        bg="#95E06C", pady=7,
                                        command=lambda: self.next(low_amount, high_amount, op, starting_question, questions_played))
            self.next_btn.grid(row=2, column=1)

    def next(self,low_amount, high_amount, op, starting_question, questions_played):
        starting_question = int(starting_question)

        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
            print(questions_played)
        elif op == 2:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1

        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#95E06C", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount, op,
                                                                   starting_question, questions_played))
        self.check_ans_btn.grid(row=2, column=1)

    def close_addition(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=NORMAL)
        partner.subtraction_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.addition_box.destroy()

    def export(self, low_amount, high_amount, questions_played):
        Export(self, low_amount, high_amount, questions_played)


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
                               text="This is a math game "
                                    " It will help you to learn addition subtraction and multiplication \n"
                               "\n"
                                    "How do you play?\n"
                                "\n"
                                    "The first box is for how many  want to play a min of 5 and a max of 20\n"
                               "\n"
                                    "The second box is for the lowest number you want your questions to be\n"
                               "\n"
                                    "The second box is for the highest number you want your questions to be \n ",
                               justify=LEFT, width=50, bg=background_color, wrap=400, font="arial 15 ")
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

class Export:
    def __init__(self, partner, low_amount, high_amount, questions_played):

        print(low_amount, high_amount, questions_played)

        background_color = "#68B684"

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # If user press cross at top, closes export and
        # 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background_color)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export", fg="black",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename"
                                                         "in the box below"
                                                         "button to save your"
                                                         "game history"
                                                         "to a text file.",
                                 font="arial 13 italic",
                                 justify=LEFT, width=50, bg=background_color, wrap=200)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename"
                                                         "you enter below"
                                                         "already exists,"
                                                         "its contents will"
                                                         "be replaced with"
                                                         "your game"
                                                         "history",
                                 justify=LEFT, bg=background_color, fg="black",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # error massage labels (initially blank, row 4 )
        self.save_error_label = Label(self.export_frame, text="", fg="black",
                                      bg=background_color)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons 9row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="arial 10 bold", fg="black",
                                  bg="#95E06C", padx=10, pady=10,
                                  command=partial(lambda: self.save_history(partner, low_amount, high_amount,
                                                                            questions_played)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="arial 10 bold", fg="black",
                                    bg="#95E06C", padx=10, pady=10,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, low_amount, high_amount, questions_played):

        # Regular expression to check filname is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            f.write("your low number was: {}""\n".format(low_amount))
            f.write("your high number was: ${}""\n".format(high_amount))
            f.write("you have played {} around""\n".format(questions_played))
            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
