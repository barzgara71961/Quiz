from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random

class Quiz:
    def __init__(self):
        # Formatting variables...
        background_color = "#8FF7A7"

        # Converter Main Screen GUT...
        self.quiz_frame = Frame(width=500, height=500, bg=background_color)
        self.quiz_frame.grid()

        self.heading_frame = Frame(self.quiz_frame, bg=background_color)
        self.heading_frame.grid(row=0)

        # Quiz (row 0)
        self.Quiz_label = Label(self.heading_frame, text="GEOGRAPHY QUIZ",
                                font=("arial 20 bold"),
                                fg="#757761", bg=background_color)
        self.Quiz_label.grid(row=0)

        # Quiz (row 1)
        self.Quiz_instruction_label = Label(self.heading_frame, text="Pick a topic you want to have a quiz on ",
                                            font=("arial 10 bold"),
                                            fg="#757761", bg=background_color)
        self.Quiz_instruction_label.grid(row=1)

        self.cho_btn__frame = Frame(self.quiz_frame, width=300, bg=background_color)
        self.cho_btn__frame.grid(row=1)


        self.countries_btn = Button(self.cho_btn__frame, text="Capitals \nto\nCountry ", bg="#51BBFE",
                                    font="arial 14 bold", command=self.country)
        self.countries_btn.grid(row=1)


    def country(self):
        get_country = Country(self)
        get_country.country_text.configure(text="Fill in the boxes")



class Country:
    def __init__(self, partner):
        background_color = "#8FF7A7"

        countries = open('cou_caps.csv')
        csv_countries = csv.reader(countries)
        print(csv_countries)

        # Set up Geo game one
        self.Country_box = Toplevel()

        # Set up GUI Frame
        self.Country_frame = Frame(self.Country_box, width=300, bg=background_color)
        self.Country_frame.grid(row=1)
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.Country_frame,
                             text="Country",
                             font="arial 20 bold", bg=background_color)
        self.heading.grid(row=0)

        # Geo text (label, row 1)
        self.country_text = Label(self.Country_frame,
                                  text="Fill the boxes",
                                  justify=LEFT, width=50, bg=background_color, wrap=200)
        self.country_text.grid(row=1)

        self.country_names = Label(self.Country_frame,
                                   text=random.choice(countries),
                                   font="arial 15 bold", bg=background_color)
        self.country_names.grid(row=2)

        self.capital_entry = Entry(self.Country_box,
                                   font=("arial 10 bold"))
        self.capital_entry.grid(row=3, column=1)
        self.add_funds_button = Button(self.Country_box, text="My Answer", font="arial 10 bold", fg="black",
                                       bg=background_color, )
        self.add_funds_button.grid(row=3, column=2)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.Country_box, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_country, partner))
        self.dismiss_btn.grid(row=4)

    def close_country(self, partner):
        # Put help button back to normal
        partner.countries_btn.config(state=NORMAL)

        self.Country_box.destroy()
