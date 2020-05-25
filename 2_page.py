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

        self.button_lable_frame = Frame(self.quiz_frame,bg=background_color)
        self.button_lable_frame.grid(row=1)

        self.geo_button = Button(self.button_lable_frame,
                                  text="Geography", font="arial 20 bold", fg="#757761",
                                  bg="#51BBFE",padx=5,command=self.geo)
        self.geo_button.grid(row=2)

        self.geo_label = Label(self.button_lable_frame,
                                text="This will give you a test about capital",
                                font="arial 10 bold", fg="#757761",bg="#F7FE72")
        self.geo_label.grid(row=2,column=1)

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

    def geo(self):
        geo = Geo(self)
        geo.geo_text.configure(text="Fill the boxes")

class Geo:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable button
        partner.geo_button.config(state=DISABLED)

        # Set up Geo game one
        self.geo_box = Toplevel()
        # Set up GUI Frame
        self.heading_frame = Frame(self.geo_box, width=300, bg=background_color)
        self.heading_frame.grid(row=1)
        # Set up Geo Instruction heading (row 0)
        self.how_heading = Label(self.heading_frame,
                                 text="Geo",
                                 font="arial 20 bold",bg=background_color)
        self.how_heading.grid(row=0)
        # Geo text (label, row 1)
        self.geo_text = Label(self.heading_frame,
                               text="Fill the boxes",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.geo_text.grid(column=0,row=1)

        self.cho_btn__frame = Frame(self.geo_box, width=300, bg=background_color)
        self.cho_btn__frame.grid(row=2)

        self.capital_btn = Button(self.cho_btn__frame,text="Capitals",width=10,bg="#51BBFE",
                                  font="arial 20 bold")
        self.capital_btn.grid(row=1,column=1)

        self.countries_btn = Button(self.cho_btn__frame,text="Countries ",width=10,bg="#51BBFE",
                                  font="arial 20 bold")
        self.countries_btn.grid(row=1,column=2)


        # Set up GUI Frame
        self.diss_btn__frame = Frame(self.geo_box, width=300, bg=background_color)
        self.diss_btn__frame.grid(row=3)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.diss_btn__frame,text="Dismiss",width=10,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_geo, partner))
        self.dismiss_btn.grid(row=2)

    def close_geo(self, partner):
        # Put help button back to normal
        partner.geo_button.config(state=NORMAL)
        self.geo_box.destroy()

class Help:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        # disable help button
        partner.geo_button.config(state=DISABLED)

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
        partner.geo_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
