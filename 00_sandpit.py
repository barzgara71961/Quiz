class Subtraction:
    def __init__(self, partner, starting_question, low_amount, high_amount):
        starting_question = int(starting_question)
        low_amount = int(low_amount)
        high_amount = int(high_amount)
        background_color = "#8FF7A7"

        for item in range(starting_question):
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            correct = hi_lo_num + hi_lo_num2

        # disable button
        partner.subtraction_btn.config(state=DISABLED)
        partner.subtraction_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.subtraction_box = Toplevel()

        # Set up GUI Frame
        self.subtraction_frame = Frame(self.subtraction_box, width=300, bg=background_color)
        self.subtraction_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.subtraction_frame, text="Subtraction",
                             font="arial 20 bold", bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.subtraction_text = Label(self.subtraction_frame,
                                   text="Fill the boxes",
                                   justify=LEFT, width=50, bg=background_color, wrap=200)
        self.subtraction_text.grid(row=1)

        self.ask_questions_frame = Frame(self.subtraction_frame, bg=background_color)
        self.ask_questions_frame.grid(row=1)

        self.get1_label = Label(self.ask_questions_frame,
                                text=questions,
                                font="arial 10 bold", fg="black", bg=background_color)
        self.get1_label.grid(row=1)

        self.checking_ans_btn = Entry(self.ask_questions_frame, font="arial 15 bold")
        self.checking_ans_btn.grid(row=2)

        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#95E06C", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount,correct))
        self.check_ans_btn.grid(row=2, column=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.ask_questions_frame, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_subtraction, partner))
        self.dismiss_btn.grid(row=3)

    def check_ans(self,low_amount, high_amount,correct):
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
                                    command=lambda: self.next(low_amount, high_amount))
        self.check_ans_btn.grid(row=2, column=1)

    def next(self,low_amount, high_amount):

        hi_lo_num = random.randrange(low_amount, high_amount)
        hi_lo_num2 = random.randrange(low_amount, high_amount)
        questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
        self.get1_label.config(text=questions)
        correct = hi_lo_num + hi_lo_num2

        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#95E06C", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount,correct))
        self.check_ans_btn.grid(row=2, column=1)


    def close_subtraction(self, partner):
        # Put help button back to normal
        partner.subtraction_btn.config(state=NORMAL)
        partner.subtraction_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.subtraction_box.destroy()