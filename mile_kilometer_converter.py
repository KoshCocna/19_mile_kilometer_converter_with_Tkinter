from tkinter import *


def mile_km_converter():
    miles = float(mile_entry.get())
    km = miles * 1.609
    kilo_label.config(text=f"{km}")


window = Tk()

window.title("Mile-Kilometer Converter")
window.config(padx=20, pady=20)

mile_entry = Entry(width=7)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_label = Label(text="0")
kilo_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calc_btn = Button(text="calculate", command=mile_km_converter)
calc_btn.grid(column=1, row=2)

window.mainloop()
