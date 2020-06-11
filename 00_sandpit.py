def check_question(self):
    question_amount = self.cho_num_entry.get()

    # Set error background colour (and assum that there are no
    # error at the start
    error_back = "#ffafaf"
    has_error = "no"
    error_feedback = ""

    # change background to white (for testing purposes) ...
    self.cho_num_entry.config(bg="white")
    self.amount_error_label.config(text="")

    partner.addition_btn.config(state=DISABLED)
    partner.division_btn.config(state=DISABLED)
    partner.multiplication_btn.config(state=DISABLED)


def check_question(self):
    question_amount = self.cho_num_entry.get()

    # Set error background colour (and assum that there are no
    # error at the start
    error_back = "#ffafaf"
    has_error = "no"
    error_feedback = ""

    # change background to white (for testing purposes) ...
    self.cho_num_entry.config(bg="white")
    self.amount_error_label.config(text="")

    partner.addition_btn.config(state=DISABLED)
    partner.division_btn.config(state=DISABLED)
    partner.multiplication_btn.config(state=DISABLED)

    try:
        question_amount = int(question_amount)

        if question_amount <0:
            has_error = "yes"
            error_feedback = "did you not read the instructions\n" \
                             "a minimum of $5 "
        elif question_amount > 20:
            has_error = "yes"
            error_feedback = "unfortunately I can't steal that much money"
        elif question_amount >= 1:
            partner.addition_btn.config(state=NORMAL)
            partner.division_btn.config(state=NORMAL)
            partner.multiplication_btn.config(state=NORMAL)
            error_feedback = "sorry you are too cheap"

    except ValueError:
        has_error = "yes"
        error_feedback = "Please enter a dollar amount"

    if has_error == "yes":
        self.cho_num_entry.config(bg=error_back)
        self.amount_error_label.config(text=error_feedback)

    else:
        self.question_amount.set(question_amount)
